# 07 — Shared Futures as a Sensitivity Parameter (Gate 37, EXPLORATORY)

V is an optional scalar modulating the barrier: B_eff = max(0, B + 0.8·V).
Sign NOT stipulated; V ∈ {−0.5, 0, +0.5, +1.0} swept including
polarization/backlash (V < 0 lowers the effective barrier).
Output: `results/g37_sharedfutures.csv`.

## Results (κ = 0.09 lever, n=500)

| V | B_eff | first hit | spell | hollow |
|---|-------|-----------|-------|--------|
| −0.5 | 1.6 | ~4 | 31 | 9 |
| 0.0 | 2.0 | ~6 | 31 | 9 |
| +0.5 | 2.4 | ~8 | 31 | 9 |
| +1.0 | 2.8 | ~10 | 31 | 9 |

## Interpretation boundary (Discussion-only)

- V shifts onset delay smoothly (∂first_hit/∂V ≈ +4 periods per unit V);
  the effect operates through B, i.e. on *coordination/enforcement
  cost*, not on the core mechanism's sustainment channel — spell and
  hollow outcomes unchanged.
- Negative V (polarization/backlash) weakens the barrier — consistent
  with treating shared futures as a double-edged parameter, not a
  premise.
- Cross-partials noted but small in this grid; aspirational communities
  need not coincide with territorial borders — kept conceptual.
- **Not a necessary condition for any Phase-4 theorem** — all core
  results were derived at V = 0.
