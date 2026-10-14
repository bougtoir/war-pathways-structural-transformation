import os
os.makedirs("results", exist_ok=True)
import experiments
if __name__ == "__main__":
    for f in (experiments.gate19_consent_rules, experiments.gate20_channels,
              experiments.gate21_sponsors, experiments.gate22_reachability,
              experiments.gate23_civilian_coupled, experiments.gate24_rules,
              experiments.gate25_dual_use, experiments.gate26_null_comparison,
              experiments.gate26_stepdown):
        print("===", f.__name__, "==="); f()
    print("outputs in results/")
