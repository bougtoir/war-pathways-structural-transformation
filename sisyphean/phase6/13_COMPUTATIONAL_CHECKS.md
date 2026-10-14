# 13 — Computational Checks (Gate 8)

`code/model6.py`, `code/checks6.py`, `code/tests/test_model6.py`.
numpy/pandas/pytest only; fixed seeds; runtime < 1 min; simulation
outputs labeled computational, never conflated with real data.

## What each check verifies

| file | check | key result |
|---|---|---|
| c1_objects.csv | four distinct objects | at r=0: ∂π/∂r=+0.79 while π(0)=0 — the conflation made visible |
| c2_t1_counterexample.csv | old-T1 premises ⇒ π∞>0 | π∞=+0.015/+0.025 under dominant consent weights — old claim fails |
| c3_level_grid.csv | LVL boundary across w_phys, two specs | opt: π∞<0 ∀mixes; rule: π∞>0 at w_phys=1.0 — spec decides sign |
| c4_behavior.csv | dL*/dr is an outcome | negative everywhere except fear_gain=3.0 (≈0/+) — compliance maintained under coercion is possible |
| c5_boundaries.csv | r=0, L edge | π(0,L)≡0 confirmed |
| c6_regimes.csv | two stable regimes | physical+rule profitable; consent regime unprofitable — both stable |
| tests/ | boundary + sign claims | 5 tests pass |

## Explicitly NOT claimed

- No simulation result was used to "prove" a proposition — checks are
  numerical consistency verification of analytic statements.
- No expensive sweeps: only information-bearing grids (w_phys × spec;
  behavior parameter triples) were run.
