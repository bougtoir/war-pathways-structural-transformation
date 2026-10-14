# 11 — Empirical Feasibility

Assessment of public datasets for *future* testing. No large datasets
downloaded (per instructions); this is a feasibility mapping only.
Observational associations do not establish causality — stated once and
held throughout.

## Dataset assessment

| dataset | variables | coverage | access/license | missingness | causal-inference suitability |
|---|---|---|---|---|---|
| **UCDP** (Ged/Gleditsch) | conflict onset, intensity, termination, type (state/non-state/one-sided) | 1946– | free, CC-BY-like terms | low for state-based; thin for sub-threshold violence | medium — supports duration/recurrence models for stage 5–6 |
| **ACLED** | event-level political violence, protests, actors | 1997– global (depth varies by region) | free registration, non-commercial | reporting bias by country; media-source dependence | medium — high resolution but endogenous coverage |
| **Correlates of War** (NMC, MID, alliances) | capabilities (CINC), militarized disputes, formal alliances | 1816– | public | MID threshold excludes low-level coercion | medium-high for stage 4 (capability, mobilization proxies) |
| **SIPRI** | military expenditure, arms transfers, industry | 1949/1988– | free public use with citation | estimates for closed states | high for stage-4 mobilization-cost proxy |
| **World Bank WDI** | GDP/capita, trade, fiscal capacity, labor | 1960– | CC-BY-4.0 | thin for fragile states (exactly the cases needed) | high as covariates; low as instruments |
| **V-Dem** | institutional indices: accountability, executive constraints, regime type | 1789– | free, CC-BY-SA | expert-coding measurement error | high for stage-3 divergence δ proxies (accountability indices) |
| **Archigos** | leader entry/exit, manner of removal | 1875–2015 | public (Goemans et al.) | irregular regime coding | medium for leader-level survival analysis (lam proxy) |
| **Trade datasets** (UN Comtrade / COW trade / CEPII BACI) | bilateral trade flows | varies | public | re-export distortions | medium for stabilizing-edge construction (stage 5/network) |

## Which mechanisms are testable — and how

| mechanism | proxy design | testable? |
|---|---|---|
| B opportunity cost at mobilization gate | military personnel share or mobilization duration vs civilian wage/development level; conditional on dispute onset | **partially** — selection into disputes is endogenous; need dispute-conditional samples |
| C alignment (δ) | V-Dem accountability × leader-level war initiation × outcome-by-regime interactions | partially — δ is a latent construct, not an index; measurement model needed |
| Escalation amplification k | dispute→war transition probability vs alliance/territorial contiguity structure | partially — Holsti-type widening data exist |
| War-rationality region size | not directly observable — only *choices* are; bounds via choice-based partial identification | **weakly** — flagged UNSUPPORTED as direct measurement |
| Stabilizing-edge share | trade/GDP-weighted dependency vs alliance-commitment structure predicting third-party joining | partially — network construction is under-identified |
| Evolutionary stability | no direct test; comparative case evidence of regime persistence through leader change | conceptual only |

## Which remain conceptual

- R-region *size* (defined metric, unobserved beliefs).
- Long-run durability of substitution (requires post-transformation
  counterfactuals).
- System adaptation stage as measurable object.

## Feasibility verdict

A reduced-form test program is feasible for mechanisms B, C-proxy, and
escalation gating — a UCDP/COW + V-Dem + SIPRI + Archigos merge with
dispute-conditional samples. The framework's *integrated* claims
(multiplicative gates, region shrinkage) are not directly testable with
public data; the honest empirical strategy is gate-by-gate estimation,
not joint validation.
