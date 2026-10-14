# phase3/code — Endogenous Keystone Model

Python 3.10+, numpy+pandas. `pip install -r ../requirements.txt && python run_all.py`

- `model.py` — separates V_G (objective efficacy), U_L (leader utility),
  m, K, rho(t) endogenous replenishment, H civilians, D defender, L consent.
  Two sponsor types (patron w/ exit-entry, balancer), substitution market,
  two non-maximizing consent rules (habitual, threshold), six leader rules.
  Channel A = consent collapse of attainable value; Channel B = endogenous
  replenishment collapse. `stepdown` param = exogenous V_G null.
- `experiments.py` — gates 19–26 experiment functions.
- `results/` — generated CSVs (seeded).
All parameters ILLUSTRATIVE; no empirical calibration claimed.
