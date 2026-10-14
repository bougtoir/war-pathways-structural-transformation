# 07 — Fair Rival Comparison (Gate 5)

Equal channel/parameter budgets; `results/g5_rivals.csv`.

| model | mechanism on/off | p_hit | mean onsets | exit type | discriminating implication |
|---|---|---|---|---|---|
| appropriability_lever | all channels | 1.0 | 51 | K | onsets continue; episodes end on sustainment |
| cost_only (c2=.6, no consent) | cost only | 0.0 | 0 | — | pure cost prevents onset entirely |
| sanctions_exog (ρ cut) | external supply cut | 1.0 | 134 | K | more oscillation than lever |
| attrition_no_consent | L_decay=0 | 1.0 | 124 | K | onsets triple vs lever (consent channel is what changes onset count) |
| war_economy (w_phys=.9, patron∞) | substitution ∞ | 1.0 | 33 | none | p_K_exit=0 — permanent |
| displacement_persistent | disp 60 | 1.0 | 51 | K | violence widened |

## Distinguishing implications — honest list

1. **Onset-count discrimination**: the consent channel alone (lever vs
   attrition_no_consent) reduces mean onsets 51 vs 124 — the only
   prediction that differs between our mechanism and generic attrition
   at equal complexity. A unique timing signature is explicitly NOT
   claimed (Phase-4 result preserved).
2. Generic cost increase *prevents* onsets; appropriability loss does
   not — opposite policy signatures, testable in principle.
3. Observationally equivalent pairs flagged: lever vs sanctions_exog
   differ only in oscillation intensity, not cessation — largely
   equivalent on duration outcomes.
4. Negative controls: war_economy (no consent dependence) shows the
   mechanism off — required control arm, included.
5. Rivals not reducible to ours: Kalyvas selective-violence (different
   estimand: compliance information, not value), commercial peace
   (aggregate dyadic correlation, not micro mechanism) — noted, not
   simulated.
