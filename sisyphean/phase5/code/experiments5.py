"""Phase 5 experiment suite — gates 2,3,5,8."""
import numpy as np
import pandas as pd
from dataclasses import replace
from model5 import P5, mc5, alpha


def _tag(a, **kw):
    a.update(kw)
    return a


def gate23_theorem_sweep():
    """Appropriability sign by asset mix — theorem + counterexample."""
    rows = []
    mixes = {
        "physical_only": dict(w_phys=1.0, w_hum=0, w_inst=0, w_net=0),
        "human_only": dict(w_phys=0.0, w_hum=1.0, w_inst=0, w_net=0),
        "institutional": dict(w_phys=0.2, w_hum=0.2, w_inst=0.4, w_net=0.2),
        "mixed_realistic": dict(),   # defaults
        "network_heavy": dict(w_phys=0.1, w_hum=0.2, w_inst=0.2, w_net=0.5),
    }
    for name, w in mixes.items():
        a, _ = mc5(replace(P5(), **w), n=600, seed=5)
        rows.append(_tag(a, mix=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g23_mix.csv", index=False)
    return df


def gate5_rivals():
    """Fair-complexity rivals: same channels available, different
    mechanisms turned on/off."""
    rows = []
    specs = {
        "appropriability_lever": dict(),
        "cost_only": dict(L_decay=0.0, c2=0.6),  # generic cost increase
        "sanctions_exog": dict(L_decay=0.0, patron_flow=0.0,
                              sub_rate=0.0, rho_dom=0.005),
        "attrition_no_consent": dict(L_decay=0.0),
        "war_economy": dict(w_phys=0.9, w_hum=0.1, w_inst=0, w_net=0,
                            tol_patron=99, patron_flow=0.06),
        "displacement_persistent": dict(disp_persist=60),
    }
    for name, mod in specs.items():
        a, _ = mc5(replace(P5(), **mod), n=600, seed=11)
        rows.append(_tag(a, model=name))
    df = pd.DataFrame(rows)
    df.to_csv("results/g5_rivals.csv", index=False)
    return df


def gate8_rules():
    """6 coercer rules; appropriability vs harm by rule."""
    rows = []
    for r in ["eu", "noisy", "aspiration", "bureaucratic", "intrinsic",
              "regime_survival"]:
        a, _ = mc5(P5(rule=r), n=500, seed=13)
        rows.append(_tag(a, rule=r))
    df = pd.DataFrame(rows)
    df.to_csv("results/g8_rules.csv", index=False)
    return df


def gate8_failure_regions():
    """Parameter regions of success AND failure."""
    rows = []
    for w_phys in [0.0, 0.4, 0.8, 1.0]:
        for tol in [0.3, 0.6, 2.0]:
            p = replace(P5(), w_phys=w_phys,
                        w_hum=(1 - w_phys) * 0.5,
                        w_inst=(1 - w_phys) * 0.3,
                        w_net=(1 - w_phys) * 0.2, tol_patron=tol)
            a, _ = mc5(p, n=400, seed=17)
            rows.append(_tag(a, w_phys=w_phys, tol=tol))
    df = pd.DataFrame(rows)
    df.to_csv("results/g8_regions.csv", index=False)
    return df


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    for f in (gate23_theorem_sweep, gate5_rivals, gate8_rules,
              gate8_failure_regions):
        print("\n===", f.__name__, "===")
        print(f())
