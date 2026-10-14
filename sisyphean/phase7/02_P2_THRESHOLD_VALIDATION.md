# 02 — P2 Threshold Validation (Gate 2)

## Corrected algebra (simplex imposed: w ≥ 0, Σw = 1)

π < 0 ⟺ α·V < c1 + c2·r. With α = w_phys + S, S = w_hum·L + w_inst·L·q
+ w_net·L²:

  **π < 0  ⟺  w_phys < w*_phys := (c1 + c2r)/V(L) − S**

Phase-6 doc-01 printed the first term as (c1+c2r)/(r·V̄) — a
superfluous r; the code used the correct form. **Defect corrected.**

## Feasibility conditions (necessary AND sufficient)

Under the simplex, α = 1 − w_hum(1−L) − w_inst(1−Lq) − w_net(1−L²),
so α ∈ [something, 1] and α(L=1,q) = 1 identically.

- **Interior threshold** w*_phys ∈ (0,1) exists iff
  S < (c1+c2r)/V < 1 + S.
- **Boundary**: if (c1+c2r)/V ≥ 1+S, every mix is unprofitable at that
  (L,q,V,r) — maximal non-appropriability region.
- **Nonexistence**: if (c1+c2r)/V ≤ S, EVERY mix remains profitable —
  the non-appropriability claim is vacuous in that region. In
  particular at L=1, α=1 → π<0 iff V(1) < c1+c2r: **independent of all
  weights** — an invariant bound Phase 6 never reported.

## Dependences (all now explicit)

- w*_phys increases linearly in r (through c2r/V): higher intensity
  widens the unprofitable region — P6 omitted this.
- w*_phys decreases in V: richer targets enlarge the profitable region.
- w*_phys decreases in L through S (holding w's fixed): at high
  cooperation the threshold tightens — cooperation makes coercion MORE
  profitable in physical terms yet also raises A via consent terms:
  the two-sided role of L, quantified in results/r9_domain.csv.

## Numerical counterexample to Phase-6 text

Phase-6 doc claimed w*-formula with extra r: at r=0.5, V=1, c1=c2=0.1
their formula yields w* ≈ 0.4−S; correct is 0.15−S — a factor-2.7
difference on that cell. The code's grid is unaffected.

## Degenerate cases

- L=0: α = w_phys → π<0 iff w_phys < (c1+c2r)/V(0): pure-physical
  threshold, exact.
- q irrelevant at w_inst=0; L² term binds only when w_net > 0.
