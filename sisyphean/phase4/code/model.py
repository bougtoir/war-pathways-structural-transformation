"""
Sisyphean Lever — PHASE 3 model.
Endogenous keystone + political-value collapse + protected recovery.

Separates, per the prompt:
  V_G(t)  objective efficacy — can G still be achieved by force?
  U_L(t)  leader's perceived utility of continuing
  M(t)    military feasibility
  K(t)    sustainment stock (aggressor)
  rho(t)  sustainment REPLENISHMENT LAW (endogenous; sponsors set it)
  H(t)    civilian welfare
  D(t)    defender capability
  L(t)    consent/legitimacy of third-party cooperation with the aggressor

Goal types G_TYPE:
  territory | security | status | identity | regime_survival | intrinsic

CHANNEL A (functional-value collapse): force attains G only through
  cooperation legibility — territory needs consenting governance, status
  needs recognition, security needs stable deterrence. Onset makes
  consent-holders withdraw (actor mechanism below), so V_G falls even when
  battlefield position improves. For 'intrinsic' and 'regime_survival',
  V_G does NOT collapse — war can rationally-for-the-actor continue.
CHANNEL B (sustainment collapse): onset changes rho(t), not just stock:
  sponsors recompute support conditional on externalities; patron may
  exit, balancer enters on defender side, substitution markets open.

ACTOR MECHANISM (Gate 19): two populations —
  * consent-holders (rate phi_c): cooperation leg L follows the observed
    onset and ongoing harm h_use; each period cooperation decays toward
    L_floor when war_on, recovers otherwise. Two non-maximizing rules
    implemented: 'habitual' (L tracks past war experience) and
    'threshold' (withdraw when cumulative observed harm > tau_i, tau_i
    heterogeneous). Under BOTH, L falls endogenously after onset.
  * sponsors: 'patron' supports aggressor while its externality price
    e(t)=c*ext is below tolerance tol_p; exits when exceeded, re-enters
    when c subsides. 'balancer' enters defender side proportional to c.
    Substitution market opens at rate sub when patron exits — bounded.

Non-circularity: nothing writes "V_G -= onset". V_G = g_attain(L, position)
with g_attain depending on goal type; L falls only through the actor
mechanism. If actors don't withdraw, V_G stays — falsifiable by params.

All parameters ILLUSTRATIVE. Seeds fixed.
"""
import numpy as np
import pandas as pd
from dataclasses import dataclass, field, replace

C_W = 0.5
K_MIN = 0.05


@dataclass
class P3:
    # dispute pressure
    a_q: float = 0.10; sig_q: float = 0.12; jump_rate: float = 0.08
    jump_scale: float = 0.35; shock_dist: str = "normal"
    # leader selection rule
    rule: str = "eu"          # eu|noisy|aspiration|bureaucratic|intrinsic|regime_survival
    iota: float = 0.0; temp: float = 0.10; asp_gap: float = 0.55
    m_routine: float = 0.75; e_b: float = 0.30
    # goal
    g_type: str = "territory"
    # feasibility / barrier
    m_req0: float = 0.35; B: float = 0.0
    # dual-use
    o: float = 0.30; spill: float = 0.0
    # sustainment stock + endogenous replenishment
    K0: float = 1.0; kappa: float = 0.045
    S_p0: float = 0.30; s_release: float = 0.05
    rho_dom: float = 0.010        # domestic replenishment (fixed)
    # sponsors (endogenous, Gate 21)
    patron_in: bool = True; tol_patron: float = 0.60
    patron_flow: float = 0.030    # inflow while patron present
    patron_ext: float = 1.0       # externality weight * c -> patron exit
    patron_reenter: float = 0.30  # re-enter when c < this
    balancer_gain: float = 0.020  # defender support rate ∝ c
    sub_rate: float = 0.012       # black-market substitution when patron out
    # consent/legitimacy actors (Channel A)
    consent_rule: str = "threshold"  # 'habitual' | 'threshold'
    L0: float = 1.0; L_floor: float = 0.05; L_decay: float = 0.06
    L_recover: float = 0.02; harm_weight: float = 1.0
    # objective efficacy
    v0: float = 0.80; collapse_rate: float = 0.08
    # in-war
    c_rate: float = 0.25; dur_max: int = 80
    resist_burn: float = 0.03
    # civilians / defense (dynamically coupled, Gate 23)
    harm_c: float = 0.010; infra_coupling: float = 0.5
    protect: float = 0.60
    d0: float = 0.30; d_max: float = 0.85; d_rate: float = 0.10
    h_min: float = 0.50; d_min: float = 0.30
    # recovery
    K_regrow: float = 0.008; q_decay: float = 0.0; p_disp: float = 0.35
    # null-model controls (Gate 26)
    stepdown: float = -1.0   # >=0: V_G forced to this AT onset (exogenous)
    # Phase 4 additions
    exit_delay: int = 0      # periods e>tol must persist before patron exits
    rho_sig: float = 0.0     # stochastic replenishment noise sd (bounded)
    p_misid: float = 0.0     # false-positive aggressor identification prob
    p_preempt: float = 0.0   # preemptive defender strike when barrier blocks
    disp_persist: int = 0    # displaced conflict duration (0 = instant count)
    exog_L: bool = False     # Gate30 null: consent collapse w/o sponsors
    disp_to_civ: float = 0.4      # displaced violence harms civilians too
    hollow_thr: float = 0.2      # hollow-war threshold (sensitivity G29)


# ---------- objective efficacy (Channel A) ----------
def goal_efficacy(g_type, L, pos):
    """V_G = attainable political value. pos = battlefield position [0,1].
    Coercion-dependent goals need consent L; others don't."""
    if g_type in ("territory", "status", "identity", "security"):
        return pos * (0.3 + 0.7 * L)      # consent-starved success hollow
    if g_type == "regime_survival":
        return pos                        # survival doesn't need consent
    if g_type == "intrinsic":
        return 0.2 + 0.8 * pos            # aggression valued for itself
    raise ValueError(g_type)


# ---------- leader utility (may diverge from V_G) ----------
def leader_utility(x, p):
    pos = x["pos"]
    U = (x["V_G"] * (1 - 0.3 * pos) + p.iota
         + (0.35 if p.g_type == "intrinsic" else 0.0)
         + (0.45 if p.g_type == "regime_survival" and x["war"] else 0.0)
         - (0.35 + 0.3 * p.o))
    UA = 0.5 * 0.5 * (1 - pos) - 0.05 + 0.075
    return U, UA


def selection_fires(x, p, rng):
    UW, UA = leader_utility(x, p)
    r = p.rule
    if r == "eu":
        return UW > UA
    if r == "noisy":
        return rng.random() < 1 / (1 + np.exp(-(UW - UA) / p.temp))
    if r == "aspiration":
        return x["q"] > p.asp_gap and UW > 0
    if r == "bureaucratic":
        f = x["m"] > p.m_routine
        return f if rng.random() > p.e_b else not f
    if r == "intrinsic":                    # never optimizes: fires on capacity
        return x["m"] > p.m_req0 and rng.random() < 0.6
    if r == "regime_survival":              # fires whenever threatened/extant
        return (x["q"] > 0.25) or x["war"]
    raise ValueError(r)


def consent_step(x, p):
    """Third-party cooperation dynamics — the actor mechanism."""
    if p.consent_rule == "habitual":
        target = p.L_floor if x["war"] else 1.0
        x["L"] += p.L_decay * (target - x["L"])
        if not x["war"]:
            x["L"] = min(1.0, x["L"] + p.L_recover * (1 - x["L"]))
    else:  # threshold: withdraws once cumulative observed harm passes level
        if x["war"]:
            x["obs_harm"] += p.harm_weight * x["c"]
            if x["obs_harm"] > x["tau_i"]:
                x["L"] += p.L_decay * (p.L_floor - x["L"])
        else:
            x["obs_harm"] = max(0.0, x["obs_harm"] - 0.5)
            x["L"] = min(1.0, x["L"] + p.L_recover * (1 - x["L"]))
    x["L"] = float(np.clip(x["L"], 0, 1))


def sponsor_step(x, p, rng):
    """Endogenous replenishment rho(t): patron exit/entry (with delay),
    balancer, substitution market, bounded stochastic noise."""
    e = x["c"] * p.patron_ext if x["war"] else 0.0
    if x["patron"]:
        x["e_streak"] = x["e_streak"] + 1 if e > p.tol_patron else 0
        if x["e_streak"] > p.exit_delay:
            x["patron"] = False
            x["t_patron_exit"] = x["t_war"]
    else:
        if not x["war"] or e < p.patron_reenter:
            x["patron"] = True
            x["e_streak"] = 0
    rho = p.rho_dom + (p.patron_flow if x["patron"] else 0.0)
    rho += 0.0 if x["patron"] else p.sub_rate   # substitution opens
    rho = max(0.0, rho + p.rho_sig * rng.standard_normal())
    x["rho"] = rho
    x["balancer"] = p.balancer_gain * x["c"] if x["war"] else 0.0


def step3(x, p, rng):
    dq = -p.a_q * x["q"] + p.sig_q * rng.standard_normal()
    if rng.random() < p.jump_rate:
        s = (rng.standard_cauchy() if p.shock_dist == "cauchy"
             else rng.standard_normal()) * p.jump_scale
        dq += abs(s)
    x["q"] = float(np.clip(x["q"] + dq - p.q_decay * x["q"], 0, 1))
    x["m"] += 0.05 * (min(1.0, 0.6 + p.spill - 0.4 * p.o) - x["m"])

    consent_step(x, p)
    sponsor_step(x, p, rng)

    if not x["war"]:
        if selection_fires(x, p, rng):
            feasible = x["m"] >= p.m_req0 + 0.1 * x["V_G"]
            barrier = rng.random() < np.exp(-p.B)
            if feasible and barrier:
                x["war"] = True
                x["c"] = max(x["c"], C_W)
                if rng.random() < p.p_misid:
                    x["misid"] = True   # defender labeled aggressor:
                                        # roles' burn/protect swap not
                                        # modeled — flagged as failure
                if p.stepdown >= 0:
                    x["V_G"] = p.stepdown
                return x, "onset"
            if not barrier and rng.random() < p.p_preempt:
                x["preempts"] += 1     # adversarial first strike by the
                                       # threatened party (counted only)
            return x, ("blocked_barrier" if not barrier
                       else "blocked_feasibility")
        return x, None

    # --- in war ---
    x["c"] += p.c_rate * (1 - x["c"])
    x["pos"] += 0.05 * (x["m"] - x["d"])          # battlefield position
    x["pos"] = float(np.clip(x["pos"], 0, 1))
    # Channel A: V_G updates from consent + position (endogenous)
    if p.stepdown < 0:
        x["V_G"] = goal_efficacy(p.g_type, x["L"], x["pos"])
    # Channel B: burn vs endogenous rho
    burn = p.kappa * x["c"] * x["m"] + p.resist_burn * x["d"]
    rel = min(p.s_release, x["S_p"])
    x["S_p"] -= rel
    x["K"] += -burn + x["rho"] + rel
    # defender: supported by balancer, coupled to civilian infra
    x["d"] += p.d_rate * (p.d_max - x["d"]) * (x["h"] > 0.6 * p.h_min) \
        + x["balancer"] * (1 - x["d"])
    x["d"] = float(np.clip(x["d"], 0, 1))
    # civilians: war harms; low h degrades defense infrastructure (coupled)
    x["h"] = max(0.0, x["h"] - p.harm_c * x["c"] * (1 - p.protect))
    x["t_war"] += 1
    if x["K"] <= K_MIN or x["t_war"] >= p.dur_max:
        x["war"] = False
        x["exit_reason"] = ("K_starved" if x["K"] <= K_MIN else "dur_max")
        x["c"] = C_W * 0.5
        return x, "exit"
    return x, None


def simulate3(p, rng, T=300, tau_i=None):
    x = dict(q=0.3, c=0.0, m=0.5, v=p.v0, V_G=p.v0, pos=0.5,
             K=p.K0, S_p=p.S_p0, rho=p.rho_dom, h=1.0, d=p.d0,
             L=p.L0, obs_harm=0.0, tau_i=(tau_i if tau_i is not None
                                          else 6.0 + 2.0 * rng.random()),
             patron=p.patron_in, balancer=0.0, e_streak=0,
             t_patron_exit=None, misid=False, preempts=0,
             proxy=0, proxy_left=0,
             war=False, t_war=0, exit_reason=None)
    hits, exits = [], []
    blocked = {"barrier": 0, "feasibility": 0}
    disp = 0
    harm_cum, peak_intensity = 0.0, 0.0
    violence_periods = 0
    spells = 0
    vg_collapses = 0
    war_continues_hollow = 0   # periods where V_G<hollow_thr and war on
    for t in range(T):
        x, ev = step3(x, p, rng)
        if not x["war"]:
            x["K"] = min(p.K0, x["K"] + p.K_regrow * (p.K0 - x["K"]))
        if ev == "onset":
            hits.append(t); spells += 1
        elif ev == "exit":
            exits.append((t, x["exit_reason"], x["t_war"], x["h"]))
        elif ev == "blocked_barrier":
            blocked["barrier"] += 1
            if rng.random() < p.p_disp:
                disp += 1
                if p.disp_persist > 0:
                    x["proxy"] += 1
                    x["proxy_left"] += p.disp_persist
                else:
                    x["h"] = max(0.0, x["h"] - p.disp_to_civ * p.harm_c)
        elif ev == "blocked_feasibility":
            blocked["feasibility"] += 1
        if x["proxy_left"] > 0:      # displaced conflict is a STATE:
            x["proxy_left"] -= 1     # persists, harms, then decays
            x["h"] = max(0.0, x["h"] - p.disp_to_civ * p.harm_c)
            violence_periods += 1
        if x["war"]:
            violence_periods += 1
            harm_cum += (1 - x["h"]) * p.harm_c
            peak_intensity = max(peak_intensity, x["c"])
            if x["V_G"] < p.hollow_thr:
                war_continues_hollow += 1
    return dict(hit_W=bool(hits), first_hit=hits[0] if hits else np.nan,
                n_onsets=spells, oscillation=int(spells >= 2), exits=exits,
                blocked=blocked, displaced=disp, harm_cum=harm_cum,
                h_final=x["h"], d_final=x["d"], L_final=x["L"],
                V_G_final=x["V_G"], patron=x["patron"],
                hollow_periods=war_continues_hollow,
                patron_exit_t=x["t_patron_exit"], misid=x["misid"],
                preempts=x["preempts"], proxy_states=x["proxy"],
                violence_periods=violence_periods,
                mean_spell=np.mean([e[2] for e in exits]) if exits else np.nan,
                defender_ok=x["d"] >= p.d_min, civilian_ok=x["h"] >= p.h_min)


def mc3(p, n=1500, T=300, seed=1):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame([simulate3(p, rng, T) for _ in range(n)])
    agg = dict(
        p_hit_W=df["hit_W"].mean(), p_oscillation=df["oscillation"].mean(),
        mean_onsets=df["n_onsets"].mean(),
        mean_spell=np.nanmean(df["mean_spell"]),
        mean_first_hit=np.nanmean(df["first_hit"]),
        harm_cum_mean=df["harm_cum"].mean(),
        harm_cum_p90=df["harm_cum"].quantile(0.9),
        h_final_mean=df["h_final"].mean(), L_final_mean=df["L_final"].mean(),
        V_G_final_mean=df["V_G_final"].mean(),
        patron_retained=df["patron"].mean(),
        hollow_periods=df["hollow_periods"].mean(),
        defender_ok=df["defender_ok"].mean(),
        civilian_ok=df["civilian_ok"].mean(),
        displaced_mean=df["displaced"].mean(),
        violence_periods=df["violence_periods"].mean(),
        preempts=df["preempts"].mean(),
        misid_share=df["misid"].mean(),
        p_K_exit=np.mean([any(e[1] == "K_starved" for e in r["exits"])
                          for _, r in df.iterrows()]),
    )
    return agg, df
