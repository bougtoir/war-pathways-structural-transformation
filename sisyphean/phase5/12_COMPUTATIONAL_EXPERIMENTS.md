# 12 — Computational Experiments (Gate 8)

`code/model5.py` + `code/experiments5.py`; `results/*.csv` (4 files).
n=400–600 MC per cell; all parameters illustrative; seeds fixed;
runtime < 10 min.

## g23 — asset-mix theorem sweep

Onset occurs in all mixes (p_hit=1, onsets 27–51): appropriability does
not gate initiation. Exit mechanism flips by mix — physical_only never
exits "unprofitable" (0.0); human/institutional/network mixes do
(p=1.0). The emergent sign result of Gate 3 holds numerically.

## g5 — fair rivals (see doc 07)

Key rows: consent channel removes ~60% of oscillation vs generic
attrition (51 vs 124 onsets); war_economy is the permanent-failure arm
(p_K_exit=0); pure cost eliminates onset (a rival mechanism more
effective at prevention — reported).

## g8 — coercer rules (see doc 08)

Sustainment channel is rule-agnostic (p_K_exit ≈ 1 all rules);
onset/harm are not: intrinsic (93 onsets) and regime_survival (70)
produce the longest spells — non-rational actors undeterred, Phase-3/4
finding preserved.

## g8 regions — success AND failure map

tol_patron = 2.0 (patient sponsors) → p_K_exit = 0 across all asset
mixes: **the sponsor-failure region from Phase 3/4 remains intact and
is the dominant boundary**, independent of asset composition. Asset mix
shifts exit type (unprofitable vs K), not existence of failure.

## Limits

No empirical calibration; runtime toy-scale; no strategic multi-actor
game — these are mechanism checks, not predictions.
