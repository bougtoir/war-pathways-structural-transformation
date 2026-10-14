# 09 — Complex Systems Model

Minimal network model (`code/network_model.py`): Watts-type threshold
cascade on Erdős–Rényi graphs, n=400, with two edge types.

## Setup

- Nodes: states/political actors.
- Edges: mixed — each node i has a stabilizing-edge share s_i ∈ [0,1]
  (economic dependencies, institutional ties) vs destabilizing edges
  (security commitments, transmission pathways).
the fraction of *destabilizing* neighbors in conflict ≥ τ_i =
  0.25 + 0.45·s_i. Stabilizing ties raise the threshold and do not
  transmit — connectivity spreads conflict only through destabilizing
  channels; its effect depends on edge type.
- Seed: ~1% exogenous conflict onset (2% for the shock test).

## Results (results/network_cascade.csv; 30 reps per cell)

Cascade share by mean degree z and stabilizing fraction s̄:

| z | s̄=0.0 | s̄=0.2 | s̄=0.4 | s̄=0.6 | s̄=0.8 |
|---|---|---|---|---|---|
| 2 | .767 | .057 | .022 | .015 | .012 |
| 4 | .917 | .028 | .015 | .013 | .011 |
| 6 | .059 | .018 | .013 | .011 | .010 |
| 8+ | ≤.015 | — all ≈.01 | | | |

(z=6, s̄=0 is bimodal: most runs die early, a minority produces large
cascades — mean .059 with p90 .044.)
Shock test (5% seed, z=6): cascade 0.998 with s̄=0 → 0.055 with s̄=0.6.

## Substantive findings beyond established network models

1. **Non-monotone connectivity effect.** With s̄=0, the largest cascades
   occur at *low* degree (z=2–4: 0.74–0.95), not high — in threshold
   cascades, sparse neighborhoods convert a small number of active
   neighbors into a high *fraction*, so peripheral nodes are easier to
   tip. Dense networks are self-buffering under this rule. This is a
   known property of Watts models but counter to the informal
   "interdependence spreads war" intuition and worth restating.
2. **Edge type dominates topology.** A 20% stabilizing share collapses
   the cascade by ~97% at z=4 — the *composition* of ties matters more
   than their density. Policy translation: the same trade/alliance
   network transmits or blocks escalation depending on what the edges
   carry.
3. **Resilience is structural, not behavioral.** s̄=0.6 absorbs a 5%
   exogenous shock (0.057 residual) without any node "choosing" peace —
   the property is in the tie structure, matching the framework's
   rationality-independence requirement.
4. **No new mechanism claimed.** These are standard cascade phenomena;
   the marginal contribution is plugging node thresholds into the
   stage-5 escalation parameterization and tying them to stabilizing
   vs. destabilizing edge semantics — i.e., an integration, not a new
   network result (flagged for the hostile review, Q11).

## Limits

ER graphs ignore clustering/hierarchy of real alliance-trade networks;
fixed thresholds; no edge dynamics; cascade ≠ mobilization capacity —
a node "in conflict" here abstracts stages 3–5. Extensions (multiplex
ties, strategic rewiring) require justification before adding.
