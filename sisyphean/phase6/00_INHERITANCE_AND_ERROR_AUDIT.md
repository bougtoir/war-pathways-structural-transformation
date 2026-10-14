# 00 — Inheritance and Error Audit (Gate 0)

Inputs actually read: `sisyphean/phase5/` docs 00–18 (unzipped in-tree),
`phase5/code/model5.py`, `phase5/code/experiments5.py`,
`phase5/code/results/*.csv`, Phase-4 docs as needed. No Phase-5 file
was overwritten.

## Claim → equation → code trace

| Phase-5 claim | equation | code location | audit verdict |
|---|---|---|---|
| "coercion of consent-dependent value is self-undermining" | π = r·α(L,q)·V(L) − c1r − c2r² | `model5.payoff` | equation OK; inference flawed |
| old T-1: sign flip across asset mix | `r·w_c·|dL/dr|·V̄ > w_phys·V̄ − c1 − 2c2r` | doc 06 | **erroneous** — see below |
| α decomposition | α = w_phys + w_hum·L + w_inst·L·q + w_net·L² | `model5.alpha` | valid as a decomposition; weights still exogenous |
| exit on "unprofitable" | net < −0.3 threshold | `simulate5` | arbitrary threshold, undocumented bound |
| asset-mix table (g23) | — | `gate23_theorem_sweep` | reproduces; interpretation exceeds theorem |

## The precise error in old T-1

The condition compared a **derivative-weighted** term
(r·w_c·|dL/dr|·V̄) against a **level** term to conclude "long-run
realizable value declines below zero." Two conflations:

1. **Marginal vs level**: a negative ∂π/∂r (or dπ/dr along L*(r)) does
   not imply π < 0 — π can fall while remaining strictly positive. The
   correct abandonment condition is the *level* α(L∞,q)V(L∞) <
   c1 + c2·r (Gate 1, doc 01).
2. **Derivative-of-what**: |dL/dr| (response of state to intensity) was
   multiplied into a marginal-payoff expression as if it were dπ/dr;
   time derivative dπ/dt and intensity derivative dπ/dr were not
   distinguished.

## Unstated assumptions now made explicit

- V treated as a flow; earlier text called it "value" ambiguously
  (stock vs flow now fixed, doc 01).
- r bounded in [0, r_max] with r_max = 1 — intensity, not probability.
- q exogenous in Phase 5; now noted as an assumption (doc 04).
- exit threshold "net < −0.3" was an undocumented boundary condition —
  replaced by the analytic level condition.
- w-weights were static; Phase-6 doc 04 endogenizes them.
- no discounting/horizon declared; repaired propositions declare both.
- r=0: π(0,L) = 0 identically — strictly negative payoff is impossible
  there; old text implied it.
