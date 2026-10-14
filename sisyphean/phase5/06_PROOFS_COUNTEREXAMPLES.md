# 06 — Proposition, Proof Sketch, Counterexample (Gate 3)

## Proposition (bounded)

Let the coercer sustain coercion at intensity r with net payoff
π(r,L) = r·α(L,q)·V(L) − c1·r − c2·r², and let consent follow
dL/dr < 0, L → L_floor ≥ 0 under sustained coercion.

**If** the consent-dependent weight w_c = w_hum + w_inst·q̄ + 2·w_net·L̄
satisfies

```
r_max · w_c · |dL/dr|̄ · V̄  >  w_phys·V̄ − c1 − 2·c2·r_max      (T-1)
```

then π(r_max, L(t)) → π⁺ < 0 under sustained coercion: the coercer's
long-run realizable value declines while civilians' h remains bounded
(protect > 0 keeps h ≥ h_min in the tested grid).

Meaning: "more coercion → less appropriable value" holds only when
consent-dependent weights dominate physical ones AND consent actually
withdraws. The conclusion is NOT a restatement of a monotonic payoff —
it is a comparative-static sign flip across the asset mix.

## Numerical verification (g23_mix.csv)

| mix | p_unprofitable exit | mean onsets | reading |
|---|---|---|---|
| physical_only | 0.00 | 51.5 | coercion pays — sign positive |
| human_only | 1.00 | 42.3 | consent withdrawal → net < 0 exits |
| institutional | 1.00 | 31.5 | same + fewer onsets |
| network_heavy | 1.00 | 27.8 | strongest consent effect |
| mixed | 0.00* | 51.0 | mixed arm exits on K, not profitability |

*mixed arm: unprofitable exits ≈ 0 because K-depletion fires first —
onset-region qualification stated honestly.

## Counterexample (sign reversal)

w_phys = 1, c2 small, patron tolerant: net stays positive, coercion
episodes run to dur_max or K-exit with A > 0 throughout — reproducing
Liberman's qualitative result that conquest of industrial-physical
assets can pay. This is the model's own falsifier and it holds.

## Impossibility statements

- No global "coercion never pays" theorem exists; T-1's negation is a
  large parameter region.
- For non-maximizing rules (intrinsic, regime_survival) the sign of π
  is behaviorally irrelevant — no theorem binds them (g8_rules: longest
  spells occur exactly there).
