# 10 — Empirical Design (Gate 6–7 setup)

The measurement audit (09_*.xlsx) concludes: no public dataset directly
measures appropriability, consent, objective attainment, or political
value. Two designs are specified; only the second is feasible now.

## Design A (primary, deferred): occupation appropriability test

- Question: does coercion of consent-dependent value yield less
  realizable gain than coercion of physical assets?
- Would need: original coding of post-conquest extraction vs target
  asset mix (skilled-labor share, network density, institutional
  legibility) — no existing dataset codes "appropriability."
- Status: **deferred — requires original coding**; defined here only so
  the next phase knows what to collect.

## Design B (feasible now): sponsor-externality duration test

Carried over from Phase 4 Gate 39 — unchanged, still the single
implementable design.

- Unit: dyadic conflict episode (UCDP armed-conflict dataset).
- Outcome: duration/cessation hazard.
- Exposure: pre-war SIPRI TIV dependence of the belligerent on the
  patron; patron-side externality shocks (sanctions votes, embargoes)
  as quasi-exogenous events.
- Controls: COW battle deaths, V-Dem regime, GDP, duration dependence.
- Identification: patron domestic events as instruments; selection via
  exposure heterogeneity, not randomization; covert-transfer
  missingness truncates the sample (stated).
- Negative control: no-patron conflicts → null predicted.
- Rivals: attrition (duration ~ deaths), war economy (no response to
  patron shocks), war-weariness (duration-only).
- Labels: association unless the instrument holds — stated pre-analysis.

## Temporal ordering & inclusion

Only conflicts with an identified external sponsor and ≥3 pre-war
SIPRI observations; patron shock must post-date onset by ≥1 year
(rules out anticipation). Conflicts ending <2 periods after shock
excluded from the principal hazard estimate (left-censoring note).
