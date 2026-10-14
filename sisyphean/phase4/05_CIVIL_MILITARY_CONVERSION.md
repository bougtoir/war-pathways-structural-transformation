# 05 — Civil–Military Functional Conversion (Gate 35, EXPLORATORY)

Discussion-level sensitivity module. NOT part of core results; no claim
of war obsolescence. Output: `results/g35_conversion.csv`.

## Model

net_social = 1.2·util − c_conv (benefit per converted capacity unit vs
conversion cost; retraining cost embedded in c_conv, never zero).
spill_to_mil carried as a parameter showing capacity can feed back into
military capability (opposing channel, sign not stipulated).

## Grid findings

- Conversion is net-positive only when utilization u > ~0.3 and
  c_conv < ~0.8·(1.2u): feasibility edge near u·1.2 ≈ c_conv.
- At u = 0.2 conversion is net-negative at any cost ≥ 0.1 — idle
  converted capacity is a net cost.
- spill_to_mil ≥ 0.2 does not change net_social in this accounting
  (benefits accrue where deployed) but flags the double-use risk:
  converted "civilian" capacity can re-militarize.

## Substantive notes (illustrative, not claims)

- Military expeditionary self-sufficiency (logistics, comms, field
  medicine, power, shelter, autonomous ops) maps best to disaster
  response / humanitarian relief / remote missions.
- Distinguish military-origin space tech from civilian agencies: we do
  NOT claim space exploration is primarily military — it is a boundary
  case, flagged.
- Avoided double counting: saved capacity and service benefits counted
  once via utilization.
- Governance/civilian oversight is a precondition for the civilian
  accounting to apply at all — noted as a constraint, not modeled.
