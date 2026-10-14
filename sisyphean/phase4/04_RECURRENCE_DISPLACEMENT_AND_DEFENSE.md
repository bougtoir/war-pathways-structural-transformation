# 04 — Recurrence, Displacement, and Defense (Gate 33)

Output: `results/g33_recurrence.csv`. Displaced violence is now a
*persistent state* (proxy_left periods at reduced harm rate), not a
point count.

## Total-violence comparison (the gate's required metric)

| scenario | war spell | violence periods | total harm | h_p10 |
|----------|-----------|------------------|------------|-------|
| baseline | 56.0 | 56.0 | 0.058 | 0.782 |
| lever (disp instant) | 31.3 | 31.3 | 0.026 | 0.818 |
| lever (disp persists 20) | 31.3 | **148.7** | **0.057** | 0.460 |
| lever (disp persists 60) | 31.3 | **231.7** | **0.057** | 0.242 |

## Most damaging Phase-4 finding

**When displaced conflict persists, the lever's civilian-harm advantage
over baseline is ~zero** (0.057 vs 0.058) while total violence periods
increase 4–7×. The lever shortens the *named war* but converts it into a
longer smoldering conflict with comparable cumulative harm and worse
h tails (h_p10 0.24 vs 0.78). A "successful" lever can thus be strictly
worse on the gate's own metric — reported as a failure region, the
largest one this phase.

## Defender

Defense stays non-degraded (d ≥ d_min everywhere, balancer support
endogenous). Preemption (g31) is the defender-side failure: barriers
that delay the aggressor can incentivize defensive first strikes —
5.3 events/run in the adversarial arm.

## Failure regions (prominent)

1. ρ ≥ burn (tolerant sponsors, substitution) — permanent failure.
2. Persistent displacement — total harm unchanged, violence widened.
3. Mis-identification — 10.8% false-positive onset labeling; lever does
   not know whom to starve.
4. High-barrier + intrinsically motivated actors — maximal displacement
   (up to 40 events, g24 replicated).
