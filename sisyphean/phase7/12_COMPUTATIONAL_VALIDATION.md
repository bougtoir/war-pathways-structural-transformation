# 12 — Computational Validation (Gate 11)

`code/verify7.py` — sympy + numpy, independent reimplementation;
`results/symbolic_checks.csv`, `r7_rivals.csv`, `r9_domain.csv`.
Fixed seed (7); runtime < 30 s.

## Checks performed and outcomes

| check | method | result |
|---|---|---|
| level equivalence π<0 ⟺ αV<c1+c2r | sympy factor π/r | PROVEN |
| threshold formula corrected | symbolic solve | PROVEN — extra-r defect found in Phase-6 text |
| simplex implications | symbolic rewrite | PROVEN — α(L=1,q)=1 → V(1)<c1+c2r is a weight-free bound |
| derivative objects | symbolic diff | PROVEN — distinct |
| derivative⇒level independence | 2000-dirichlet sweep | NUMERIC — P=0.157 co-occurrence |
| finite-time abandonment | analytic bound | PROVEN conditionally (strict crossing + monotone path + rule) |
| abandonment needs rule | logic check | PROVEN — no payoff comparison → no abandonment |
| rivals R1–R4 | matched calibration | NUMERIC — all rivals pay at V̄=1; discriminating only in consent region |
| domain map | (w_phys × L) grid | NUMERIC — boundary w*_phys(L) decreasing in L; L is two-sided |

## Things verified NOT to hold

- No weight-free non-appropriability region at L=1 unless costs exceed
  full realized value.
- No general abandonment theorem — needs rule class.
- No r-independent threshold.

Honesty clause honored: nothing was hardcoded to expected conclusions;
the script's checks are logic/symbolic, not fitted.
