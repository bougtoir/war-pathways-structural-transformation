# 12 — Adversarial Theoretical Review

Hostile review of the framework. Each criticism: severity (H/M/L),
supporting literature, possible response, remaining limitation.
No conclusion is forced.

**Q1. Is this merely a restatement of rationalist war theory?**
- Severity: **H** — the most dangerous objection.
- Literature: Fearon 1995; Powell 2006; Lake & Powell 1999.
- Response: three additions are not restatements — (i) actor-split
  utilities with quantified leader-only region; (ii) mobilization as a
  probabilistic gate rather than an assumption; (iii) durability analyzed
  as a stability property of structure. Each is testable independently
  of the rationalist core.
- Remaining limitation: the *foundation* is still expected-utility
  comparison; "rationality-independence" holds only at the system level
  (network/EGT components), not at the selection stage, which still
  compares U_W vs U_A. The claim must be stated precisely: independence
  from *state-level* rationality, not from preference comparisons per se.

**Q2. Isn't structural substitution just commercial peace theory?**
- Severity: **M**.
- Literature: Gartzke 2007; Russett & Oneal 2001.
- Response: commercial peace asserts a correlation; this framework
  locates the mechanism at specific gates (opportunity cost binds at
  mobilization, not selection — visible in the simulation where B moves
  feasibility, not willingness) and predicts *where* it fails (when
  δ-driven leader preferences dominate).
- Remaining limitation: the added value is diagnostic structure, not a
  new mechanism. Fair hit.

**Q3. Does the model assume rationality despite claiming independence?**
- Severity: **H**.
- Literature: bounded-rationality critiques; bureaucratic politics
  (Allison).
- Response: the only "rational" step is stage-3 comparison, applied to
  the *leader* — i.e., rationality is localized to the actor where it is
  empirically most defensible (survival-seeking), while beliefs are noisy
  (σ) and the other stages are structural/adaptive. The model tolerates
  irrational initiation through the misperception channel (p_war can be
  positive outside R_leader — p_war_misperceived is computed).
- Remaining limitation: the comparison structure itself is still a
  maximization metaphor. An organizationally-driven selection stage
  (garbage-can/bureaucratic) is not implemented. Downgrade claim from
  "rationality-independent" to "state-rationality-independent".

**Q4. Can leaders initiate war despite negative national utility?**
- Severity: n/a (affirming).
- Literature: BdM & Siverson 1995; Chiozza & Goemans 2011.
- Response: yes — this is exactly the leader-only region (≈9% of (G,p)
  space at baseline). The framework *predicts* such wars and treats them
  as the central pathology.

**Q5. Can military aggression be intrinsically valued?**
- Severity: **M**.
- Literature: honor/status seeking (Lebow); militarism.
- Response: an intrinsic-war term can be added to U_W^leader; the gate
  structure is agnostic about the utility's origin. It doesn't change the
  architecture — intrinsic value enlarges R_leader, gates 4–6 unchanged.
- Limitation: no micro-foundation for intrinsic value provided.

**Q6. Can resource competition increase rather than decrease conflict?**
- Severity: **M**.
- Literature: resource curse; scarcity-conflict links.
- Response: yes — o is not globally pacifying; where resources are the
  stake, higher civilian returns can raise the value of capture. The
  model's c_state assumes war costs scale with o; a zero-sum resource
  setting needs an added capture term. Scope condition: mechanism B
  applies to labor/capital opportunity costs, not lootable-resource
  economies.
- Limitation: scope condition is stipulated, not derived.

**Q7. Can civilian technological development strengthen military
capabilities?**
- Severity: **H for mechanism C**.
- Literature: dual-use ambiguity; spin-ons vs spin-offs.
- Response: agreed — this is why C is marked fragile in §07. The model
  treats dual-use as adding +0.15a to mobilization slack *and* raising o;
  the sign of the net effect is genuinely ambiguous and parameter-
  dependent.
- Limitation: the ambiguity is resolved by a sign choice, not derived.

**Q8. Can institutional integration create new vulnerabilities?**
- Severity: **M**.
- Literature: dependence-as-vulnerability (Hirschman); weaponized
  interdependence (Farrell & Newman).
- Response: yes — stabilizing edges can be coercively weaponized; the
  network model's τ_i assumes stabilizing ties remain stabilizing. A
  hostile-actor extension should let edge type switch under adversarial
  control.
- Limitation: static edge types — real vulnerability is dynamic.

**Q9. Can aggressive actors exploit nonviolent institutional structures?**
- Severity: **H**.
- Literature: spoiler problems (Stedman); exploitation of open systems.
- Response: modeled directly — the `exploit` parameter and the invasion
  analysis. Result: at exploit=0.70 no pure-strategy peace is an ESS; a
  nonviolent structure that fully disarms fails. The framework's answer
  is therefore not "substitute everything" but "substitution must retain
  a defense payoff" (S keeps 0.15 vs W).
- Limitation: the defense floor is asserted in the payoff, not derived
  from a deterrence model.

**Q10. Can war-rationality regions be meaningfully measured?**
- Severity: **M–H**.
- Response: |R| is defined as area over (G,p) with subjective utilities;
  beliefs are unobserved, so only revealed-choice bounds are estimable
  (partial-identification logic). Stated as UNSUPPORTED for direct
  measurement in §04 and §11 — this is the framework's weakest
  operational link.
- Limitation: an unmeasurable construct risks non-falsifiability —
  mitigated by tying claims to gate-level passage probabilities instead.

**Q11. Does the framework predict anything existing theories do not?**
- Severity: **H**.
- Response: falsifiable-type predictions produced: (i) opportunity-cost
  interventions reduce *mobilization-success conditional on dispute
  onset* more than *dispute onset itself* (stage-specificity); (ii) the
  leader-state agency gap predicts a distinct class of wars (wars
  initiated where material calculus rejects); (iii) connectivity-conflict
  relation is non-monotone and edge-type-dependent (z≈4 peak).
- Limitation: (i)–(iii) are comparative predictions *within* the model;
  empirical discriminating power vs. selectorate or steps-to-war accounts
  is untested.

**Q12. Falsifiable hypotheses?**
- Severity: **M**.
- Response: gate-level passage probabilities are estimable objects
  (§11): the model can be *wrong* about which stage an intervention
  binds. The integrated claim (multiplicative gates) is falsifiable via
  interaction tests.
- Limitation: the fully integrated structure is not.

**Q13. Does transformation merely relocate violence to another level?**
- Severity: **H**.
- Literature: van Creveld 1991; Kaldor's new wars.
- Response: this is the deepest objection and the framework accepts it
  as a scope condition: the model addresses *organized interstate mass
  violence*. Substitution that displaces violence into civil, proxy, or
  criminal channels is not a victory condition here — the architecture
  requires tracking violence at each level, and §04/§07 mark
  relocation-susceptible mechanisms explicitly.
- Limitation: no substate violence module; the most important failure
  mode is unmodeled.

**Q14. Is claimed durability realistic?**
- Severity: **M**.
- Response: the evolutionary analysis says conditional — durability
  requires the substitution premium + enforcement floor to exceed the
  exploitation wedge *across* leadership changes and shocks. Nothing in
  the framework warrants "permanent obsolescence"; the claim is
  "shrinkable and stabilizable", not "eliminable".
- Limitation: parameter values for real societies unknown.

**Q15. Does it confuse descriptive stability with ethical desirability?**
- Severity: **M**.
- Response: a stable nonviolent structure can be stable *because* it
  entrenches other exploitation (colonial "peace", frozen injustice).
  The framework is descriptive — it defines stability of pathway
  structure, not its justice.
- Limitation: normative evaluation explicitly out of scope; flagged so
  the model is never read as endorsement of any stable order.

## Overall verdict of the hostile review

The framework survives with **three mandatory concessions**: (1) retitle
the claim from "rationality-independent" to "state-rationality-
independent"; (2) treat obsolescence as scoped to interstate organized
violence with explicit relocation-tracking; (3) concede that |R|
measurement is construct-level, not observable. These do not kill the
project but bound it.
