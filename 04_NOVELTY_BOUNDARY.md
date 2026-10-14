# 04 — Novelty Boundary

Method: each candidate contribution was checked against the 23 closest prior
studies in `03_CLOSEST_PRIOR_STUDIES.xlsx` (bibliography verified via
Crossref, 2026-10-14). Classification: ALREADY ESTABLISHED / PARTIALLY
ESTABLISHED / POTENTIALLY NOVEL / UNSUPPORTED.

## Contribution-by-contribution

### C1. War as a conjunctive pathway: willing AND feasible AND escalates

Separating initiation (preference) from mobilization (capacity) from
escalation (dynamics).

- Senese & Vasquez (2008) already model war as a *sequence of steps*;
  steps-to-war is the direct ancestor. — largely descriptive/empirical.
- Slantchev (2003) and the bargaining school treat the war option as
  always-feasible background.
- No prior study we identified *formalizes* mobilization feasibility as an
  independent probabilistic gate whose parameters are policy-intervenable
  (opportunity cost, dual-use value, fiscal depth).

**Classification: PARTIALLY ESTABLISHED** — the staged intuition exists;
the formal gated decomposition with intervenable stage parameters is the
defensible increment.

### C2. Actor-divergent war-rationality regions R_state ≠ R_regime ≠ R_leader ≠ R_population

- Selectorate theory (BdM et al. 2003; BdM & Siverson 1995; Weeks 2014;
  Chiozza & Goemans 2011) establishes *that* leader and national incentives
  diverge.
- War and Reason (BdM & Lalman 1992) formalizes two-level incentives.
- What none does: define per-actor *regions* in stake × capability space as
  measurable objects, quantify the leader-only region (the "agency gap"),
  and treat the divergence `delta` as itself an intervention target.

**Classification: PARTIALLY ESTABLISHED** — mechanism established, the
region-measurement formalization is the increment. In our illustrative
parameterization, R_leader (9.3%) exceeds R_state (0.3%) by ~9 points of
(G,p) space — a quantifiable "wars the leader wants that the state would
reject" region.

### C3. Multiplicative intervention structure

If war requires passing multiple gates, interventions at different stages
compound (p_war ≈ product of gate passage probabilities), so partial
improvements at several weak points can outperform a strong improvement at
one. The simulation suite shows combined interventions (E) driving pathway
probability to ≈0 where single interventions leave 0.2–1.4%.

- Implied by but never stated in the staged/steps literature; Russett &
  Oneal's Kantian "tripod" is additive, not gated.

**Classification: POTENTIALLY NOVEL** as an explicit formal claim; easily
stated, but we found no prior articulation as a design principle.

### C4. War-rationality region can expand again after shocks; durability as a distinct property

- Fortna (2004/2008) studies peace durability empirically; Kydd (2005)
  studies trust restoration. Neither defines durability of the *structural
  region* itself (resilience vs. recovery vs. ESS-like stability are
  distinguished here).

**Classification: PARTIALLY ESTABLISHED.**

### C5. Structural obsolescence thesis (war becoming ineffective/unnecessary)

- Mueller (1989/1991) asserts obsolescence without mechanism; van Creveld
  (1991) and Kaldor (1999/2005) argue transformation displaces rather than
  eliminates violence; Gartzke (2007) gives the opportunity-cost mechanism
  correlational support; Pinker (2011) documents decline descriptively.

**Classification: ALREADY ESTABLISHED** as a claim. This project does NOT
claim the thesis itself; it claims a testable mechanism for it (and for its
failure). Treating the thesis as a *question* with gate-level answers is the
increment — honest framing: the contribution is a framework, not the thesis.

### C6. Substitution of military force by nonviolent alternatives

- Commercial/capitalist peace (mechanism B is Gartzke's channel);
  functional alternatives discussed in institutional peace literature;
  Fearon & Laitin (1996) for decentralized institutional substitutes.

**Classification: ALREADY ESTABLISHED to PARTIALLY ESTABLISHED.** Our
increment: locating *which gate* each substitution mechanism binds (e.g.,
opportunity cost binds at mobilization, not at selection — the simulation
shows B reduces feasibility while leader preference barely moves).

### C7. EGT stability of nonviolent structures under invasion and shocks

- Skyrms (2004) on stag-hunt stability; Cederman (2001) Kantian-system ABM.
- The specific finding that S can be an ESS with a large basin yet remain
  non-ESS under high-exploitation parameters — a *conditional stability*
  result — is a direct consequence of the payoff structure, not a novel
  theorem.

**Classification: PARTIALLY ESTABLISHED.**

### C8. Empirical measurement of the war-rationality region

No established operationalization exists. Our measure (area over (G,p)
space) is a *defined* metric; whether it can be estimated from observables
is open (see 11_EMPIRICAL_FEASIBILITY.md — likely only proxies).

**Classification: POTENTIALLY NOVEL as a metric; UNSUPPORTED as a claim of
measurability** — flagged honestly.

## Verdict

No single component is novel. The defensible independent contribution is
the **integration**: an actor-split, gate-structured pathway in which (i)
each gate has distinct structural parameters, (ii) interventions are
multiplicative across gates, and (iii) durability is analyzed as a
stability property of the structure rather than of preferences. This is
PARTIALLY ESTABLISHED bordering on POTENTIALLY NOVEL — sufficient for
CONDITIONAL GO, not for claims of a new theory.
