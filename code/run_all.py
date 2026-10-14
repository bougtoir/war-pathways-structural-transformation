"""Run the full simulation suite. Usage: cd code && python run_all.py"""
import os
os.makedirs("results", exist_ok=True)
import bargaining_model, evolutionary_stability, network_model, make_figures

if __name__ == "__main__":
    print("=== bargaining / pathway scenarios ===")
    print(bargaining_model.run()[["p_war", "p_leader_wants", "p_feasible",
                                  "p_escalate", "p_agency_gap"]].round(3))
    print("\n=== region overlap ===")
    print(bargaining_model.region_overlap())
    print("\n=== sensitivity ===")
    bargaining_model.sensitivity()
    print("=== evolutionary stability ===")
    print(evolutionary_stability.run().round(3))
    print("misperceived invasion rate:",
          round(evolutionary_stability.misperception_robustness(), 3))
    print("\n=== network cascade ===")
    print(network_model.run().round(3).to_string(index=False))
    print("resilience:", network_model.resilience_test())
    make_figures.fig_scenarios(); make_figures.fig_sensitivity()
    make_figures.fig_cascade(); make_figures.fig_basin()
    print("\nAll outputs in results/")
