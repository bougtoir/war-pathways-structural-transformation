# 03 — Formal Results and Counterexamples (Gates 31–32)

## Four-outcome accounting (Gate 31)

States kept distinct in code and tables: onset (hit_W), sustained
violence (spell + violence_periods incl. proxy states), cessation (exit
with reason), recurrence/displacement (oscillation flag, proxy states).

**Aggressor identification is an explicit failure mode.** With
p_misid = 0.10, 10.8% of onsets are false-positive labels — recorded
rather than resolved (role swap not modeled; flagged as open failure).

**Preemption adversarial case.** Under high barrier + lever, threatened
parties strike first at mean 5.3 events/run (p_preempt = 0.30 arm,
g31). The lever's barrier creates a use-it-or-lose-it incentive — a real
side effect, counted, not modeled as tactics.

## Sufficient conditions (Gate 32)

**Theorem (finite-time cessation, corrected clock).** Let t* be the
first time post-trigger replenishment drops permanently to
ρ_post = ρ_dom + sub_rate (patron exit after exit_delay periods of
sustained e > tol). If

```
κ·c·m + r_b·d  >  ρ_dom + sub_rate          (SC-1)
```

then K-exit occurs within t* + (K(t*) + S_p(t*) − K_min)/(b̄ − ρ_post),
where b̄ is mean burn over the spell. Numerical verification
(g29_boundclock, g32_sufficiency): p_K_exit = 1.0 in all deterministic
cells; spell ≈ delay + residual depletion as predicted.

**Impossibility / stochastic guarantee erosion.** With stochastic
replenishment ρ ~ N(ρ̄, ρ_sig)⁺, SC-1 must hold on the *pathwise* mean;
spikes postpone K_min crossing. Quantified: p_K_exit drops to 0.927 at
delay 40, S_p0 = 1.5, ρ_sig = 0.025 (g32). At ρ_sig ≥ ~0.05 with
positive drift the guarantee fails entirely — robust guarantees require
bounded-support noise or a strict inequality margin, stated as the
limitation, not repaired.

**Counterexample (unchanged):** tolerant patrons keep ρ ≥ burn →
p_K_exit = 0 (g21/g29 piv_tolerant_fail reproduces). Substitution
channels (sub_rate ≥ κ·c·m − ρ_dom) are equally fatal — no unlimited
support needed, merely sufficient substitution.
