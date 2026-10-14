# 03 — Formal Model (Hybrid Stochastic, Discrete Time)

## State vector

Per aggressor–defender dyad, at time t (Δt = 1 period):

| symbol | meaning | range |
|--------|---------|-------|
| q | dispute pressure (OU + jump shocks) | [0,1] |
| c | conflict intensity | [0,1] |
| m | aggressor mobilization capacity | [0,1] |
| v | political value of conquest (aggressor) | [0,1] |
| K | keystone sustainment stock for *aggressive* war | ≥0 |
| S_p | pre-war stockpile buffer feeding K | ≥0 |
| h | civilian functionality | [0,1] |
| d | defender capacity | [0,1] |

War set W = {(c ≥ C_W) ∧ war_on}, C_W = 0.5. Civilian-safe set
S = {h ≥ h_min}, h_min = 0.5.

## Selection (Gate 15 — non-maximizing rules allowed)

Four implemented rules (model.py `selection_fires`):

- **eu**: fire iff U_W > U_A (utility maximizer — reference only)
- **noisy**: fire with prob σ((U_W−U_A)/temp) (trembling / bounded)
- **aspiration**: fire iff q > asp_gap ∧ U_W > 0 (satisficing; ignores U_A)
- **bureaucratic**: fire iff m > m_routine, with error prob e_b
  (organizational routine, utility-free)

Feasibility: m ≥ m_req(v) = m_req0 + 0.1·v.
Barrier: an independent structural gate, onset succeeds only if
u ~ U(0,1) < exp(−B). Onset event E = selection ∧ feasible ∧ barrier.

## Dynamics

```
dq = −a_q·q + σ_q·ε_t + jump_t            (OU + shocks; normal or Cauchy)
m → m_target = 0.6 + spill − 0.4·o        (dual-use: cost o vs spillover)
```

In-war:
```
dK = −κ·c·m − resist_burn·d + sponsor + release
release = min(s_release, S_p);  S_p −= release
dd = d_rate·(d_max − d)·1[h > 0.6·h_min]   (defender; does NOT draw K)
dh = −harm_c·c·(1 − protect)
exit when K ≤ K_min or t_war ≥ dur_max
```

Post-war: K regrows at K_regrow (capacity rebuilding); q persists unless
decayed — relapse path remains open (Gate 13).

## Displacement

Each barrier-blocked onset attempt produces a sub-war violence event with
probability p_disp (recorded; suppressed war ≠ suppressed violence).

## Why this formalization and not an N-player game

The prompt requires results not to depend on maximization. A one-sided
state-machine model with interchangeable selection rules directly encodes
that requirement: the equilibrium concept is replaced by a *family* of
behavioral rules and the claim is evaluated over the family, not within
one rule.
