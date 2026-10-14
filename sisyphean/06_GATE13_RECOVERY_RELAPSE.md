# 06 — Gate 13: Recovery, Relapse, Displacement, First-Strike Incentives

Output: `gate13_relapse.csv` (n = 1500/condition, seed 7), T = 300.

## Metrics

| scenario | mean onsets | spell | harm mean | displaced |
|----------|-------------|-------|-----------|-----------|
| baseline | 1.0 | 39.0 | 0.028 | 0 |
| lever | 1.0 | 23.0 | 0.009 | 0 |
| lever + slow K regrowth | 1.0 | 23.0 | 0.009 | 0 |
| suppress-only (B=2.5) | 1.0 | 39.0 | 0.028 | 3.9 |
| lever + strong sponsor | 1.0 | 38.0 | 0.026 | 0 |

Under the eu/aspiration selection regime one onset per horizon is typical;
high-variance rules (gate15 table) produce oscillation: noisy rule
52 onsets baseline → 9.3 under lever; bureaucratic 60 → 10.1. The lever
therefore *reduces oscillatory on-off violence* roughly 5–6× under
rules where onset is stochastic, while under deterministic-selection rules
it only shortens spells.

## Assessment against the gate's fail conditions

- **Time to cessation**: lever halves spell length; no infinite-war regime
  except sponsor-rich region (documented).
- **Cumulative civilian harm**: reduced ~3× under lever — rapid cessation
  is not counted as success when harm occurs first (harm measured
  cumulatively, p90 reported, not just cessation time).
- **Postwar functionality**: h_final 0.85 → 0.91 under lever.
- **Recurrence/relapse**: K regrowth re-opens onset; under persistent
  grievance (q_decay = 0) recurrence risk is rule-dependent — the lever
  does not remove grievance, it only makes each episode shorter and onset
  less frequent. **Honest residual: relapse is reduced, not eliminated.**
- **Displacement**: blocking onsets reroutes ~35% of attempts to sub-war
  violence (displaced_mean ≈ 3.9–7.2 under high B). The framework does not
  count displaced violence as success — it is reported as a cost.
- **First-strike incentive**: a high barrier B penalizes *initiation*
  equally whoever moves first; no asymmetry favoring first strike was
  introduced. However we did not model preemption incentives explicitly —
  flagged as a limitation rather than claimed resolved.

**Gate 13: CONDITIONAL PASS.** No unresolved fatal item; relapse reduction
partial; displacement quantified as cost, not hidden.
