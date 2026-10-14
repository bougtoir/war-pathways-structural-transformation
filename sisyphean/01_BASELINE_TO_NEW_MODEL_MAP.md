# 01 — Baseline Audit and Baseline→New Model Map

Baseline = parent directory `../` (STRUCTURAL_WAR_TRANSFORMATION package,
PR branch `devin/1791969113-war-pathways`). Baseline simulations re-ran
cleanly: `python3 code/bargaining_model.py` reproduces p_war=0.025
baseline, R_leader=0.093, R_state=0.003, leader-only=0.023
(identical to committed CSVs; seeds hold).

## Retained components

| baseline component | disposition in the new model |
|---|---|
| Gated pathway (willing ∧ feasible ∧ escalate) | retained as the *onset* architecture; onset is now one event among W-set, persistence, relapse |
| Actor-split utilities (state/regime/leader/population) | retained; augmented by a *non-maximizing* selection stage (Gate 15) |
| Divergence δ, diversion div, removal exposure lam | retained as parameters of aggressor selection |
| Mobilization feasibility M(θ) vs M_req(G) | retained; now feeds the keystone K (K is the *sustainment* capacity, distinct from one-shot feasibility) |
| Escalation amplification k | retained inside the in-war intensity process c(t) |
| Stabilizing/destabilizing network ties | retained and extended: ties can *switch type* after onset (Gate 16) |
| Numbered deliverable structure, hostile review, gates | retained |

## Unresolved issues carried from baseline (fixed or explicitly deferred)

| baseline issue | handling in this phase |
|---|---|
| Stage-3 selection is still expected-utility maximization | Gate 15: replaced/augmented with noisy-threshold, aspiration, and bureaucratic-routine rules; rationality claim now bounded |
| Dual-use sign ambiguity (mechanism C) | Gate 16: two opposing channels modeled; reversal region reported, no stipulated sign |
| S non-ESS under high exploitation | Gate 12/13: reframed — the claim is not equilibrium peace but *self-undermining* of sustained aggression; invasion pressure is a modeled stressor |
| |R| not directly measurable | unchanged concession; empirical bridge uses only gate-level observables (11_EMPIRICAL_TEST_DESIGN) |
| No relocation/displacement tracking | added explicitly: displacement into proxy/civil channels counted as failure, not success (Gate 13) |
| Defensive war conflated with aggression | asymmetric actor model: defender mobilization does not drain the keystone (Gate 14) |

## Components requiring revision → new model elements

| new element | motivation (gate) |
|---|---|
| state vector x=(c,m,v,K,h,d,r) with hybrid stochastic dynamics | GATE 11 reachability |
| onset event τ_w = inf{t : enters W} with barrier B | GATE 11 |
| keystone K dynamics: onset-triggered burn vs replenishment (sponsors, stockpiles, substitution, black markets) | GATE 12 |
| time-to-cessation, cumulative civilian harm ∫(1−h), relapse, oscillation metrics | GATE 13 |
| civilian functionality floor h ≥ h_min and defense floor d ≥ d_min as hard constraints; aggressor/defender asymmetry | GATE 14 |
| 4 selection rules: EU-max, noisy threshold, aspiration, bureaucratic routine | GATE 15 |
| dual-use two-channel model + weaponized-interdependence edge switching | GATE 16 |

## Mapping of the CONDITIONAL GO conditions

- "state-rationality-independent only" → enforced: Gate 15 tests whether
  conclusions survive non-maximizing rules; if not, claim is withdrawn.
- "obsolescence scoped to interstate organized mass violence" → enforced:
  displacement is a metric, not an assumption.
- "|R| construct-level" → unchanged.
