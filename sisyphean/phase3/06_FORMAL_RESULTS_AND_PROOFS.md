# 06 — Formal Results and Proofs

## R1 (finite-lag exit under replenishment collapse). 

If patron exit is absorbing and burn b = κ·c·m + r_b·d exceeds
ρ_post = ρ_dom + sub_rate, then war exits in

```
t_exit ≤ (K₀ + S_p₀ − K_min)/(b − ρ_post)
```

from onset. *Proof sketch:* K is monotone-decreasing at rate ≥ b−ρ_post
once S_p drains; K hits K_min within the bound; exit rule forces
termination. Simulation agreement: all K-exit runs fall below bound
(gate12 pattern preserved).

## R2 (hollow-war existence). 

For consent-dependent goals, once L ≤ L*, V_G = pos(0.3+0.7L) < 0.2 can
hold while U_L > 0 → war continues with zero efficacy. Observed:
hollow_periods mean 27–58 across scenarios (g20/g26). **V_G decrease does
not imply termination** — required honest result, confirmed.

## R3 (channel separability). 

A alone: spell unchanged (80, dur cap) — efficacy collapse cannot end a
war whose sustainment is intact. B alone: spell 56 — sustainment ends it.
Both: 56 — no interaction gain in this calibration (channels are
causally disjoint: L never enters dK). The lever's *cessation* work is
entirely Channel B; Channel A produces hollow-war *observability* and
post-war legitimacy loss, not cessation.

## R4 (failure region). 

If ∃ sponsor law with ρ ≥ b sustained (tolerant patron: tol ≥ c·ext
always; sub_rate ≥ b−ρ_dom), K never starves → no K-exit
(p_K_exit = 0, spell = dur_max). Proven by the bound's denominator
vanishing; simulated in g21 permanent_failure. **This is the lever's
exact boundary.**

## R5 (non-superiority to exogenous sanctions).

Under matched budgets the endogenous lever (spell 56) is *slower* than
exogenous sanctions (spell 34): endogenous channels cost onset delay but
replenishment remains higher until tolerance binds. The model's value is
therefore NOT claimed as faster termination — see discriminating
predictions (14) for what it uniquely predicts.
