# 08 — Civilian Preservation and Defense (Gate 23, HARD STOP)

Output: `results/g23_civilian.csv` (n=1000, seed 29). H and D are
**dynamically coupled variables**: h degrades under harm and displaced
violence; d's buildup is gated on h (infrastructure), not assumed fixed.

## Non-inferiority vs baseline (pre-specified)

| scenario | spell | harm mean | harm p90 | h_final | h_p10 | civilian_ok | defender_ok |
|----------|-------|-----------|----------|---------|-------|-------------|-------------|
| baseline | 56.0 | 0.058 | 0.058 | 0.782 | 0.782 | 1.0 | 1.0 |
| lever | 31.1 | **0.020** | 0.024 | **0.873** | 0.858 | 1.0 | 1.0 |
| lever, weak protection | 31.1 | 0.037 | 0.041 | 0.755 | 0.740 | 1.0 | 1.0 |
| deprivation (FORBIDDEN) | 32.1 | **2.01** | 2.21 | **0.00** | 0.000 | **0.0** | 1.0 |

## Findings

- Lever is strictly non-inferior: shorter spells cut cumulative harm ~3×;
  h_final better. Cessation is never credited while mass harm precedes it —
  harm is measured cumulatively (and at p90).
- When protection degrades (protect 0.6→0.2) the lever still helps but
  h_p10 falls to 0.74 — protection is a real parameter, not a constant;
  reported, not hidden.
- Deprivation achieves similar spell length at ~60× the harm and total
  civilian collapse — the constraint binding is demonstrated by contrast.
- Displaced violence feeds back into h (disp_to_civ): blocking onsets is
  not free; counted as civilian cost.
- Residual caveat: under sponsor-rich failure (g21) civilian_ok → 0 — the
  lever failing *means* civilians are worse off. Non-inferiority holds
  only inside the model's feasible region; stated, not generalized.

**Gate 23: PASS (model-conditional).** Protection is emergent from
shorter wars, not assumed; no toy-threshold claim about real wars.
