"""
Minimal formal model: stage-decoupled war pathway with actor-specific utilities.

Stages (analytical, not chronological):
  1. Conflict formation       -> issue G drawn from a range of stakes
  2. Bargaining failure       -> bargaining surplus existence + info/commitment failure prob.
  3. Selection of force       -> leader-level decision (U_leader(W) > U_leader(A))
  4. Military mobilization    -> feasibility constraint M(theta) >= M_req
  5. Escalation               -> nonlinear escalation propensity vs threshold
  6. System adaptation        -> (handled in evolutionary/network modules)

War = conjunctive event: willing AND feasible AND escalates.
Interventions act on separate factors, so effects are multiplicative.

All results are ILLUSTRATIVE (arbitrary parameterization, no calibration).
"""
import numpy as np
import pandas as pd

RNG = np.random.default_rng(20261014)


# ---------------------------------------------------------------------------
# Structural parameter vector theta
# ---------------------------------------------------------------------------
BASELINE = dict(
    a=0.30,      # quality of nonviolent alternatives (0..1)
    o=0.30,      # civilian opportunity cost of mobilization (0..1)
    delta=0.60,  # state-regime incentive divergence (0..1)
    k=0.60,      # escalation amplification / feedback gain (0..1)
    m=0.70,      # baseline mobilization capacity / fiscal-military efficiency
    div=0.40,    # diversionary benefit of external conflict to leader/regime
    lam=0.60,    # punishment sensitivity: leader's exposure to removal after loss
    sigma=0.25,  # misperception / bounded rationality (std of belief noise)
    rho=0.30,    # commitment-problem severity (prob. bargaining fails exogenously)
    alpha=0.50,  # settlement implementation efficiency (bargained deals deliver alpha*p*G)
)

SCENARIOS = {
    "baseline":   dict(),
    "A_alternatives":  dict(a=0.65),   # improved nonviolent alternatives
    "B_opportunity":   dict(o=0.60),   # higher civilian opportunity cost
    "C_alignment":     dict(delta=0.20),  # reduced state-regime divergence
    "D_deescalation":  dict(k=0.25),   # reduced escalation amplification
    "E_combined":      dict(a=0.65, o=0.60, delta=0.20, k=0.25),
}


def actor_utilities(G, p, theta, eps=None):
    """
    Return dict of actor utilities for war (U_W) and best alternative (U_A).

    G in [0,1]: value of the political objective.
    p in [0,1]: expected probability of military victory.
    eps: belief noise (bounded rationality / misperception), applied to p.
    """
    a, o, delta = theta["a"], theta["o"], theta["delta"]
    div, lam = theta["div"], theta["lam"]
    sigma = theta["sigma"]
    p_hat = np.clip(p + (0.0 if eps is None else sigma * eps), 0.0, 1.0)

    # Material (state) payoffs
    c_state = 0.35 + 0.30 * o          # fiscal/material war cost, rising in o
    UW_state = p_hat * G - c_state
    UA_state = theta["alpha"] * p * G - 0.05 + 0.25 * a  # bargained settlement is imperfectly implemented

    # Regime survival: war outcome shifts regime survival probability
    d_survive = div * delta - lam * (1 - p_hat) * delta
    UW_regime = UW_state + d_survive * G
    UA_regime = UA_state + 0.10 * delta * (a - 0.3)  # weak institutions make peace costlier to regime

    # Leader: sharper version of regime (leader bears removal risk personally)
    d_leader = 1.4 * div * delta - 1.6 * lam * (1 - p_hat) * delta
    UW_leader = UW_state + d_leader * G
    UA_leader = UA_state + 0.10 * delta * (a - 0.3)

    # Population: bears most costs, gets small share of G
    UW_pop = p_hat * 0.3 * G - (0.55 + 0.25 * o)
    UA_pop = p * 0.3 * G + 0.30 * a

    return {
        "UW_state": UW_state, "UA_state": UA_state,
        "UW_regime": UW_regime, "UA_regime": UA_regime,
        "UW_leader": UW_leader, "UA_leader": UA_leader,
        "UW_pop": UW_pop, "UA_pop": UA_pop,
    }


def mobilization_feasible(theta, G):
    """M(theta) >= M_req. Opportunity cost o reduces net capacity."""
    m, o = theta["m"], theta["o"]
    capacity = m * (1.0 - 0.7 * o) + 0.15 * theta["a"]  # dual-use/civilian conversion slack
    M_req = 0.30 + 0.20 * G                            # bigger objectives need more mobilization
    return capacity >= M_req, capacity - M_req


def escalates(theta, n_trials=1):
    """Nonlinear escalation: prob = k^2 / (k^2 + (1-k)^2) shaped response."""
    k = theta["k"]
    p_esc = (k ** 2) / (k ** 2 + (1.0 - k) ** 2)
    return RNG.random(n_trials) < p_esc, p_esc


def war_pathway_probability(theta, n=20000):
    """
    Monte-Carlo estimate of P(war pathway completes) over draws of G, p,
    belief noise, and exogenous bargaining failure.
    War requires: bargaining fails AND leader chooses force AND
    mobilization feasible AND escalation occurs.
    Also returns stage-conditional rates and actor-specific region sizes.
    """
    G = RNG.random(n)
    p = np.clip(0.25 + 0.5 * RNG.random(n), 0.05, 0.95)
    eps = RNG.standard_normal(n)

    rho = theta["rho"]
    bargain_fail = RNG.random(n) < rho

    u = actor_utilities(G, p, theta, eps)
    u_obj = actor_utilities(G, p, theta, eps=np.zeros(n))  # noiseless utilities
    leader_wants = u["UW_leader"] > u["UA_leader"]
    leader_wants_obj = u_obj["UW_leader"] > u_obj["UA_leader"]
    state_wants = u["UW_state"] > u["UA_state"]
    pop_wants = u["UW_pop"] > u["UA_pop"]

    feas = np.array([mobilization_feasible(theta, g)[0] for g in G])
    esc_flag, p_esc = escalates(theta, n)

    war = bargain_fail & leader_wants & feas & esc_flag
    out = {
        "p_war": war.mean(),
        "p_bargain_fail": bargain_fail.mean(),
        "p_leader_wants": leader_wants.mean(),
        "p_state_wants": state_wants.mean(),
        "p_pop_wants": pop_wants.mean(),
        "p_feasible": feas.mean(),
        "p_escalate": p_esc,
        # conditional pathway: among cases where leader wants war
        "p_war_given_willing": war[leader_wants].mean() if leader_wants.any() else 0.0,
        # mobilization feasibility restricted to cases where leader wants war
        "p_feasible_given_willing": feas[leader_wants].mean() if leader_wants.any() else 0.0,
        # wars the state "shouldn't" want but leader does (agency gap)
        "p_agency_gap": (leader_wants & ~state_wants).mean(),
        # wars whose leader selection flips on belief noise (misperception-driven):
        # completes pathway, but noiseless leader utility would reject force
        "p_war_misperceived": (war & ~leader_wants_obj).mean(),
        # reverse: pathway blocked only because misperception suppressed choice
        "p_blocked_by_misperception": (bargain_fail & ~leader_wants
                                       & leader_wants_obj & feas & esc_flag).mean(),
    }
    return out


def region_sizes(theta, G_grid=None, p_grid=None):
    """Measure |R_actor|: share of the (G, p) unit square where U_W^a > U_A^a.
    Region size is an area over stakes x expected victory probability, so the
    measure is dimensionless and bounded in [0,1] (no noise -> 'objective'
    subjective-utility region; beliefs enter via sigma elsewhere)."""
    if G_grid is None:
        G_grid = np.linspace(0, 1, 121)
    if p_grid is None:
        p_grid = np.linspace(0, 1, 121)
    G, P = np.meshgrid(G_grid, p_grid)
    u = actor_utilities(G.ravel(), P.ravel(), theta)
    return {a: float(np.mean(u[f"UW_{a}"] > u[f"UA_{a}"]))
            for a in ("state", "regime", "leader", "pop")}


def run():
    rows = []
    for name, mod in SCENARIOS.items():
        theta = dict(BASELINE, **mod)
        res = war_pathway_probability(theta)
        res.update(region_sizes(theta))
        res["scenario"] = name
        res.update({f"theta_{k}": v for k, v in theta.items()})
        rows.append(res)
    df = pd.DataFrame(rows).set_index("scenario")
    df.to_csv("results/scenarios.csv")
    return df


def sensitivity(n=3000):
    """One-at-a-time sensitivity of p_war to each theta parameter."""
    base = dict(BASELINE)
    rows = []
    for key in BASELINE:
        for val in np.linspace(0.05, 0.95, 11):
            theta = dict(base); theta[key] = float(val)
            r = war_pathway_probability(theta, n=n)
            rows.append({"param": key, "value": val, "p_war": r["p_war"],
                         "p_agency_gap": r["p_agency_gap"]})
    df = pd.DataFrame(rows)
    df.to_csv("results/sensitivity.csv", index=False)
    return df


def region_overlap(theta=None):
    """Joint region overlap over the (G, p) square."""
    theta = dict(BASELINE) if theta is None else theta
    G, P = np.meshgrid(np.linspace(0, 1, 121), np.linspace(0, 1, 121))
    u = actor_utilities(G.ravel(), P.ravel(), theta)
    L = u["UW_leader"] > u["UA_leader"]
    S = u["UW_state"] > u["UA_state"]
    R = u["UW_regime"] > u["UA_regime"]
    P_ = u["UW_pop"] > u["UA_pop"]
    out = {
        "all_four": float(np.mean(L & S & R & P_)),
        "leader_only": float(np.mean(L & ~S & ~R & ~P_)),
        "leader_not_state": float(np.mean(L & ~S)),
        "state_not_leader": float(np.mean(S & ~L)),
        "none": float(np.mean(~L & ~S & ~R & ~P_)),
    }
    pd.DataFrame([out]).to_csv("results/region_overlap.csv", index=False)
    return out


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    df = run()
    print(df[["p_war", "p_leader_wants", "p_feasible", "p_escalate",
              "p_agency_gap", "state", "leader", "pop"]].round(3))
    print("\nRegion overlap:", {k: round(v, 3) for k, v in region_overlap().items()})
    sensitivity()
    print("wrote results/scenarios.csv, results/sensitivity.csv, results/region_overlap.csv")
