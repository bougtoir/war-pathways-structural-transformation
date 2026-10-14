"""Run the full Sisyphean suite: cd sisyphean/code && python run_all.py"""
import os
os.makedirs("results", exist_ok=True)
import experiments

if __name__ == "__main__":
    for f in (experiments.gate11_reachability,
              experiments.gate12_keystone_exit_bound,
              experiments.gate13_relapse,
              experiments.gate14_civilian_defense,
              experiments.gate15_choice_rules,
              experiments.gate16_dual_use,
              experiments.adversarial_failure):
        print(f"\n=== {f.__name__} ===")
        out = f()
        print(out.round(3) if hasattr(out, "round") else out)
    print("\nAll outputs in results/")
