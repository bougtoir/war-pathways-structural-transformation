"""Phase 4 experiment suite — gates 29–38. Seeds fixed."""
import numpy as np
import pandas as pd
from dataclasses import replace
from model import P3, mc3, simulate3


def _tag(a, **kw):
    a.update(kw)
    return a


def gate29_audit():
    """Reproduce pivotal Phase-3 cases + hollow-threshold sensitivity +
    corrected bound-clock audit."""
    rows = []
    # pivot reproduction
    for name, mod in {
        "pivA_channelA": dict(patron_flow=0.03, tol_patron=99),
        "pivB_channelB": dict(L_decay=0.0),
        "piv_tolerant_fail": dict(tol_patron=99, patron_flow=0.09,
                                  K0=2.0, S_p0=2.0, s_release=0.15),
        "piv_civilian": dict(kappa=0.09, B=2.0),
    }.items():
        a, _ = mc3(replace(P3(), **mod), n=600, seed=3)
        rows.append(_tag(a, audit=name))
    # hollow-threshold sensitivity
    for thr in [0.1, 0.2, 0.3, 0.4]:
        a, _ = mc3(P3(hollow_thr=thr), n=600, seed=9)
        rows.append(_tag(a, audit=f"hollow_thr_{thr}"))
    df = pd.DataFrame(rows)
    df.to_csv("results/g29_audit.csv", index=False)

    # corrected bound clock: exit_delay shifts post-trigger clock
    bound_rows = []
    for delay in [0, 10, 30]:
        for kappa in [0.045, 0.09]:
            p = P3(exit_delay=delay, kappa=kappa, sponsor_flow=None) \
                if False else P3(exit_delay=delay, kappa=kappa)
            a, df2 = mc3(p, n=400, seed=11)
            bound_rows.append(_tag(a, exit_delay=delay, kappa=kappa))
    bd = pd.DataFrame(bound_rows)
    bd.to_csv("results/g29_boundclock.csv", index=False)
    return df, bd


def gate30_richer_nulls():
    """Nulls that INCLUDE endogenous legitimacy collapse / sponsor
    withdrawal — does the hollow signature still discriminate?"""
    rows = []
    specs = {
        # null with consent collapse but NO sponsor channel
        "n_legit_no_sponsor": dict(patron_in=False, patron_flow=0.0,
                                   sub_rate=0.0, rho_dom=0.010),
        # null with sponsor exit but NO consent channel
        "n_sponsor_no_legit": dict(L_decay=0.0),
        # null with BOTH (fair-complexity rival)
        "n_full_rival": dict(),
        # exogenous sanctions + consent collapse
        "n_sanc+legit": dict(L_decay=0.0, patron_in=False, patron_flow=0.0,
                             sub_rate=0.0, rho_dom=0.005),
        "lever": dict(),
    }
    for name, mod in specs.items():
        a, _ = mc3(replace(P3(), **mod), n=800, seed=15)
        rows.append(_tag(a, model=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g30_richernulls.csv", index=False)
    return df


def gate31_outcomes_misid_preempt():
    """Four-outcome accounting + mis-ID + preemption counterexample."""
    rows = []
    for name, mod in {
        "baseline": dict(),
        "lever": dict(B=2.0, kappa=0.09),
        "lever+misid10": dict(B=2.0, kappa=0.09, p_misid=0.10),
        "lever+preempt": dict(B=3.0, kappa=0.09, p_preempt=0.30),
        "highB_only": dict(B=3.0),
    }.items():
        a, _ = mc3(replace(P3(), **mod), n=1000, seed=19)
        rows.append(_tag(a, scenario=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g31_outcomes.csv", index=False)
    return df


def gate32_sufficiency():
    """Sufficient conditions with exit delays, stochastic rho, reserves."""
    rows = []
    for delay in [0, 20, 40]:
        for rho_sig in [0.0, 0.010, 0.025]:
            for S_p0 in [0.3, 1.5]:
                p = P3(exit_delay=delay, rho_sig=rho_sig, S_p0=S_p0,
                       kappa=0.09)
                a, df = mc3(p, n=600, seed=23)
                rows.append(_tag(a, delay=delay, rho_sig=rho_sig,
                                 S_p0=S_p0))
    df = pd.DataFrame(rows)
    df.to_csv("results/g32_sufficiency.csv", index=False)
    return df


def gate33_recurrence_states():
    """Displacement as persistent conflict states; total violence metric."""
    rows = []
    for name, mod in {
        "baseline": dict(),
        "lever_disp0": dict(B=3.0, kappa=0.09),
        "lever_disp_persist": dict(B=3.0, kappa=0.09, disp_persist=20),
        "lever_disp_long": dict(B=3.0, kappa=0.09, disp_persist=60),
    }.items():
        a, df = mc3(replace(P3(), **mod), n=800, seed=27)
        a["total_harm"] = df["harm_cum"].mean()
        a["h_p10"] = df["h_final"].quantile(0.1)
        rows.append(_tag(a, scenario=name))
    out = pd.DataFrame(rows)
    out.to_csv("results/g33_recurrence.csv", index=False)
    return out


def gate34_rules_robustness():
    """6 leader rules × lever; ideologically committed (intrinsic) and
    regime-survival stress arms."""
    rows = []
    for r in ["eu", "noisy", "aspiration", "bureaucratic", "intrinsic",
              "regime_survival"]:
        g = ("intrinsic" if r == "intrinsic" else
             "regime_survival" if r == "regime_survival" else "territory")
        for name, mod in {"base": dict(), "lever": dict(B=2.0,
                                                        kappa=0.09)}.items():
            a, _ = mc3(replace(P3(), rule=r, g_type=g, **mod),
                       n=600, seed=33)
            rows.append(_tag(a, rule=r, scenario=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g34_rules.csv", index=False)
    return df


def gate35_conversion():
    """EXPLORATORY: conversion of military capacity to civilian uses.
    Transition cost c_conv, utilization u, benefit per converted unit.
    Net social value = benefit - cost; grid over parameters."""
    rows = []
    for cost in [0.1, 0.3, 0.5, 0.8]:
        for util in [0.2, 0.5, 0.8]:
            for spill_m in [-0.1, 0.0, 0.2]:  # negative = capacity loss
                benefit = 1.2 * util - cost + spill_m * 0  # benefit model
                rows.append(dict(c_conv=cost, util=util,
                                 spill_to_mil=spill_m,
                                 net_social=round(benefit, 3),
                                 feasible=(cost < 0.8 and util > 0.3)))
    df = pd.DataFrame(rows)
    df.to_csv("results/g35_conversion.csv", index=False)
    return df


def gate36_cost_model():
    """EXPLORATORY symbolic cost-benefit sketch.
    Illustrative anchors only; 1000T JPY used as sensitivity anchor."""
    I_anchor = 1000.0  # trillion JPY, illustrative
    rows = []
    for disc in [0.01, 0.03, 0.05]:
        for T in [50, 100]:
            for avoided in [0.5, 2.0, 8.0]:   # T JPY/yr avoided harm
                npv = sum(avoided / (1 + disc) ** t for t in range(1, T + 1))
                maint = 0.02 * I_anchor
                rows.append(dict(disc=disc, T=T,
                                 avoided_TJPY_per_yr=avoided,
                                 NPV_TJPY=round(npv, 1),
                                 I_anchor=I_anchor,
                                 net=round(npv - I_anchor - maint, 1)))
    df = pd.DataFrame(rows)
    df.to_csv("results/g36_cost.csv", index=False)
    return df


def gate37_shared_futures():
    """EXPLORATORY: V in {-0.5,0,0.5,1.0} shifts barrier B and maintenance
    cost multiplicatively (sign not stipulated)."""
    rows = []
    for V in [-0.5, 0.0, 0.5, 1.0]:
        B_eff = max(0.0, 2.0 + 0.8 * V)
        a, _ = mc3(P3(B=B_eff, kappa=0.09), n=500, seed=39)
        rows.append(_tag(a, V=V, B_eff=B_eff))
    df = pd.DataFrame(rows)
    df.to_csv("results/g37_sharedfutures.csv", index=False)
    return df


def gate38_scenario_grid():
    """Machine-readable robust/fragile grid."""
    rows = []
    for tol in [0.3, 0.6, 2.0]:
        for sub in [0.0, 0.02, 0.05]:
            for kappa in [0.045, 0.09]:
                for V in [0.0, 1.0]:
                    p = P3(tol_patron=tol, sub_rate=sub, kappa=kappa,
                           B=max(0.0, 2.0 + 0.8 * V))
                    a, _ = mc3(p, n=400, seed=43)
                    robust = a["p_K_exit"] > 0.9 and a["civilian_ok"] > 0.9
                    rows.append(_tag(a, tol=tol, sub=sub, kappa=kappa,
                                     V=V, robust=robust))
    df = pd.DataFrame(rows)
    df.to_csv("results/g38_grid.csv", index=False)
    return df


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    fs = [gate29_audit, gate30_richer_nulls, gate31_outcomes_misid_preempt,
          gate32_sufficiency, gate33_recurrence_states,
          gate34_rules_robustness, gate35_conversion, gate36_cost_model,
          gate37_shared_futures, gate38_scenario_grid]
    for f in fs:
        print("\n===", f.__name__, "===")
        out = f()
        if isinstance(out, tuple):
            for o in out:
                print(o.round(3) if hasattr(o, "round") else o)
        else:
            print(out.round(3) if hasattr(out, "round") else out)
