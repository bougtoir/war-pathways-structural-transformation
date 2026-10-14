# 04 — Causal Graph and Actors

## Actors and what each controls

| actor | controls | information | rule class |
|-------|----------|-------------|------------|
| aggressor leader | onset attempts, continuation | U_L (may ≠ V_G), m, q | 6 rules (eu, noisy, aspiration, bureaucratic, intrinsic, regime_survival) |
| consent-holders | cooperation leg L | observed war state + cumulative harm | habitual or threshold (both non-maximizing) |
| patron sponsor | flow into ρ | externality e = c·ext | tolerance threshold + re-entry |
| balancer sponsor | defender support | observed c | proportional response |
| defender | d buildup | own h (infrastructure) | mechanical buildup |
| civilians | h (harmed, coupled) | — | passive state |
| substitution market | ρ floor | patron absence | opens when patron exits, bounded rate |

## Graph (directed)

```
onset ──> c (intensity) ──> e = c·ext ──> patron exit ──> ρ ↓ ──> K ↓
   │             │                                        ↑
   │             └────> observed harm ──> L ↓ ──> V_G ↓    │ (Channel A)
   │                            (consent-holders)         │
   └────> m,c ──> burn ───────────────────────> K ↓        │
                                                       (Channel B joins)
   c ──> balancer support ──> d ↑ ──> resist_burn ↑ (complements lever)
   c ──> harm ──> h ↓ ──> (couples) d buildup rate ↓, and blocks
   defender infrastructure when h low — civilians are not free
   barrier-blocked onsets ──> displaced violence ──> h ↓ (cost)
   V_G ↓ ≁ termination: U_L may remain > 0 → hollow war
```

## Endogeneity proof obligation (Gate 19)

Nothing writes `V_G := f(onset)` directly. V_G = g_attain(L, pos); L is
lowered only by consent-holders responding to observed war/harm under
their own rules. Set `L_decay = 0` (g19 withdraw=False arm) and the
collapse vanishes — the trigger is actor-produced, falsifiable by
parameter, not wiring.
