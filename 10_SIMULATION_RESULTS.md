# 10 — Simulation Results

**ALL RESULTS ARE ILLUSTRATIVE.** Arbitrary parameterization, no
historical calibration; they demonstrate internal model behavior, not
empirical effects. Code: `code/` (seeded RNG: 20261014/7/99).
Outputs: `code/results/` (CSV + figures).

## Scenario comparison (n=20,000 draws per scenario)

P(war pathway) = ρ · P(leader selects W) · P(feasible) · p_esc:

| scenario | p_war | P(leader wants) | P(feasible) | p_esc | P(agency gap)* |
|---|---|---|---|---|---|
| baseline | .025 | .112 | 1.000 | .692 | .073 |
| A alternatives (a→.65) | .014 | .070 | 1.000 | .692 | .053 |
| B opportunity (o→.60) | .005 | .075 | **.753** | .692 | .059 |
| C alignment (δ→.20) | .013 | .063 | 1.000 | .692 | **.024** |
| D de-escalation (k→.25) | .004 | .108 | 1.000 | **.100** | .071 |
| E combined | .000 | .014 | 1.000 | .100 | .011 |

*agency gap = leader wants war while state utility rejects it.

Read-outs:
- Each intervention binds at a *different gate*: B barely moves leader
  preference (0.112→0.075) but removes a quarter of feasibility; C
  collapses the agency gap (0.073→0.024); D leaves selection untouched
  but removes escalation. The model's core claim is visible numerically:
  **interventions are stage-specific, so combining them multiplies.**
  decisive but because all gates shrink simultaneously.
- Misperception: ~92% of baseline war-pathway completions occur where
  the noiseless leader utility would have rejected force
  (p_war_misperceived=.023 of p_war=.025). Bounded rationality is a
  substantive channel, not a perturbation.

## War-rationality regions (share of (G,p) square, no noise)

| actor | baseline | A | B | C | E |
|---|---|---|---|---|---|
| state | .003 | .000 | .000 | .003 | .000 |
| regime | .070 | .025 | .031 | .021 | .000 |
| leader | **.093** | .045 | .051 | .029 | .000 |
| population | .000 | .000 | .000 | .000 | .000 |

R_leader > R_regime ≫ R_state > R_pop — divergence ordering as
constructed, quantified. Leader-only region: 0.023; leader-not-state:
0.090; no actor: 0.907.

## Sensitivity (one-at-a-time, n=3,000)

Dominant levers on p_war across the [0.05,0.95] sweep (see
`fig_sensitivity.png`): ρ and k (multiplicative gates), δ and div
(selection), o (feasibility + cost), a (alternatives). m has weaker
marginal effect once feasible — feasibility is a constraint, not a
probability.

## Evolutionary stability

See 08. ESS verdicts: S is an ESS at baseline and strong_S; no ESS
under weak_S, high exploitation (0.70), or institutional shock.
S-dominated attractors recover from 15% invasion shocks (recovery to
within 2% of pre-shock share: t≈3.4–19.0 depending on scenario);
~11.8% misperceived invasion pressure persists.

## Network cascade

See 09. Transmission only via destabilizing edges; connectivity effect
non-monotone (peak at z≈4 when s̄=0); stabilizing ties dominate topology:
s̄=0.2 alone cuts cascades ~97% at z=4; 5%-shock absorbed at s̄=0.6
(0.055 residual vs 0.998). All draws seeded — results reproduce
identically across reruns.

## Figures

- `results/fig_scenarios.png` — pathway probability and agency gap by scenario
- `results/fig_sensitivity.png` — OAT sensitivity of p_war
- `results/fig_cascade.png` — cascade vs degree × stabilizing share
- `results/fig_basin.png` — strategy basins by payoff scenario

## Reproducibility

```
cd code
pip install -r ../requirements.txt   # numpy scipy pandas matplotlib networkx openpyxl
python run_all.py                    # writes results/*.csv and *.png
python make_prior_studies_xlsx.py    # rebuilds ../03_CLOSEST_PRIOR_STUDIES.xlsx
```

Bounded-rationality, adversarial (high exploit), and institutional-shock
cases are all included above; no result in this file is presented as
empirical evidence.
