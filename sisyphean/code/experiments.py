"""Experiment suite for the Sisyphean Lever model. All runs seeded."""
import numpy as np
import pandas as pd
from dataclasses import replace
from model import P, mc


def gate11_reachability():
    """P(hit W in T) under baseline / barrier / combined; shock sensitivity."""
    rows = []
    scenarios = {
        "baseline":      P(),
        "barrier":       P(B=3.0),
        "keystone_burn": P(kappa=0.09, sponsor=0.004),
        "combined":      P(B=3.0, kappa=0.09, sponsor=0.004),
        # adversarial counterexample: rich sponsors + big stockpile
        "sponsor_rich":  P(B=3.0, kappa=0.09, sponsor=0.030, S_p0=1.5,
                           s_release=0.12),
    }
    for name, p in scenarios.items():
        for dist in ["normal", "cauchy"]:
            pp = replace(p, shock_dist=dist)
            agg, _ = mc(pp, n=1500, seed=42)
            agg.update(scenario=name, shock_dist=dist)
            rows.append(agg)
    df = pd.DataFrame(rows)
    df.to_csv("results/gate11_reachability.csv", index=False)
    return df


def gate12_keystone_exit_bound():
    """Numerical verification of the bounded-exit bound.
    Bound: t_exit <= (K0-K_min+S_p0)/(kappa*c_min*m_min - rho_bar)."""
    from model import K_MIN, C_W
    rows = []
    for kappa in [0.03, 0.045, 0.06, 0.09]:
        for sponsor in [0.0, 0.004, 0.010, 0.020, 0.030]:
            p = P(kappa=kappa, sponsor=sponsor, B=0.0, jump_rate=0.5)
            # force early onset deterministically: no barrier, high m
            p = replace(p, m_routine=0.0, rule="bureaucratic", e_b=0.0)
            rng = np.random.default_rng(0)
            from model import simulate
            r = simulate(p, rng, T=300)
            burn = kappa * C_W * 0.5 - 0  # approx: c>=C_W, m~0.5
            bound = ((p.K0 - K_MIN + p.S_p0) / max(burn - sponsor, 1e-6))
            rows.append(dict(kappa=kappa, sponsor=sponsor,
                             exits_by_K=any(e[1] == "K_starved"
                                            for e in r["exits"]),
                             first_exit_t=(r["exits"][0][0]
                                           if r["exits"] else np.nan),
                             bound=bound))
    df = pd.DataFrame(rows)
    df.to_csv("results/gate12_bound.csv", index=False)
    return df


def gate13_relapse():
    """Relapse/oscillation under the lever vs under pure suppression."""
    rows = []
    for name, p in {
        "baseline": P(),
        "lever": P(kappa=0.09, sponsor=0.004),
        "lever_lowregrow": P(kappa=0.09, sponsor=0.004, K_regrow=0.002),
        "suppress_only": P(B=2.5),  # high barrier, no keystone burn
        "lever+sponsor": P(kappa=0.09, sponsor=0.030),
    }.items():
        agg, df = mc(p, n=1500, seed=7)
        agg["scenario"] = name
        rows.append(agg)
    out = pd.DataFrame(rows).set_index("scenario")
    out.to_csv("results/gate13_relapse.csv")
    return out


def gate14_civilian_defense():
    """Harm distributions & defender survival: lever vs deprivation-style
    comparator (forbidden mechanism shown only as a failure reference)."""
    rows = []
    for name, p in {
        "baseline": P(),
        "lever": P(kappa=0.09, sponsor=0.004),
        "lever_defensive_boost": P(kappa=0.09, sponsor=0.004, d_max=0.95,
                                    d_rate=0.15, resist_burn=0.06),
        "deprivation_FORBIDDEN": P(kappa=0.09, sponsor=0.004,
                                    harm_c=0.08, protect=0.0),
    }.items():
        agg, df = mc(p, n=1500, seed=11)
        agg["scenario"] = name
        agg["h_final_p10"] = df["h_final"].quantile(0.1)
        agg["h_final_p90"] = df["h_final"].quantile(0.9)
        rows.append(agg)
    out = pd.DataFrame(rows).set_index("scenario")
    out.to_csv("results/gate14_civilian.csv")
    return out


def gate15_choice_rules():
    """Robustness of onset suppression + lever efficacy across selection rules."""
    rows = []
    for rule in ["eu", "noisy", "aspiration", "bureaucratic"]:
        for name, mod in {"baseline": {}, "lever": dict(kappa=0.09,
                          sponsor=0.004, B=2.0)}.items():
            p = replace(P(), rule=rule, **mod)
            agg, _ = mc(p, n=1200, seed=21)
            agg.update(rule=rule, scenario=name)
            rows.append(agg)
    df = pd.DataFrame(rows)
    df.to_csv("results/gate15_rules.csv", index=False)
    return df


def gate16_dual_use():
    """Two-channel dual-use: opportunity cost vs spillover. Reversal region."""
    rows = []
    for o in np.linspace(0, 0.8, 9):
        for spill in np.linspace(0, 0.5, 6):
            p = P(o=float(o), spill=float(spill))
            agg, _ = mc(p, n=800, T=200, seed=31)
            agg.update(o=float(o), spill=float(spill))
            rows.append(agg)
    df = pd.DataFrame(rows)
    df.to_csv("results/gate16_dualuse.csv", index=False)
    return df


def adversarial_failure():
    """Deliberate counterexample: sponsor-rich aggressor + bureaucratic rule.
    The lever should fail — documented, not hidden."""
    p = P(rule="bureaucratic", m_routine=0.0, e_b=0.0,
          sponsor=0.05, S_p0=3.0, s_release=0.15, K0=1.5,
          B=0.0, jump_rate=0.2)
    agg, df = mc(p, n=800, seed=99)
    pd.DataFrame([agg]).to_csv("results/adversarial_failure.csv",
                               index=False)
    return agg


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    for f in (gate11_reachability, gate12_keystone_exit_bound,
              gate13_relapse, gate14_civilian_defense,
              gate15_choice_rules, gate16_dual_use, adversarial_failure):
        print(f"\n=== {f.__name__} ===")
        print(f())
