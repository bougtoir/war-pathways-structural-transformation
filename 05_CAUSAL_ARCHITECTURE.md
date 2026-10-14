# 05 — Integrated Causal Architecture

Six analytical stages. They are *distinctions, not a fixed chronology*:
feedback loops run from stages 4–6 back to 1–3 (e.g., past mobilization
changes fiscal capacity; escalation outcomes reshape leader incentives).

## Directed causal graph

```
                 ┌──────────────── feedback ────────────────────────┐
                 │                                                  │
 (1) Conflict    (2) Bargaining   (3) Selection   (4) Mobilization  (5) Escalation   (6) System
  formation  ──▶  failure     ──▶  of force   ──▶  feasibility  ──▶ into mass     ──▶ adaptation
   [G, theta]     [rho, info]      [R_leader]       [M(theta)]        violence          [learn,
                                   ▲                  ▲                [k, net]         mutate]
                                   │                  │                                    │
                      leader utility divergence   fiscal capacity,                    institutional
                      (delta), diversion (div),   opportunity cost (o),               memory feeds
                      misperception (sigma)       dual-use value, legitimacy          back to (1)-(3)
```

Each gate emits a binary/graded passage probability; the pathway completes
only through the conjunction (gates can be re-entered — e.g., a leader who
fails to mobilize may retry after regime change).

## Stage specifications

### Stage 1 — Conflict formation
- **State variables:** stake G ∈ [0,1]; structural conditions θ
  (security dilemma severity, identity cleavage, resource scarcity).
- **Actor incentives:** all levels can generate conflict; G is exogenous
  to the choice structure here.
- **Institutional constraints:** norms, prior institutional ties.
- **Information:** distribution of G known to actors approximately.
- **Transitions:** disagreement → articulated demand (territory, policy,
  status).
- **Feedback:** unresolved stage-6 outcomes seed new G.
- **Interventions:** conflict transformation, agenda management.
- **Observable indicators:** militarized dispute onset (COW MID), UCDP
  conflict records, alliance polarization.

### Stage 2 — Bargaining failure
- **State variables:** settlement efficiency α (bargained deals deliver
  α·p·G), commitment-problem severity ρ, private-information depth.
- **Incentives:** each actor compares U_A with expected U_W.
- **Constraints:** enforcement availability (IOs, third parties), audience
  costs, indivisibility of the issue.
- **Information:** private information + misperception σ (epistemic
  failures kept distinct from structural failures).
- **Transitions:** ρ-driven exogenous collapse OR comparison-driven
  rejection.
- **Feedback:** failed bargains raise ρ in subsequent disputes.
- **Interventions:** enforcement provision (Fortna), costly reassurance
  (Kydd), issue linkage/divisibility engineering.
- **Indicators:** negotiation frequency, mediation presence (ICM data),
  alliance reliability indices.

### Stage 3 — Selection of force
- **State variables:** actor utilities U_W^a vs U_A^a; decision rests at
  leader level.
- **Incentives:** U_leader includes survival stakes (diversion `div`,
  removal exposure `lam`) and divergence `delta` from state utility.
- **Constraints:** regime institutions determine how leader utility maps
  to state action; some regimes constrain, others amplify.
- **Information:** beliefs p̂ = p + σε (bounded rationality).
- **Transitions:** choose W iff U_leader(W) > max_A U_leader(A).
- **Interventions:** accountability structures (raise lam), reduce delta,
  improve information.
- **Indicators:** leader tenure regime (Archigos), decision-system type
  (V-Dem), diversionary-conflict precursors.

### Stage 4 — Mobilization feasibility
- **State variables:** capacity M(θ) = m·(1−0.7o) + dual-use/civilian
  slack; requirement M_req(G).
- **Incentives:** military organizational incentives (budget-maximizing
  armed forces may push mobilization independently).
- **Constraints:** fiscal depth, legitimacy, civilian labor opportunity
  cost o, supply chains, war financing.
- **Transitions:** feasible iff M ≥ M_req.
- **Interventions:** civilian development raising o; dual-use conversion
  raising the civilian value of military tech; conscription/legitimacy
  institutions (in either direction).
- **Indicators:** military expenditure share (SIPRI), personnel share
  (COW NMC), fiscal capacity (tax/GDP), reserves.

### Stage 5 — Escalation into organized mass violence
- **State variables:** escalation amplification k; retaliation feedback;
  alliance/network trigger structure.
- **Transitions:** nonlinear escalation probability (k-shaped response);
  threshold cascades on the network of commitments.
- **Feedback loops:** retaliation spirals; audience costs locking in;
  sunk mobilization raising continuation incentive.
- **Interventions:** de-escalation norms, firebreak institutions, arms
  control, defensive posture distinguishability (Jervis).
- **Indicators:** conflict intensity levels (UCDP), battle deaths,
  widening (Holsti), third-party joiners (COW).

### Stage 6 — System adaptation
- **State variables:** institutional memory; strategy distribution over
  {W, B, S}; structural parameters themselves (they evolve).
- **Transitions:** adaptive selection (EGT metaphor), institutional
  learning, mutation/invasion of aggressive strategies.
- **Interventions:** peacekeeping/enforcement (Fortna), institutional
  design that survives leadership change.
- **Indicators:** peace duration, recurrence (Fortna dataset), treaty
  survival, V-Dem institutional indices.

## Required distinctions (model invariants)

- **A. Conflict exists ≠ B. bargaining fails ≠ C. force selected ≠
  D. force mobilized ≠ E. violence escalates ≠ F. violence persists.**
  Each pair can dissociate: conflict can persist with functional
  bargaining; leaders can select force they cannot mobilize; initiated
  violence can fail to escalate; escalated violence can fail to persist.
- **Actor utilities never collapse into one function:**
  state (material), regime (survival-weighted), leader (survival-sharpened),
  population (cost-bearing), military organization (resource-seeking).
- **Objective utility, subjective expected utility, and realized outcomes
  are kept separate** via the p̂ = p + σε construction and ex-post outcomes.
