# 08 — Scenario Grid (Gate 38)

Output: `results/g38_grid.csv` (36 cells, machine-readable, n=400/cell).
Robust = p_K_exit > 0.9 AND civilian_ok > 0.9.

## Robust vs fragile combinations

| condition | robust |
|-----------|--------|
| sub = 0, κ = 0.09, any tol, any V | ✓ robust |
| sub = 0, κ = 0.045, tol ≤ 0.6 | ✓ robust |
| sub = 0.02, κ = 0.09 | ✓ robust |
| sub = 0.02, κ = 0.045 | ✗ fragile |
| sub = 0.05, any κ | ✗ fragile |
| tol = 2.0 (patient patron) + κ = 0.045 | ✗ fragile |

## Read

- The lever's robust region is **{low substitution × high burn-rate ×
  intolerant sponsors}**; it shrinks to zero as substitutability or
  patron tolerance grows. This is the same boundary as Gate 32's SC-1 —
  the grid corroborates rather than adds.
- V (shared futures) never flips robustness — onset-side parameters do
  not rescue a sustainment failure (consistent with channel
  separability, Phase 3 R3).
- Political misalignment and exogenous shocks enter only through
  delay/streak timing: they shift spell lengths, not the robust/fragile
  boundary.

All quantities hypothetical and illustrative; no real-world effect
sizes claimed.
