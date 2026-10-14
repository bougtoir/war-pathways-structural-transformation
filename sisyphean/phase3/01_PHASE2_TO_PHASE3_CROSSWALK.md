# 01 — Phase 2 → Phase 3 Crosswalk

Phase 1/2 packages preserved unchanged; nothing overwritten.
Phase 3 code lives in `sisyphean/phase3/code/` (new files, seeds differ).

| concept | Phase 2 | Phase 3 |
|---------|---------|---------|
| political objective | scalar v0 (fixed) | V_G(t) = goal_efficacy(g_type, L, pos), 6 goal types |
| leader utility | UW/UA from v | U_L from V_G + type bonuses; may persist when V_G→0 |
| sustainment | stock K only | K + endogenous replenishment law ρ(t) |
| sponsors | exogenous `sponsor` rate | patron (exit/re-enter on externality e=c·ext) + balancer (∝c) + substitution market |
| onset → damage | only burn rate | Channel A (consent L → V_G) AND Channel B (ρ) |
| consent actors | none | consent-holders, 2 non-maximizing rules (habitual, threshold) |
| cessation drivers | K ≤ K_min, dur_max | same — deliberately unchanged; lets Channel A's (non-)effect show |
| defender | grows, K-agnostic | + balancer support + h-coupled infrastructure |
| civilians | h metric + constraint | dynamically coupled; displaced violence harms h too |
| rules | 4 (eu/noisy/asp/bur.) | 6 (+ intrinsic, regime_survival) |
| nulls | none | 5 matched nulls: attrition, exog sanctions, payoff step-down, bargaining, sponsor war |
| Phase-2 negative results | sponsor-rich failure, dual-use reversal | **preserved** (g21 permanent_failure, g25 reversal edge) |

## Assumptions kept, flagged

- Phase-2 findings remain *model-conditional illustrations*, not estimates.
- Defensive asymmetry retained as a normative constraint; now weakened
  test exists (lever_weak_protect arm in g23).
- First-hitting ≈ 1 over long horizons remains true (g22): barriers delay
  (P_hit 0.953 @ T=60, B=3) and filter stochastic onsets.
