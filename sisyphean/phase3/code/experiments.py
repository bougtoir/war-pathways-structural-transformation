"""Phase 3 experiment suite. Seeds fixed; outputs to results/."""
import numpy as np
import pandas as pd
from dataclasses import replace
from model import P3, mc3


def _tag(agg, **kw):
    agg.update(kw)
    return agg


def gate19_consent_rules():
    """V_G collapse under BOTH non-maximizing consent rules, and a control
    where actors do NOT withdraw (L_decay=0) — falsification arm."""
    rows = []
    for rule in ["threshold", "habitual"]:
        for withdraw in [True, False]:
            p = P3(consent_rule=rule,
                   L_decay=0.06 if withdraw else 0.0)
            a, _ = mc3(p, n=800, seed=5)
            rows.append(_tag(a, consent_rule=rule, withdraw=withdraw))
    df = pd.DataFrame(rows)
    df.to_csv("results/g19_consent.csv", index=False)
    return df


def gate20_channels():
    """A alone (V_G collapse only), B alone (sustainment only), both,
    neither — across goal types incl. intrinsic/regime_survival."""
    rows = []
    chan = {
        "neither": dict(collapse_rate=0.0, L_decay=0.0, patron_flow=0.03,
                        tol_patron=99),
        "A_only": dict(patron_flow=0.03, tol_patron=99),   # no sponsor exit
        "B_only": dict(L_decay=0.0),                        # no consent loss
        "both": dict(),
    }
    for g in ["territory", "security", "status", "regime_survival",
              "intrinsic"]:
        for name, mod in chan.items():
            p = replace(P3(), g_type=g, **mod)
            a, _ = mc3(p, n=800, seed=13)
            rows.append(_tag(a, g_type=g, channel=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g20_channels.csv", index=False)
    return df


def gate21_sponsors():
    """Endogenous sponsors: tolerant vs intolerant patron, substitution,
    and the permanent-failure counterexample."""
    rows = []
    for name, mod in {
        "baseline": dict(),
        "intolerant_patron": dict(tol_patron=0.30, patron_flow=0.05),
        "tolerant_patron": dict(tol_patron=2.0, patron_flow=0.05),
        "permanent_failure": dict(tol_patron=99, patron_flow=0.09,
                                  sub_rate=0.05, K0=2.0, S_p0=2.0,
                                  s_release=0.15),
        "balancer_strong": dict(balancer_gain=0.06),
    }.items():
        a, _ = mc3(replace(P3(), **mod), n=800, seed=17)
        rows.append(_tag(a, scenario=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g21_sponsors.csv", index=False)
    return df


def gate22_reachability():
    """Hitting probabilities at multiple horizons + harm + recurrence."""
    rows = []
    for name, mod in {"baseline": dict(), "lever": dict(B=3.0),
                      "combined": dict(B=3.0, kappa=0.09)}.items():
        p = replace(P3(), **mod)
        for T in [60, 150, 300]:
            a, _ = mc3(p, n=1000, T=T, seed=23)
            rows.append(_tag(a, scenario=name, T=T))
    df = pd.DataFrame(rows)
    df.to_csv("results/g22_reach.csv", index=False)
    return df


def gate23_civilian_coupled():
    """Non-inferiority: lever vs baseline vs deprivation-forbidden; also a
    'no asymmetry' arm where defender draws the same pool (coupling test)."""
    rows = []
    for name, mod in {
        "baseline": dict(),
        "lever": dict(kappa=0.09, B=2.0),
        "lever_weak_protect": dict(kappa=0.09, B=2.0, protect=0.2),
        "deprivation_FORBIDDEN": dict(kappa=0.09, B=2.0, harm_c=0.08,
                                      protect=0.0),
    }.items():
        a, df = mc3(replace(P3(), **mod), n=1000, seed=29)
        a["h_p10"] = df["h_final"].quantile(0.1)
        rows.append(_tag(a, scenario=name))
    out = pd.DataFrame(rows)
    out.to_csv("results/g23_civilian.csv", index=False)
    return out


def gate24_rules():
    """Six decision rules incl. intrinsic-aggression and regime-survival."""
    rows = []
    for r in ["eu", "noisy", "aspiration", "bureaucratic", "intrinsic",
              "regime_survival"]:
        for name, mod in {"baseline": dict(),
                          "lever": dict(B=2.0, kappa=0.09)}.items():
            g = ("intrinsic" if r == "intrinsic" else
                 "regime_survival" if r == "regime_survival" else "territory")
            a, _ = mc3(replace(P3(), rule=r, g_type=g, **mod),
                       n=800, seed=31)
            rows.append(_tag(a, rule=r, scenario=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g24_rules.csv", index=False)
    return df


def gate25_dual_use():
    """Opportunity cost vs spillover with endogenous supply response
    (spill raises m_target; o raises it via substitution demand too)."""
    rows = []
    for o in np.linspace(0, 0.8, 9):
        for spill in np.linspace(0, 0.5, 6):
            a, _ = mc3(P3(o=float(o), spill=float(spill)), n=400,
                       T=200, seed=37)
            rows.append(_tag(a, o=float(o), spill=float(spill)))
    df = pd.DataFrame(rows)
    df.to_csv("results/g25_dualuse.csv", index=False)
    return df


def gate26_null_comparison():
    """Matched nulls, same parameter budget:
    n0 ordinary attrition (no consent, no sponsors, flat rho)
    n1 exogenous sanctions (rho *= 0.5 fixed, no endogeneity)
    n2 exogenous payoff step-down (V_G forced to 0.2 at onset)
    n3 bargaining baseline (Phase-2-like: no L, no sponsors)
    n4 sponsor-supported prolonged war (tolerant patron, high flow)
    lever = full endogenous model.
    Matched: same K0, S_p0, kappa, m, rule='eu', T."""
    base = dict(rule="eu", g_type="territory", K0=1.0, S_p0=0.3,
                kappa=0.045)
    rows = []
    specs = {
        "n0_attrition": dict(L_decay=0.0, patron_in=False, patron_flow=0.0,
                             sub_rate=0.0, rho_dom=0.010),
        "n1_exog_sanctions": dict(L_decay=0.0, patron_in=False,
                                  patron_flow=0.0, sub_rate=0.0,
                                  rho_dom=0.005),
        "n3_bargaining": dict(L_decay=0.0, patron_in=False, patron_flow=0.0,
                              sub_rate=0.0, rho_dom=0.010, protect=0.6),
        "n4_sponsor_war": dict(tol_patron=99, patron_flow=0.06),
        "lever_endogenous": dict(),
    }
    for name, mod in specs.items():
        a, _ = mc3(replace(P3(), **{**mod, **base}),
                   n=1000, seed=41)
        rows.append(_tag(a, model=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g26_nulls.csv", index=False)
    return df


def gate26_stepdown():
    """n2: exogenous payoff step-down null — V_G forced to 0.2 at onset
    with NO consent mechanism (L_decay=0). Compared against lever where
    the same V_G path is produced endogenously."""
    a, df = mc3(P3(rule="eu", stepdown=0.2, L_decay=0.0), n=1000, seed=43)
    pd.DataFrame([_tag(a, model="n2_stepdown")]).to_csv(
        "results/g26_stepdown.csv", index=False)
    return a


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    for f in (gate19_consent_rules, gate20_channels, gate21_sponsors,
              gate22_reachability, gate23_civilian_coupled, gate24_rules,
              gate25_dual_use, gate26_null_comparison, gate26_stepdown):
        print(f"\n=== {f.__name__} ===")
        print(f())
