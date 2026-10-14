# 08 — Evolutionary Stability

## Model choice (required justification)

Replicator dynamics on strategies {W, B, S} is used **only as an
illustrative adaptive-selection metaphor** — for institutional diffusion,
elite learning, or strategy imitation — because the literal mapping
(states as population members, fitness as replication) cannot be
justified for ~200 strategic actors. This limitation is stated, not
resolved. Alternative defensible frames: best-response dynamics with
inertia, reinforcement learning on institutional rules, or ABM à la
Cederman (2001). The qualitative conclusions below survive the
metaphor choice only in the *direction* of conditional stability.

## Payoff structure

A[i,j] = payoff to i against j (code/evolutionary_stability.py):

```
        W            B                S
W    [ -0.30,   0.60+exploit,    0.60+exploit ]
B    [  0.10,   beta,            beta-0.05    ]
S    [  0.15,   beta+alpha,      beta+gamma+alpha ]
```

alpha: substitution efficiency premium; beta: bargaining surplus;
gamma: S-vs-S resilience bonus; exploit: aggressor's gain vs nonviolence.
Key feature: W exploits both B and S one-on-one; S only wins if
(beta+gamma+alpha) dominates W's exploitation term in expectation —
nonviolence pays against nonviolence but bleeds against aggression
without external enforcement.

## Results (illustrative, code/results/evolutionary_stability.csv)

| scenario | ESS? | eq shares (W,B,S) | S basin* | post-shock S |
|---|---|---|---|---|
| baseline (α=.4,β=.5,γ=.3,exploit=.35) | S only | ≈(0,0,1) | 0.93 | recovers to 1.0 (t≈8.6) |
| weak_S (α=.1,γ=.1) | none | S-dominant mix 0.64 | 0.93* | 0.64 (t≈9.9) |
| strong_S (α=.6,γ=.5) | S only | ≈(0,0,1) | 0.93 | 1.0 (t≈3.4) |
| high_exploit (.70) | none | S-mix 0.82 | 0.93* | 0.82 (t≈19.0) |
| instit_shock (β=.3,exploit=.5) | none | S-mix 0.82 | 0.93* | 0.82 (t≈19.0) |

*Basin measured by argmax share at t=300, which overstates pure-S
convergence; the eq shares are the honest attractor description.

**Findings:**
1. S is an ESS only when substitution premium + resilience exceed the
   exploitation wedge — *conditional stability*, not unconditional peace.
   With exploit=0.70 no pure strategy is an ESS; the system rests at an
   S-dominant mixed state (≈18% W permanently latent).
2. The S-dominated equilibrium *survives* a 15% W invasion shock and
   re-converges — measured recovery to within 2% of the pre-shock share:
   t≈3.4 (strong_S), 8.6 (baseline), 9.9 (weak_S), 19.0 (high-exploit and
   institutional-shock cases — the mixed equilibria return to their
   coexistence level, aggression persists but bounded).
3. W is never an ESS in this parameterization: W-vs-W payoff −0.30 is
   self-defeating. Aggression persists only as a parasite on nonviolent
   hosts — the model's version of "war needs peace to feed on".
4. Under misperception (σ_noise=0.15 on payoffs), ~11.8% of draws
   perceive W as outcompeting S — bounded rationality *alone* does not
   destroy the structure but keeps a permanent invasion pressure.

## Answer to the key question

Can a nonviolent interaction structure remain stable without rational or
benevolent actors? **Conditionally yes** — under adaptive dynamics it
requires (i) the substitution premium exceeding the exploitation wedge,
(ii) some enforcement of the boundary (S must not fully disarm — the
model's S retains a 0.15 defense payoff), and (iii) shock magnitudes
below the basin boundary. The framework does not deliver unconditional
stability, and asserting it would be UNSUPPORTED.

## Local vs global vs resilience (required distinctions)

- **Local stability:** S is locally stable iff A[2,2] > A[0,2] (ESS
  condition) — scenario-dependent.
- **Global/basin:** S-attractor dominates the simplex in all runs
  (argmax basin ≈0.93) but the attractor is not always pure S.
- **Resilience:** recovery after a 15% invasion shock occurs in ESS
  scenarios; in mixed-equilibrium scenarios the *post-shock state is the
  same mixed state* — the structure is resilient as a statistical
  distribution, not as purity.
- **Resistance to strategic invasion:** monotone in exploit; breaks
  between exploit 0.35 (stable) and 0.70 (no ESS) — the fragility
  frontier is a researchable object, not a fixed verdict.
