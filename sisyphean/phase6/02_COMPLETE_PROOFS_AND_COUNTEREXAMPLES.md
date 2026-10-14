# 02 — Complete Proofs and Counterexamples

## Proof of P1

Given the cooperation dynamic dL/dt = κ_L·(L*(r) − L), κ_L > 0, L* single-valued, L(t) → L∞(r) monotonically. Then π(r, L(t)) → r·α(L∞)V(L∞) − c1r − c2r² = r·[αV − (c1 + c2r)]. If LVL holds, the bracket is negative ⇒ π∞(r) < 0. Under discounting δ < 1 the coercer's continuation value of sustaining r is π∞(r)/(1−δ) < 0, strictly less than abandoning (π = 0 after). ∎

## Proof of P3 (no derivative condition implies the level)

Suppose dπ/dr < 0 on (r̄, r_max]. Add Δ to c1 such that c1′ = c1 + Δ. Derivatives (a) and (b) shift by −Δ (a constant), preserving sign if Δ small; level shifts by −r·Δ. Choose Δ < 0 (lower fixed cost): signs of all derivatives unchanged, π∞ rises by |r·Δ|. Hence derivative sign never fixes level. ∎

## Symbolic counterexample to old T-1 (satisfying its premises)

Take c1 = c2 = 0.01, w = (0.05, 0.5, 0.3, 0.15), coll_action = 3,
exit_cost = 0.5, L_floor = 0.1, q = 0.7, V0 = 1, v_min = 0.3.

- Premises of old T-1 hold: consent-dependent weights dominate
  (w_phys = 0.05); cooperation response exists (L∞ = 0.1 ≪ 1).
- Yet α(0.1)·V(0.1) = 0.045 > c1 + c2·r at r ∈ {0.5, 1.0}: π∞ = +0.015
  and +0.025 — **strictly positive** (c2_t1_counterexample.csv).
- Conclusion: old T-1's premises + large response do NOT yield negative
  payoff; the level condition fails exactly because c1+c2r is tiny —
  a low-cost coercer keeps appropriating the floor level of value even
  after cooperation collapses. This is the Liberman arm in miniature.

## Complementary counterexample (LVL fails by behavior spec)

At defaults (c1 + c2·r = 0.4 at r=1), the optimizing population
(L∞ = 0.1) gives αV = 0.37 < 0.4 → π∞ < 0; the rule-bound population
(L∞ = 0.2) gives αV = 0.44 > 0.4 → π∞ = +0.04 (c3_level_grid.csv row
w_phys=1/spec=rule). Same costs, same asset mix, opposite sign: the
response *specification* alone flips the theorem's conclusion — an
honest sensitivity, not a repairable bug.

## Boundary cases verified (c5)

π(0, L) = 0 at L = 0, 0.5, 1. Derivative objects at r=0 are positive
(0.79) while level is 0 — the r=0 singularity documented.
