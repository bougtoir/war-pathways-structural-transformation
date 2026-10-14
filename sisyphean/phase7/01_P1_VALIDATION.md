# 01 — P1 Validation (Gate 1)

Independent reconstruction. Four claims kept logically separate:

## Claims and verdicts

| claim | verdict |
|---|---|
| (1) declining marginal returns ∂π/∂r < 0 | true at fixed L beyond r* = (αV − c1)/2c2 — but ∂π/∂r is positive at r=0 whenever αV > c1 (0.79 at defaults) — coercion's marginal return is positive at the margin of onset |
| (2) π(r) < 0 (level) | ⟺ αV < c1 + c2r — proven; a *level* statement needing no derivative |
| (3) abandonment | NOT implied by π<0 — requires a behavioral update rule; valid only for payoff-comparing rules |
| (4) finite-time abandonment | conditionally provable — bound below |

## Derivative ⇒ level: FALSE (formally)

dπ/dr < 0 on an interval is consistent with π > 0 everywhere on it.
Random check: P(∂π/∂r<0 ∧ π>0) = 0.157 over 2000 draws
(symbolic_checks.csv). Phase 6's P3 is CONFIRMED.

## Level ⇒ abandonment: FALSE without a rule

π∞ < 0 leads to abandonment only if the decision rule compares π to an
outside option: valid for eu (switch at π<0), noisy (probability →1),
aspiration (π<0 triggers search). INVALID for intrinsic (fires
regardless), regime_survival (continues if q > threshold or already
coercing — costs irrelevant). **General abandonment result: impossible;
counterexample exists in-model.**

## Finite-time abandonment — sufficient conditions + bound

Given L(t) → L*(r) via dL/dt = κ(L* − L), κ>0:

If (i) α(L)V(L) strictly increasing in L on the path,
(ii) α(L*)V(L*) < c1+c2r < α(L0)V(L0) (strict crossing exists),

then a **unique** crossing time exists:

  t* = (1/κ)·ln[(L0 − L*)/(L_x − L*)],  L_x: α(L_x)V(L_x) = c1+c2r

and abandonment occurs at t* for payoff-comparing rules. If αV is not
monotone in L (e.g. w_net large creates curvature), multiple crossings
are possible — boundary case, stated.

## Verdict

P1 as corrected is **conditionally valid**: {level condition + strict
crossing + monotone path + payoff-comparing rule} → unique finite
abandonment time. As a general theorem it does NOT exist — documented.
