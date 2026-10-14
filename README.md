# Structural Transformation of War Pathways

Theory-development research package (not a manuscript). Tests whether a
falsifiable framework can be built for the structural obsolescence of
war without assuming rational or benevolent actors.

## Contents

- `01_EXECUTIVE_SUMMARY.md` … `14_RESEARCH_DECISION.md` — staged research
  deliverables (literature → model → simulation → hostile review → gates).
- `03_CLOSEST_PRIOR_STUDIES.xlsx` — 23 verified closest prior studies
  (Crossref-verified DOIs).
- `code/` — illustrative simulation suite (bargaining model, evolutionary
  stability, network cascade, figures, xlsx generator).
- `code/results/` — generated CSVs and figures.

## Run

```bash
cd code
pip install -r ../requirements.txt
python run_all.py                 # all results into results/
python make_prior_studies_xlsx.py # rebuild ../03_CLOSEST_PRIOR_STUDIES.xlsx
```

All simulations are explicitly illustrative (arbitrary parameterization,
seeded RNG, no historical calibration, no proprietary data).

## Decision

CONDITIONAL GO — see `14_RESEARCH_DECISION.md`.
