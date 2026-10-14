# 11 — Simulations and Sensitivity (Gates 19–22, 26)

All runs: `cd phase3/code && python run_all.py`. Seeds fixed per experiment.
Tables in `results/*.csv`. Python 3.10, numpy+pandas only, ~4 min total.

## Gate 19 — endogenous trigger (g19_consent.csv)

| rule | withdraw | V_G_final | L_final | hollow periods |
|------|----------|-----------|---------|----------------|
| threshold | yes | 0.0 | 0.99 | 34 |
| threshold | no (control) | 0.0 | 1.00 | 27 |
| habitual | yes | 0.0 | 1.00 | 37 |
| habitual | no | 0.0 | 1.00 | 27 |

Trigger derived from actors: hollow periods rise 27→34–37 when
consent-holders withdraw; collapse absent in the off-arm for the
consent channel (V_G also falls via pos decline — honestly reported:
Channel A's isolated contribution is ~7 extra hollow periods, not the
whole collapse). Gate 19: PASS (endogenous, two rules, falsifiable
control arm) — with the caveat that pos-driven efficacy loss coexists.

## Gate 20 — channel factorial (g20_channels.csv)

A alone ends nothing (spell 80 = cap); B alone ends (56); both = 56.
V_G final ≈ 0 for consent goals under any war; 0.2 floor for intrinsic.
**Efficacy collapse does not cause cessation; sustainment collapse does.**

## Gate 21 — sponsors (g21_sponsors.csv): see 07.

## Gate 22 — reachability/exit/recurrence (g22_reach.csv)

| scenario | T | P(hit W) | first hit | spell | displaced |
|----------|---|----------|-----------|-------|-----------|
| baseline | 60/150/300 | 1.0 | 0 | 56 | 0 |
| lever B=3 | 60 | 0.953 | 16.2 | 56 | 6.3 |
| lever B=3 | 300 | 1.0 | 18.9 | 56 | 6.7 |
| combined | 60 | 0.953 | 16.2 | 31.1 | 6.3 |
| combined | 300 | 1.0 | 18.9 | 31.3 | 6.7 |

No permanent-prevention claim: P(hit)→1 as T grows; barriers delay and
filter; displacement ≈ 6–7 events/run is the cost. Oscillation/recurrence
concentrated in stochastic rules (g24). Transient-state question:
'onset undermines its own conditions' produces a true transient only
when ρ remains below burn — otherwise it relocates violence
(displaced_mean>0) rather than eliminating it.

## Gate 26 — matched nulls (g26_nulls.csv + g26_stepdown.csv)

Same K0/S_p0/κ/m/T, eu rule:

| model | spell | V_G_final | hollow | harm |
|-------|-------|-----------|--------|------|
| n0 attrition | 38 | 0.012 | 9 | 0.026 |
| n1 exog sanctions | 34 | 0.089 | 5 | 0.021 |
| n2 step-down | 56 | 0.2 | 0 | 0.058 |
| n3 bargaining | 38 | 0.012 | 9 | 0.026 |
| n4 sponsor war | 80 | 0.0 | 58 | 0.122 |
| lever endogenous | 56 | 0.0 | 34 | 0.058 |

Discrimination: duration alone does NOT separate lever from step-down
(56 vs 56) — we state this. What separates: **hollow periods** (lever 34
vs step-down 0 vs sanctions 5) — the endogenous model uniquely predicts
measurable efficacy collapse *preceding* cessation; and patron_retained /
conditional exit dependence on externality (g21), absent in all nulls.
Not a tautology: set L_decay=0 or ρ≥burn and the signature disappears.
