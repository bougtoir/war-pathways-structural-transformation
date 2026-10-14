# 00 — Source Integrity Audit (Gate 0)

Independent re-audit of `sisyphean/phase6/` (docs 00–17, code, results).
Nothing in Phase 6 was edited; this phase re-derives every claim.

## Claim-to-evidence matrix

| Phase-6 claim | where | classification |
|---|---|---|
| π = r·αV − c1r − c2r² definitions | model6.py | PROVEN (consistent) |
| π<0 ⟺ αV < c1+c2r (r>0) | doc 01 P1 | **PROVEN** — sympy re-derived (π/r = αV − c1 − c2r) |
| no derivative implies level (P3) | doc 01/02 | PROVEN — independently re-argued + numeric: P(∂π/∂r<0 ∧ π>0)=0.157 |
| w*_phys threshold (P2) | doc 01 | **INCORRECT as printed** — extra r in denominator; code used correct form. Corrected formula in doc 02 |
| w-weights vary freely | c3 grid | **flaw** — simplex constraint Σw=1 never imposed in Phase 6; under Σw=1, α(L=1,q)=1 identically → new feasibility bound |
| abandonment at π∞<0 "in finite time" | doc 01 P1 | CONDITIONAL — holds only with (i) strict LVL, (ii) monotone αV path, (iii) payoff-comparing decision rule; doc 01 |
| α = Σ components | model6 | ASSUMED — decomposition is a parametrization, not derived from microfoundations |
| behavior spec flips theorem sign | c3 | NUMERICALLY SUPPORTED (real sensitivity, not error) |
| fear-driven compliance possible | c4 | NUMERICALLY SUPPORTED |
| two stable regimes | c6 | NUMERICALLY SUPPORTED |
| α unmeasurable → empirical NO-GO | docs 08–12 | PROVEN as audit conclusion |
| one discriminating prediction | docs 07/17 | CONDITIONAL — survives only in consent-dominated region (doc 08) |
| "rationality-independence" wording | Phase-5 text, persisted implicitly | **UNSUPPORTED** — fails for intrinsic/regime_survival; must be dropped |

## What this audit adds

- A real defect: P2's printed threshold carries a superfluous r; the
  implied boundary is otherwise correct.
- A missing constraint: the simplex on w was never stated; imposing it
  yields α(L=1)=1 → if V(1) < c1+c2r, NO asset mix makes coercion
  unprofitable at full cooperation — the non-appropriability region is
  bounded by construction.
- The r-dependence of w*_phys was omitted from P6.
