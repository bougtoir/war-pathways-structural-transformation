"""Phase 6 computational checks (Gate 8).

Validates repaired propositions numerically — labeled COMPUTATIONAL
VERIFICATION of analytic claims, never 'simulation proves theorem'.
"""
import numpy as np
import pandas as pd
from dataclasses import replace
from model6 import (P6, pi, dpi_dr_fixed_L, dpi_dr_total, L_inf, pi_inf,
                    level_condition, alpha_of, V_of_L)


def check_derivative_objects():
    """Show the four objects differ; reproduce the T-1 conflation."""
    p = P6()
    rows = []
    for r in [0.0, 0.5, 1.0]:
        L = L_inf(r, p)
        rows.append(dict(
            r=r,
            dpi_dr_fixed_L=dpi_dr_fixed_L(r, L, p),
            dpi_dr_total=dpi_dr_total(r, p),
            pi_level=pi(r, L, p)))
    df = pd.DataFrame(rows)
    df.to_csv("results/c1_objects.csv", index=False)
    return df


def check_T1_counterexample():
    """Construct parameters satisfying old T-1's premises (large consent
    response, dominant consent weights) but pi_inf > 0 — the old claim
    'negative derivative => negative level' fails."""
    base = replace(P6(), w_phys=0.05, w_hum=0.5, w_inst=0.3, w_net=0.15,
                   c1=0.01, c2=0.01, coll_action=3.0, exit_cost=0.5)
    rows = []
    for r in [0.5, 1.0]:
        lhs, rhs, neg = level_condition(r, base)
        rows.append(dict(r=r, L_inf=L_inf(r, base),
                         dpi_dr_total=dpi_dr_total(r, base),
                         alphaV=lhs, cost=rhs, pi_inf=pi_inf(r, base),
                         level_negative=neg))
    df = pd.DataFrame(rows)
    df.to_csv("results/c2_t1_counterexample.csv", index=False)
    return df


def check_level_theorem():
    """T-1R (repaired): if alpha(L_inf)*V(L_inf) < c1 + c2*r, pi_inf<0.
    Verify equivalence numerically across a grid; also verify sign flips
    at the asset-mix boundary."""
    rows = []
    for w_phys in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        rem = 1 - w_phys
        p = replace(P6(), w_phys=w_phys, w_hum=0.5 * rem,
                    w_inst=0.3 * rem, w_net=0.2 * rem)
        for spec in ["opt", "rule"]:
            lhs, rhs, neg = level_condition(1.0, p, spec)
            rows.append(dict(w_phys=w_phys, spec=spec,
                             L_inf=L_inf(1.0, p, spec),
                             alphaV=lhs, c1c2r=rhs,
                             pi_inf=pi_inf(1.0, p, spec),
                             level_negative=neg))
    df = pd.DataFrame(rows)
    df.to_csv("results/c3_level_grid.csv", index=False)
    return df


def check_behavior_specs():
    """Gate 2: optimizing vs rule-based; fear_gain > coll_action/exit_cost
    flips dL*/dr sign — coercion increasing compliance is the emergent
    possibility the prompt demands we keep."""
    rows = []
    for spec in ["opt", "rule"]:
        for fg, ca, ec in [(0.0, 0.5, 0.2), (0.0, 3.0, 0.2),
                           (1.5, 0.5, 0.2), (3.0, 0.5, 0.2)]:
            p = replace(P6(), fear_gain=fg, coll_action=ca, exit_cost=ec)
            Ls = np.array([L_inf(r, p, spec) for r in np.linspace(0, 1, 11)])
            rows.append(dict(spec=spec, fear=fg, coll=ca, exit_cost=ec,
                             dL_dr_at_05=float(np.polyfit(
                                 np.linspace(0, 1, 11), Ls, 1)[0]),
                             L_at_0=Ls[0], L_at_1=Ls[-1]))
    df = pd.DataFrame(rows)
    df.to_csv("results/c4_behavior.csv", index=False)
    return df


def check_boundary_cases():
    """r=0 must give pi=0 (not negative); boundary w_phys regimes."""
    p = P6()
    rows = [dict(r=0.0, pi=pi(0.0, 1.0, p), note="pi(0,L)=0 identically"),
            dict(r=0.0, pi=pi(0.0, 0.0, p), note="same at L=0")]
    df = pd.DataFrame(rows)
    df.to_csv("results/c5_boundaries.csv", index=False)
    return df


def check_asset_regimes():
    """Gate 3: two stable regimes — high appropriability (physical-heavy)
    and low appropriability (consent-heavy) both sustained."""
    rows = []
    for name, w in [("physical_regime", dict(w_phys=1.0, w_hum=0.0,
                                           w_inst=0.0, w_net=0.0)),
                    ("consent_regime", dict(w_phys=0.05, w_hum=0.45,
                                            w_inst=0.30, w_net=0.20))]:
        p = replace(P6(), **w)
        for spec in ["opt", "rule"]:
            lhs, rhs, neg = level_condition(1.0, p, spec)
            rows.append(dict(regime=name, spec=spec,
                             pi_inf=round(pi_inf(1.0, p, spec), 4),
                             profitable=not neg))
    df = pd.DataFrame(rows)
    df.to_csv("results/c6_regimes.csv", index=False)
    return df


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    for f in (check_derivative_objects, check_T1_counterexample,
              check_level_theorem, check_behavior_specs,
              check_boundary_cases, check_asset_regimes):
        print("\n===", f.__name__, "===")
        print(f().to_string())
