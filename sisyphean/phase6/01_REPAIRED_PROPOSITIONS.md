# 01 — Repaired Propositions (Gate 1)

Setup. r ∈ [0, r_max] intensity; L ∈ [0,1] cooperation state;
V(L) = V0(v_min + (1−v_min)L) a **flow**; q legibility;
α(L,q) = w_phys + w_hum·L + w_inst·L·q + w_net·L²;
π(r,L) = r·α·V − c1·r − c2·r², per-period. Discounting enters only via
spell length; propositions are per-period, horizon stated separately.

## The four distinct objects

(a) ∂π/∂r|_L = αV − c1 − 2c2r.
(b) dπ/dr along response equilibrium = (a) + (∂π/∂L)·L*′(r).
(c) dπ/dt on a trajectory = (∂π/∂L)·(dL/dt); L*′(r) and dL/dt are
    different objects — intensity response vs time decay.
(d) π∞(r) = π(r, L∞(r)) — the level. Abandonment is decided by (d),
    not by (a)–(c).

## Repaired propositions

**P1 (level condition — the abandonment theorem).** Fix r > 0. If the
response dynamic drives L → L∞(r) and

  α(L∞(r), q)·V(L∞(r)) < c1 + c2·r        (LVL)

then π∞(r) < 0 and any payoff-responsive coercer (eu/noisy/aspiration)
abandons coercion at r in finite time under discounting δ < 1.
Necessary condition: no proposition can yield π∞(r) < 0 unless LVL
holds, since π∞(r) = r·[αV − (c1 + c2r)].

**P2 (asset-mix boundary).** For L∞(r) = L̄ > 0 fixed, LVL defines the
boundary weight

  w*_phys = (c1 + c2r)/(r·V̄) − [w_hum·L̄ + w_inst·L̄·q + w_net·L̄²]/1

— coercion is unprofitable iff w_phys < w*_phys given the consent
weights realized. (Computed as equality on the α parametrization.)

**P3 (why a derivative cannot do the work).** dπ/dr < 0 ∀r>r̄ is
consistent with π∞(r̄) > 0 arbitrarily large; conversely π∞ < 0 requires
only LVL, no derivative sign. Derivatives order; levels decide.
Formally: for any target π* > 0 pick c1 ↦ c1 − ε — marginal conditions
unchanged, level restored positive. So no derivative inequality implies
the level condition.

**P4 (r = 0).** π(0, L) ≡ 0 for all L. No negative payoff exists at
zero coercion; claims about "force becoming unprofitable" apply only
to r > 0 — the alternative of *not coercing* always yields exactly 0 in
this accounting (no production share modeled for the coercer at r=0).

**P5 (behavioral scope).** P1–P2 bind only payoff-responsive rules.
intrinsic/regime_survival actors need not respond to π∞ < 0 — no
theorem binds them; consistent with Phase-4/5 simulations.

**Existence/uniqueness.** L∞ exists as the unique stable rest point of
dL/dt = dL_rate·(L*(r) − L) whenever L*(r) is single-valued
(continuity of clip). Monotone convergence; no cycles in this family.
