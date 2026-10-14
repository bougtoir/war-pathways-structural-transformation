# 01 — Phase 3 Reproduction and Corrections (Gate 29)

Output: `results/g29_audit.csv`, `results/g29_boundclock.csv`.

## Reproduction verdict: PASS

All pivotal Phase-3 outputs reproduce exactly under the same code+seeds:

| pivot | Phase 3 claimed | Phase 4 rerun |
|-------|-----------------|---------------|
| Channel A alone | spell 80, no K-exit | 80.0, p_K_exit 0.0 ✓ |
| Channel B alone | spell 56, K-exit | 56.0, p_K_exit 1.0 ✓ |
| tolerant-sponsor failure | no exit | 80.0, p_K_exit 0.0 ✓ |
| civilian protection | harm 0.020, h 0.87 | 0.020, 0.873 ✓ |

## Corrections applied

**C1 — bound clock origin.** Phase 3 stated t_exit ≤ (K₀+S_p₀−K_min)/(b−ρ_post)
"from onset". Corrected: the bound's clock starts at *sponsor exit* (or
any trigger of post-trigger depletion). With exit_delay ∈ {0,10,30}:

| delay | spell (κ=.045) | spell (κ=.09) |
|-------|----------------|----------------|
| 0 | 56 | 31 |
| 10 | 63 | 35 |
| 30 | 77 | 43 |

Observed spells rise by ≈ the delay minus pre-exit burn — consistent
with bound t_exit ≤ t_exit_trigger + (K(t_trigger)+S_p−K_min)/(b−ρ_post).
Docs updated; Phase 3 wording flagged as imprecise, not wrong.

**C2 — hollow threshold arbitrary.** hollow_periods: 27 (thr .1) → 34 (.2)
→ 39 (.3) → 44 (.4). The qualitative finding (hollow persistence exists)
is threshold-robust; magnitudes are not. Reported as sensitivity.

**C3 — V_G vs position confound.** V_G falls both via consent (L) and via
battlefield position decline (pos↓ when d>m). Phase-3 g19 isolated the
consent share at ~7 hollow periods of 34. Phase 4 retains this honest
decomposition; Channel A's incremental contribution is modest.

## Equations vs code consistency

Checked: goal_efficacy piecewise (6 types), sponsor_step exit/re-entry
and streak counting, stepdown null bypass, displaced-violence state
accounting, harm accumulation (war + proxy), K regrow only outside war.
One inconsistency fixed: `simulate3` signature gained `hollow_thr` param
(previously hardcoded 0.2 in the count) — now an explicit parameter.
