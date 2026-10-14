# 03 — Endogenous Response Mechanism (Gate 2)

Smallest defensible microfoundation for cooperation/exit/resistance/
adaptation. Two behavioral specifications; the sign of dL*/dr is an
outcome in both.

## Optimizing spec (`L_star_opt`)

Population coordinates (capacity `coll_action`) to withdraw cooperation
under coercion intensity r, at per-capita exit_cost. Fear of reprisal
can *raise* observed compliance:

  L* = clip(L_max + (fear_gain − coll_action/exit_cost)·r, L_floor, L_max)

- coll_action/exit_cost is the withdrawal slope (collective action over
  cost of exit) — large capacity or cheap exit → fast withdrawal.
- fear_gain > coll_action/exit_cost → dL*/dr > 0: coercion increases
  measured compliance. Compliance ≠ cooperation; the model's L is the
  *voluntary* margin, and fear-driven compliance does not feed α with
  the same terms unless parameters say so.
- collective-action constraint: with coll_action → 0 no coordinated
  exit is possible; L stays at L_max regardless of r — the
  "quiet population" regime.

## Rule spec (`L_star_rule`)

Boundedly rational threshold: cooperation is maintained up to a salience
level exit_cost + habit, then decays linearly to L_floor — no margin
optimization, inertia at low r.

## Outcomes (c4_behavior.csv)

| spec | params | dL/dr sign | reading |
|---|---|---|---|
| opt | coll .5, ec .2 | −0.78 | withdrawal dominates |
| opt | coll 3.0, ec .2 | −0.41 | strong collective action → still withdrawal, shallower at floor |
| opt | fear 1.5, coll .5 | −0.95 | fear insufficient to flip sign |
| opt | fear 3.0, coll .5 | **≈0/+** | fear outweighs withdrawal cost — compliance maintained under coercion |
| rule | any tested | −0.87 or 0 | threshold then floor |

## Liberman-type counterdomain

Physical-asset extraction stays profitable whenever α's physical term
alone covers c1 + c2·r: w_phys·V̄ > c1 + c2r, independent of L. In the
default grid this holds under the rule spec at w_phys = 1 (π∞ = +0.04)
— the documented profitable arm. Coerced compliance (fear arm) is a
second counterdomain: extraction continues on coerced output even when
voluntary cooperation is gone.
