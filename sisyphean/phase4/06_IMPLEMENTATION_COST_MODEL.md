# 06 — Implementation Cost Model (Gate 36, EXPLORATORY)

Symbolic + illustrative grid. Output: `results/g36_cost.csv`.
**1,000 trillion JPY is a sensitivity anchor, not an estimate.**

## Accounting

Net = NPV(avoided harm) − I − maintenance, with
NPV = Σ_t avoided/(1+disc)^t, maintenance = 2%·I/period-equivalent.

| disc | T | avoided/yr (T JPY) | NPV | net |
|------|---|--------------------|-----|-----|
| 3% | 100 | 0.5 | 15.8 | −1,004 |
| 3% | 100 | 2.0 | 63.2 | −957 |
| 3% | 100 | 8.0 | 252.8 | −767 |
| 1% | 100 | 8.0 | 504.2 | −516 |

**Every tested cell is net-negative at the anchor.** Break-even requires
avoided harm ≳ 30–60 T JPY/yr for a century, or I ≪ anchor — reported as
sensitivity structure, not affordability verdict. Nothing estimated
from thin air: avoided-harm values are hypothetical sweep points.

## Incidence & feasibility distinctions

- Technical feasibility ≠ positive net benefit ≠ political financing:
  separated explicitly. Winners: civilians in conflict zones, future
  generations. Payers: current funders; losers: war-economy
  beneficiaries and sponsors (whose resistance is endogenous — free
  riding and institutional capture noted, not solved).
- Non-convexity: a threshold benefit function is a hypothesis, not a
  fact; global implementation decisions are nonconvex, marginal
  analysis insufficient — stated.
- Non-monetizable constraints: rights and legitimate self-defense are
  kept outside the JPY accounting — they bind the mechanism's form, not
  its price.
