# 06 — Formal Model

Minimal model. Every complexity present has an assigned explanatory job;
nothing else was added. Implementation: `code/bargaining_model.py`.

## 1. Setup

- Political objective stake: G ∈ [0,1].
- Expected victory probability: p ∈ [0,1]; leader's belief p̂ = p + σε,
  ε ~ N(0,1), σ ≥ 0 (bounded rationality / misperception).
- Nonviolent alternatives A deliver an imperfectly implemented settlement:
  U_A^state = α·p·G − 0.05 + 0.25·a, where α ∈ (0,1] is settlement
  implementation efficiency and a ∈ [0,1] is the quality of nonviolent
  alternatives.
- Structural vector θ = (a, o, δ, k, m, div, lam, σ, ρ, α):
  a alternatives quality; o civilian opportunity cost; δ state–regime
  incentive divergence; k escalation amplification; m mobilization
  capacity; div diversionary benefit; lam leader removal exposure;
  σ misperception; ρ exogenous bargaining-failure rate; α settlement
  efficiency.

## 2. Actor-specific utilities

```
U_W^state  = p̂·G − c_state,                 c_state = 0.35 + 0.30·o
U_A^state  = α·p·G − 0.05 + 0.25·a

U_W^regime = U_W^state + [div·δ − lam·(1−p̂)·δ]·G
U_A^regime = U_A^state + 0.10·δ·(a − 0.3)

U_W^leader = U_W^state + [1.4·div·δ − 1.6·lam·(1−p̂)·δ]·G
U_A^leader = U_A^regime

U_W^pop    = p̂·0.3·G − (0.55 + 0.25·o)
U_A^pop    = p·0.3·G + 0.30·a
```

Properties: utilities diverge by construction (δ scales the survival
terms); population bears costs leaders do not; the leader's region is
state-region plus a survival wedge that *grows with the stake G*.

## 3. War-rationality regions

R_a(θ) = { (G,p) : U_W^a(G,p,θ) > max U_A^a(G,p,θ) }  — defined on the
stake × capability square, not on G alone, so that "region size" has a
defined measure: |R_a| = area(R_a)/area(unit square) ∈ [0,1].

Objective/subjective distinction: R uses subjective p̂ where noise applies;
realized outcomes are a third object.

Baseline result (illustrative): |R_leader| = 0.093, |R_regime| = 0.070,
|R_state| = 0.003, |R_pop| = 0.000; leader-only region ≈ 0.023 of the
square; leader-wants-state-rejects ≈ 0.090.

## 4. Mobilization feasibility

```
M(θ) = m·(1 − 0.7·o) + 0.15·a        (dual-use/civilian slack term)
M_req(G) = 0.30 + 0.20·G
feasible ⟺ M(θ) ≥ M_req(G)
```

War does not follow from preference: a willing leader facing M < M_req
produces no pathway. Opportunity cost o is the key structural lever —
it raises both the material war cost (c_state) and the mobilization
shortfall.

## 5. Selection and pathway

```
choose W        ⟺ U_leader(W) > max_A U_leader(A)        [stage 3]
bargain fails   ~ Bernoulli(ρ)                            [stage 2]
escalates       ~ Bernoulli( k²/(k² + (1−k)²) )           [stage 5]
war pathway     = bargain_fail ∧ leader_wants ∧ feasible ∧ escalates
```

Hence P(war) = ρ · P(leader_wants) · P(feasible | ·) · p_esc(k) under the
independence approximation used in the Monte Carlo — the multiplicative
structure that makes distributed interventions compound.

## 6. Where nonlinearity is justified (and only there)

- Escalation: k-shaped response k²/(k²+(1−k)²) — threshold-like transition
  justified by retaliation feedback (Jervis system effects), NOT introduced
  for mathematical color.
- Cascade adoption on networks (see 09): threshold rule, the minimal
  nonlinear propagation mechanism.
- Everything else is linear: preference formation is deliberately linear
  so that *where* nonlinearity lives is transparent.

## 7. Non-deliverables (explicitly out of scope)

No explicit Bayesian learning machinery (folded into ρ and σ), no dynamic
commitment problem (folded into α and ρ), no geography, no arms-race
dynamics. Each is a stated omission for the minimal model; extensions
must justify added complexity by falsifiable content.
