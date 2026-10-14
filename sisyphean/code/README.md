# sisyphean/code

Hybrid stochastic model of aggressive-war onset + keystone sustainment
(Gates 11–17). Python 3.10+, numpy/pandas only.

```
pip install -r ../requirements.txt   # numpy pandas
python run_all.py                    # writes results/*.csv
```

- `model.py` — state vector, 4 selection rules (eu/noisy/aspiration/
  bureaucratic), keystone burn vs replenishment, asymmetric defender,
  civilian constraint, relapse/displacement accounting
- `experiments.py` — gate11 reachability, gate12 exit-bound check,
  gate13 relapse, gate14 civilian/defense, gate15 rules, gate16 dual-use,
  adversarial sponsor-rich failure case
- `results/` — generated CSVs (seeded; deterministic given code version)

All parameter values are ILLUSTRATIVE (theory development, not
calibration).
