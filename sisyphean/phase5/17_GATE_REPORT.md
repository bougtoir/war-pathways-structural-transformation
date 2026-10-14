# 17 — Gate Report (Phase 5, Gates 0–11)

| gate | requirement | verdict | evidence |
|---|---|---|---|
| 0 closest literature | 10–15 verified full-text studies, matrix | **PASS** | 14 studies, 13 DOI-verified (Crossref), matrix xlsx; Liberman/Grossman-Kim/KCA/Hart-Moore etc. |
| 1 mechanism inventory | conditions, costs, counterexamples, renaming check | **PASS** | 04_MECHANISM_MAP — 7 mechanisms, honest renaming flags |
| 2 minimal formal model | derived α, no assumed monotonicity, actor-specific objectives | **PASS** | model5.py + doc 05; ∂A/∂r emergent, sign flips by mix |
| 3 theorem/impossibility | bounded proposition + counterexample | **CONDITIONAL PASS** | doc 06: T-1 verified numerically; proof is sketch-level; counterexample (physical assets) reproduces Liberman |
| 4 war as special case | map to onset/sustainment/sponsors/termination; nonrational actors | **PASS** | doc 08; Phase-4 negatives preserved |
| 5 fair rivals | equal-complexity rivals, distinguishing implication | **PASS (one survives)** | g5_rivals: onset-count effect only; no unique timing signature |
| 6 operationalization | honest latent→observable table | **PASS with negative finding** | audit xlsx: α not measurable publicly |
| 7 pilot | only if measurement passes | **NO-GO (explicit)** | doc 11: feasibility audit only, Design B specified |
| 8 computational model | success AND failure regions | **PASS** | g8 csvs; sponsor-failure region dominant |
| 9 implementation econ | secondary, anchor sensitivity | **PASS (exploratory)** | doc 13; all-anchor net-negative preserved |
| 10 discussion boundaries | philosophy quarantined; JME separation | **PASS** | doc 14, doc 15 audit |
| 11 hostile review | fatal vs remediable split | **PASS** | doc 16 |

## Hard-stop check (all clear)

- unverified novelty? no (02)
- circular theorem? no (06: conclusion isn't a restated monotonicity)
- no distinguishable implication? one survives (07)
- invalid proxies presented as measurements? no (11 is NO-GO, not a
  dressed-up result)
- civilian destruction counted as success? no (h always a cost)
- displacement ignored? no (state variable, Phase-4 convention)
- JME duplication? no (15)

## Decision

**CONDITIONAL GO** — bounded synthesis continuation only; see doc 18.
