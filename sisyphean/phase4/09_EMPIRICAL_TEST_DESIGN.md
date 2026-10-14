# 09 — Empirical Test Design (Gate 39)

ONE mechanism-level design. Latent variables' observability honestly
assessed; nothing downloaded; no fabricated findings.

## Design: sponsor-withdrawal duration test

- **Outcome**: conflict duration (dyadic-year cessation indicator).
- **Event/exposure**: patron-side externality shock — domestic
  sanctions vote, embargo decision, or public opinion collapse in the
  patron country (timing from event databases / GDELT-adjacent public
  records).
- **Key predictor**: pre-war sponsor flow exposure (SIPRI arms-transfer
  TIV dependence ratio) — high-dependence belligerents should exit
  sooner post-shock.
- **Controls**: battle deaths (COW), regime type (V-Dem), conflict type,
  GDP, duration dependence (piecewise hazard).
- **Identification assumption**: patron shocks are orthogonal to
  belligerent battlefield state (instrument via patron domestic events
  — elections, budget crises). Selection: sponsors pick strong clients —
  model via exposure heterogeneity, not randomization.
- **Missingness**: covert transfers unobserved — falsifies the design
  only where inflow measurement fails; restrict to well-instrumented
  cases and state the truncation.
- **Negative controls**: conflicts without any identified patron —
  predicted null effect of patron-side shocks.
- **Competing hypotheses**: (a) generic attrition — predicts duration
  tracks deaths/reserves, not sponsor events; (b) war-economy — predicts
  no response when profits fund substitution; (c) war-weariness —
  predicts duration-driven exit independent of shocks.

## Observability verdict

Goal attainability (V_G) is **not observable** with available data;
sponsor tolerance partially is (through exit events + flow records).
The design therefore tests Channel B only — Channel A's hollow-war
signature cannot be validated empirically now; stated as such.

## Accessible sources (public, lawful)

UCDP (conflict/duration, non-state violence for displacement),
SIPRI TIV (flows), V-Dem (regime/consent proxies), COW (battle deaths),
ATOP (alliance formalization). Licensing: all public research datasets;
terms require citation, non-commercial use ok.
