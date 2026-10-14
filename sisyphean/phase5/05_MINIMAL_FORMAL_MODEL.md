# 05 — Minimal Formal Model (Gate 2)

Agents i ∈ {coercer, target population, patron, balancer, market}.
Target j holds produced value V(θ,t). State θ = (q, m, L, K, S_p, h, d,
r, coercion, proxy_left, patron).

## Core construction (code: `model5.py`)

```
V(θ,t)      = V0 · (0.3 + 0.7·L)                # production needs consent
α(r,θ,t)    = w_phys + w_hum·L + w_inst·L·q + w_net·L²
A(r,θ,t)    = r · α · V                          # realized appropriation
C(r)        = c1·r + c2·r²                       # administration cost
net payoff  = A − C
```

α is **derived**: L follows a consent dynamic (threshold or habitual
withdrawal under coercion), q legibility, and the w-weights are the
target's asset mix. Sign of ∂A/∂r is emergent:
∂A/∂r = α·V + r·(∂α/∂r)·V + r·α·∂V/∂r − C′(r) with
∂α/∂r = (w_hum + w_inst·q + 2·w_net·L)·∂L/∂r < 0 under coercion.

## Decisions

Coercer: 6 rules (eu / noisy / aspiration / bureaucratic / intrinsic /
regime_survival) — onset via fires(x_p) at prospective r_max, never
assuming maximization. Population: consent rules. Patron: externality
tolerance exit (Phase 3 mechanism, preserved). Sustainment stock K
depletes at κ·r·m + resist·d vs replenishment ρ(patron) — the Phase-3/4
clock, intact.

## Explicit non-assumptions

- dA/dr < 0 is NOT built in — it fails for w_phys → 1.
- No welfare collapse required: h decrements are a cost, not a channel.
- Total gain ≠ marginal gain ≠ initiation utility: fires() uses
  prospective net at r_max; marginal comparative statics are analytic;
  onset uses its own gate (m + barrier).
