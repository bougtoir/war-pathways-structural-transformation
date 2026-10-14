"""
Sisyphean Lever — hybrid stochastic model of aggressive-war onset and
self-undermining sustainment.

State per simulation (discrete time, dt=1 period):
  q  dispute pressure (OU + jump shocks)
  c  conflict intensity (0..1); W set = {war_on and c >= C_W}
  m  aggressor mobilization capacity
  v  political value of conquest to the aggressor
  K  keystone sustainment stock for AGGRESSIVE war only
     (fiscal reserves + coalition support + materiel). The defender's
     sustainment is modeled separately and does NOT draw down K.
  h  civilian functionality (0..1)
  d  defender capacity (0..1)
  r  institutional resilience (0..1), fixed here
  S_p stockpile buffer feeding K before replenishment matters

Onset (Gate 11): each pre-war period a selection rule (Gate 15) may fire;
onset requires selection AND feasibility (m >= m_req(v)) AND barrier check.
Barrier B: onset succeeds only if a uniform draw < exp(-B * ...) — raised
barriers reduce the rate for ALL selection rules.

In-war (Gate 12): dK = -kappa_burn * c * m + sponsor + stockpile_release.
Self-undermining when burn exceeds replenishment. War exits when K <= K_min
or c resolves (simplified: forced exit on K starvation or max duration).

Civilian harm (Gate 14): dh = -harm_c * c; constraint interventions never
raise harm (we measure harm; deprivation as a mechanism is out of scope).
Defense (Gate 14): on onset, d grows toward d_max; defense drains the
attacker's v-gain and raises burn (resistance cost) but does NOT deplete
defender sustainment to zero (defender sustainment is asymmetric:
defensive effort is sustained by h).

Relapse (Gate 13): after exit, K regrows; grievance q persists -> new
onset possible -> count recurrences; >=2 onsets = oscillation flag.
Displacement: blocked onset can reroute to substate violence event.

All numbers ILLUSTRATIVE. Seeds fixed.
"""
import numpy as np
import pandas as pd
from dataclasses import dataclass, field, replace

C_W = 0.5          # war-intensity threshold
K_MIN = 0.05       # sustainment floor -> forced exit
T_MAX = 300        # horizon


@dataclass
class P:
    # dispute pressure
    a_q: float = 0.10; sig_q: float = 0.12; jump_rate: float = 0.08
    jump_scale: float = 0.35; shock_dist: str = "normal"   # or "cauchy"
    # selection
    rule: str = "eu"          # eu | noisy | aspiration | bureaucratic
    iota: float = 0.0         # intrinsic valuation of aggression (>=0)
    temp: float = 0.10        # noisy-rule temperature
    asp_gap: float = 0.55     # aspiration grievance threshold
    m_routine: float = 0.75   # bureaucratic mobilization precedent
    e_b: float = 0.30         # bureaucratic firing error prob.
    # feasibility / barrier
    m_req0: float = 0.35; B: float = 0.0
    # mobilization dual-use (Gate 16)
    o: float = 0.30; spill: float = 0.0
    # keystone
    K0: float = 1.0; kappa: float = 0.045; sponsor: float = 0.010
    S_p0: float = 0.30; s_release: float = 0.05
    v0: float = 0.80
    # in-war
    c_rate: float = 0.25      # intensity convergence rate toward 1
    dur_max: int = 80
    # civilians / defense
    harm_c: float = 0.010; protect: float = 0.60
    d0: float = 0.30; d_max: float = 0.85; d_rate: float = 0.10
    resist_burn: float = 0.03   # defender resistance adds to attacker burn
    h_min: float = 0.50; d_min: float = 0.30
    # recovery / relapse
    K_regrow: float = 0.008; q_decay: float = 0.0  # grievance persists unless decayed
    p_disp: float = 0.35       # displacement probability when onset blocked


def eu_utilities(x, p):
    """Simplified leader-level utility comparison (aggressor side).
    U_W = v + iota - expected cost; U_A = settlement share."""
    G, pwin = x["v"], x["d"]  # defender capacity lowers expected gain
    alpha, a = 0.5, 0.3
    UW = p.v0 * (1 - 0.6 * pwin) + p.iota - (0.35 + 0.3 * p.o)
    UA = alpha * 0.5 * (1 - pwin) - 0.05 + 0.25 * a
    return UW, UA


def selection_fires(x, p, rng):
    """Return True if the aggressor's decision rule selects force."""
    UW, UA = eu_utilities(x, p)
    if p.rule == "eu":
        return UW > UA
    if p.rule == "noisy":
        return rng.random() < 1 / (1 + np.exp(-(UW - UA) / p.temp))
    if p.rule == "aspiration":
        return x["q"] > p.asp_gap and UW > 0   # satisficing, not optimizing
    if p.rule == "bureaucratic":
        fires = x["m"] > p.m_routine
        return fires if rng.random() > p.e_b else not fires
    raise ValueError(p.rule)


def step(x, p, rng):
    """One period. x dict mutated via returned dict."""
    # grievance dynamics (OU + jumps)
    dq = -p.a_q * x["q"] + p.sig_q * rng.standard_normal()
    if rng.random() < p.jump_rate:
        shock = (rng.standard_cauchy() if p.shock_dist == "cauchy"
                 else rng.standard_normal()) * p.jump_scale
        dq += abs(shock)
    x["q"] = float(np.clip(x["q"] + dq - p.q_decay * x["q"], 0, 1))

    # mobilization with dual-use channels: o raises cost, spill grows m
    m_target = min(1.0, 0.6 + p.spill - 0.4 * p.o)
    x["m"] += 0.05 * (m_target - x["m"])

    if not x["war"]:
        if selection_fires(x, p, rng):
            feasible = x["m"] >= p.m_req0 + 0.1 * x["v"]
            barrier = rng.random() < np.exp(-p.B)
            if feasible and barrier:
                x["war"] = True
                x["c"] = max(x["c"], C_W)
                return x, "onset"
            elif not barrier:
                return x, "blocked_barrier"
            else:
                return x, "blocked_feasibility"
        return x, None

    # --- in-war dynamics ---
    x["c"] += p.c_rate * (1 - x["c"])              # intensity -> 1
    # keystone: burn vs replenishment; defender resistance adds burn
    burn = p.kappa * x["c"] * x["m"] + p.resist_burn * x["d"]
    rel = min(p.s_release, x["S_p"])
    x["S_p"] -= rel
    x["K"] += -burn + p.sponsor + rel
    # defender buildup (asymmetric: doesn't drain K)
    x["d"] += p.d_rate * (p.d_max - x["d"]) * (x["h"] > p.h_min * 0.6)
    # civilian harm
    x["h"] = max(0.0, x["h"] - p.harm_c * x["c"] * (1 - p.protect))
    x["t_war"] += 1
    if x["K"] <= K_MIN or x["t_war"] >= p.dur_max:
        x["war"] = False
        x["exit_reason"] = "K_starved" if x["K"] <= K_MIN else "dur_max"
        x["c"] = C_W * 0.5                          # intensity collapses
        return x, "exit"
    return x, None


def simulate(p, rng, T=T_MAX):
    x = dict(q=0.3, c=0.0, m=0.5, v=p.v0, K=p.K0, S_p=p.S_p0,
             h=1.0, d=p.d0, war=False, t_war=0, exit_reason=None)
    hits, exits, blocked = [], [], {"barrier": 0, "feasibility": 0}
    harm_cum, in_war = 0.0, False
    disp_events = 0
    war_spells, spell_len = 0, 0
    for t in range(T):
        x, ev = step(x, p, rng)
        if not x["war"]:
            x["K"] = min(p.K0, x["K"] + p.K_regrow * (p.K0 - x["K"]))
        if ev == "onset":
            hits.append(t); war_spells += 1; spell_len = 0
        elif ev == "exit":
            exits.append((t, x["exit_reason"], x["t_war"], x["h"]))
        elif ev == "blocked_barrier":
            blocked["barrier"] += 1
            if rng.random() < p.p_disp:
                disp_events += 1
        elif ev == "blocked_feasibility":
            blocked["feasibility"] += 1
        harm_cum += (1 - x["h"]) * p.harm_c if x["war"] else 0.0
        if x["war"]:
            spell_len += 1
    hit_prob = 1.0 if hits else 0.0
    return dict(
        hit_W=hit_prob, first_hit=hits[0] if hits else np.nan,
        n_onsets=war_spells, oscillation=int(war_spells >= 2),
        exits=exits, blocked=blocked, displaced=disp_events,
        harm_cum=harm_cum, h_final=x["h"], d_final=x["d"],
        K_final=x["K"],
        mean_spell=np.mean([e[2] for e in exits]) if exits else np.nan,
        defender_ok=x["d"] >= p.d_min, civilian_ok=x["h"] >= p.h_min,
    )


def mc(p, n=2000, T=T_MAX, seed=1):
    rng = np.random.default_rng(seed)
    rows = [simulate(p, rng, T) for _ in range(n)]
    df = pd.DataFrame(rows)
    agg = dict(
        p_hit_W=df["hit_W"].mean(),
        p_oscillation=df["oscillation"].mean(),
        mean_onsets=df["n_onsets"].mean(),
        mean_spell=np.nanmean(df["mean_spell"]),
        mean_first_hit=np.nanmean(df["first_hit"]),
        harm_cum_mean=df["harm_cum"].mean(),
        harm_cum_p90=df["harm_cum"].quantile(0.9),
        h_final_mean=df["h_final"].mean(),
        defender_ok=df["defender_ok"].mean(),
        civilian_ok=df["civilian_ok"].mean(),
        displaced_mean=df["displaced"].mean(),
        blocked_barrier=df["blocked"].map(lambda b: b["barrier"]).mean(),
        blocked_feas=df["blocked"].map(lambda b: b["feasibility"]).mean(),
        p_K_exit=np.mean([1 if any(e[1] == "K_starved" for e in r["exits"])
                          else 0 for _, r in df.iterrows()]),
    )
    return agg, df
