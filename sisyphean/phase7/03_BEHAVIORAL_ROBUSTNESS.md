# 03 — Behavioral Robustness (Gate 3)

Is the cooperation response genuinely endogenous? Phase-6's L* rests on
three parameters (coll_action, exit_cost, fear_gain) plus a population
update dL/dt = κ(L*−L) — endogenous in the minimal sense: the response
is generated, not hardcoded; its sign is an outcome. But the functional
form (linear L*, exponential convergence) is still assumed.

## Four specifications compared

| spec | mechanism | dL*/dr | LVL achievable? | verdict for P1 |
|---|---|---|---|---|
| A rational (opt) | coordinates withdrawal vs exit cost | <0 or ≥0 | yes when withdrawal wins | survives |
| B bounded (rule) | threshold then linear decay | <0 or 0 | marginally — floor higher | survives conditionally |
| C adaptive learning | would adjust L toward past payoff — not in code | varies | unknown | **not implemented — gap recorded** |
| D coercion-tolerant | L* = L_max | 0 | never unless w_phys small | **fails** |

## Explicit verdicts

- P1 (level → abandonment) survives only under payoff-comparing rules
  (specs A/B population + eu/noisy/aspiration coercer). It survives
  under ONE restrictive behavioral bundle; stated as such — not as a
  general result.
- Under D (tolerant populations) L never falls: LVL holds only in the
  physical corner — the mechanism is population-response-conditional.
- Adaptive learning absent from code: a population learning to comply
  would move toward D; the model's coverage of this arm is zero —
  honest gap.
- Coercion-induced compliance (fear_gain > withdrawal capacity):
  L maintained — D-like outcome from within A's machinery.
