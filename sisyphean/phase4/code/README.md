# phase4/code — Phase 4 audit + extensions

`pip install -r ../requirements.txt && python experiments.py` (writes results/*.csv, ~5 min)

- `model.py` — Phase-3 model + Phase-4 additions: patron exit_delay with
  streak counting, stochastic replenishment rho_sig, mis-identification
  flag p_misid, preemptive-strike counter p_preempt, persistent
  displaced-conflict STATE (disp_persist, proxy), violence_periods and
  hollow_thr metrics.
- `experiments.py` — gates 29–38 experiment functions incl. exploratory
  modules (g35 conversion, g36 cost, g37 shared-futures, g38 grid).
All parameters ILLUSTRATIVE; seeds fixed.
