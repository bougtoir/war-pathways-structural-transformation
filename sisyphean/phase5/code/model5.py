"""
Phase 5 — Structural non-appropriability of value.
War is a special case of coercion, not the organizing frame.

Constructs (Gate 2):
  V(theta,t)   value PRODUCED by target j under state theta
  A_i(r,t)     value actor i REALIZES via coercion level r (not asserted
               as fixed scalar: alpha derived from response mechanisms)
  alpha_i      = possession(r) * usability(L) * realization(q) * persistence
  L            consent/cooperation of the target's voluntary actors
  q            institutional legibility of the asset (contracting quality)

Decomposition of appropriable value:
  A = r * [w_phys * 1            # physical assets: capturable
        +  w_hum  * L            # human/relational capital: needs consent
        +  w_inst * L * q        # institutional value: consent+legibility
        +  w_net  * L^2]         # network value: quadratic in consent
  minus coercion cost C(r) = c1*r + c2*r^2 (administration, suppression)
  minus response externalities (sponsor/balancer on the coerced side).

Microfoundation for dA/dr: voluntary actors withdraw cooperation as r
rises (threshold or continuous), so alpha falls where asset weights are
consent-dependent. Sign of dA/dr is emergent: positive for physical
assets, negative for consent-dependent assets. NOT assumed.

Counterexample built-in: w_phys=1, others 0 -> dA/dr > 0 (coercion pays),
matching Liberman-style industrial conquest cases.

Actors: coercer (6 rules as Phase 3-4), target population (consent
rules), sponsor of coercer, balancer of coerced, substitution market.
Civilians harmed only as measured outcome, never as mechanism.
Displacement into repression/proxy is a persistent state (Phase 4).
"""
import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass
class P5:
    # asset mix of the target (weights sum-free)
    w_phys: float = 0.4; w_hum: float = 0.3; w_inst: float = 0.2
    w_net: float = 0.1
    q_legib: float = 0.7          # contracting legibility
    V0: float = 1.0               # produced value scale
    # coercion
    r_max: float = 1.0; c1: float = 0.15; c2: float = 0.25
    # consent response
    consent_rule: str = "threshold"   # threshold|habitual
    L0: float = 1.0; L_floor: float = 0.05; L_decay: float = 0.08
    L_recover: float = 0.02; tau_mean: float = 6.0
    # coercer decision
    rule: str = "eu"; iota: float = 0.0; temp: float = 0.1
    asp_gap: float = 0.55; m_routine: float = 0.75; e_b: float = 0.30
    # sponsors/bypass (Phase-3 style, kept)
    patron_flow: float = 0.03; tol_patron: float = 0.6
    patron_ext: float = 1.0; patron_reenter: float = 0.3
    rho_dom: float = 0.01; sub_rate: float = 0.012
    K0: float = 1.0; S_p0: float = 0.3; s_release: float = 0.05
    kappa: float = 0.045; resist_burn: float = 0.03; K_min: float = 0.05
    # civilians/defense
    harm_c: float = 0.010; protect: float = 0.6
    d0: float = 0.3; d_max: float = 0.85; d_rate: float = 0.10
    h_min: float = 0.5; d_min: float = 0.3; balancer_gain: float = 0.02
    # displacement (persistent state)
    p_disp: float = 0.35; disp_persist: int = 20; disp_to_civ: float = 0.4
    # dynamics
    m_req0: float = 0.35; B: float = 0.0
    a_q: float = 0.10; sig_q: float = 0.12; jump_rate: float = 0.08
    jump_scale: float = 0.35; dur_max: int = 80; T: int = 300
    o: float = 0.3; spill: float = 0.0


def alpha(x, p):
    """Appropriability multiplier — derived, not asserted."""
    L, q = x["L"], p.q_legib
    return (p.w_phys + p.w_hum * L + p.w_inst * L * q
            + p.w_net * L * L)


def produced_value(x, p):
    """Value production depends on consent too: coercion suppresses
    creation, not only capture."""
    return p.V0 * (0.3 + 0.7 * x["L"])


def payoff(x, p):
    """Net coercive payoff rate: appropriated flow minus coercion cost
    minus coercion-side sustainment burn."""
    A = x["r"] * alpha(x, p) * produced_value(x, p)
    C = p.c1 * x["r"] + p.c2 * x["r"] ** 2
    return A, C, A - C


def consent_step(x, p):
    if x["coercion"]:
        if p.consent_rule == "habitual":
            x["L"] += p.L_decay * (p.L_floor - x["L"])
        else:
            x["obs_harm"] += x["r"] * x["h_weight"]
            if x["obs_harm"] > x["tau_i"]:
                x["L"] += p.L_decay * (p.L_floor - x["L"])
    else:
        x["obs_harm"] = max(0.0, x["obs_harm"] - 0.5)
        x["L"] = min(1.0, x["L"] + p.L_recover * (1 - x["L"]))
    x["L"] = float(np.clip(x["L"], 0, 1))


def fires(x, p, rng):
    """Coercer's decision rule — may be non-maximizing."""
    x_p = dict(x, r=p.r_max)           # prospective payoff at r_max
    A, C, net = payoff(x_p, p)
    UW = net + p.iota - 0.2
    UA = 0.1 * produced_value(x, p) * (1 - x["r"])  # peaceful alt payoff
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
    if r == "intrinsic":
        return rng.random() < 0.6
    if r == "regime_survival":
        return x["q"] > 0.25 or x["coercion"]
    raise ValueError(r)


def simulate5(p, rng):
    x = dict(q=0.3, m=0.5, L=p.L0, h=1.0, d=p.d0, K=p.K0, S_p=p.S_p0,
             r=0.0, coercion=False, t_c=0, obs_harm=0.0,
             tau_i=p.tau_mean + 2 * rng.random(),
             patron=True, e_streak=0, h_weight=1.0,
             proxy=0, proxy_left=0)
    hits, exits, disp = [], [], 0
    harm_cum = 0.0
    hollow = 0
    captured_cum = 0.0
    for t in range(p.T):
        dq = -p.a_q * x["q"] + p.sig_q * rng.standard_normal()
        if rng.random() < p.jump_rate:
            dq += abs(rng.standard_normal() * p.jump_scale)
        x["q"] = float(np.clip(x["q"] + dq, 0, 1))
        x["m"] += 0.05 * (min(1.0, 0.6 + p.spill - 0.4 * p.o) - x["m"])

        consent_step(x, p)
        # sponsor externality on coercion intensity
        e = x["r"] * p.patron_ext if x["coercion"] else 0.0
        if x["patron"]:
            x["e_streak"] = x["e_streak"] + 1 if e > p.tol_patron else 0
            if x["e_streak"] > 0:
                x["patron"] = False
        else:
            if not x["coercion"] or e < p.patron_reenter:
                x["patron"] = True
                x["e_streak"] = 0
        rho = max(0.0, p.rho_dom + (p.patron_flow if x["patron"] else p.sub_rate))

        if not x["coercion"]:
            if fires(x, p, rng):
                feas = x["m"] >= p.m_req0 + 0.1 * x["L"]
                if feas and rng.random() < np.exp(-p.B):
                    x["coercion"] = True
                    x["r"] = p.r_max
                    hits.append(t)
                elif rng.random() < p.p_disp:
                    disp += 1
                    x["proxy"] += 1
                    x["proxy_left"] += p.disp_persist
            continue

        # coercive episode
        x["t_c"] += 1
        A, C, net = payoff(x, p)
        captured_cum += A
        burn = p.kappa * x["r"] * x["m"] + p.resist_burn * x["d"]
        rel = min(p.s_release, x["S_p"])
        x["S_p"] -= rel
        x["K"] += -burn + rho + rel
        x["d"] += p.d_rate * (p.d_max - x["d"]) * (x["h"] > 0.6 * p.h_min) \
            + p.balancer_gain * x["r"] * (1 - x["d"])
        x["d"] = float(np.clip(x["d"], 0, 1))
        x["h"] = max(0.0, x["h"] - p.harm_c * x["r"] * (1 - p.protect))
        harm_cum += (1 - x["h"]) * p.harm_c
        if A < 0.2 * p.V0:
            hollow += 1
        if x["K"] <= p.K_min or x["t_c"] >= p.dur_max or net < -0.3:
            exits.append((t, "K" if x["K"] <= p.K_min else
                          ("dur" if x["t_c"] >= p.dur_max else "unprofitable"),
                          x["t_c"]))
            x["coercion"] = False
            x["r"] = 0.0
        if x["proxy_left"] > 0:
            x["proxy_left"] -= 1
            x["h"] = max(0.0, x["h"] - p.disp_to_civ * p.harm_c)
    return dict(hit=bool(hits), first_hit=hits[0] if hits else np.nan,
                n_onsets=len(hits), exits=exits, disp=disp,
                proxy_states=x["proxy"], harm_cum=harm_cum,
                h_final=x["h"], L_final=x["L"], d_final=x["d"],
                hollow=hollow, captured=captured_cum,
                mean_spell=np.mean([e[2] for e in exits]) if exits
                else np.nan,
                civilian_ok=x["h"] >= p.h_min,
                defender_ok=x["d"] >= p.d_min)


def mc5(p, n=800, seed=1):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame([simulate5(p, rng) for _ in range(n)])
    agg = dict(p_hit=df["hit"].mean(), mean_onsets=df["n_onsets"].mean(),
               mean_spell=np.nanmean(df["mean_spell"]),
               harm=df["harm_cum"].mean(), h_final=df["h_final"].mean(),
               L_final=df["L_final"].mean(), hollow=df["hollow"].mean(),
               captured=df["captured"].mean(),
               disp=df["disp"].mean(), proxy=df["proxy_states"].mean(),
               civilian_ok=df["civilian_ok"].mean(),
               defender_ok=df["defender_ok"].mean(),
               p_unprofitable=np.mean([
                   any(e[1] == "unprofitable" for e in r["exits"])
                   for _, r in df.iterrows()]),
               p_K_exit=np.mean([
                   any(e[1] == "K" for e in r["exits"])
                   for _, r in df.iterrows()]))
    return agg, df
