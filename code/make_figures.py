"""Generate figures for 10_SIMULATION_RESULTS.md from results/*.csv."""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fig_scenarios():
    df = pd.read_csv("results/scenarios.csv", index_col=0)
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(df))
    ax.bar(x - 0.2, df["p_war"], width=0.4, label="P(war pathway)")
    ax.bar(x + 0.2, df["p_agency_gap"], width=0.4,
           label="P(leader wants, state does not)")
    ax.set_xticks(x); ax.set_xticklabels(df.index, rotation=25, ha="right")
    ax.set_ylabel("probability")
    ax.set_title("War-pathway probability by intervention scenario (illustrative)")
    ax.legend(); fig.tight_layout()
    fig.savefig("results/fig_scenarios.png", dpi=150); plt.close(fig)


def fig_sensitivity():
    df = pd.read_csv("results/sensitivity.csv")
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for key, g in df.groupby("param"):
        ax.plot(g["value"], g["p_war"], marker="o", ms=3, label=key)
    ax.set_xlabel("parameter value"); ax.set_ylabel("P(war pathway)")
    ax.set_title("One-at-a-time sensitivity (illustrative)")
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig("results/fig_sensitivity.png", dpi=150); plt.close(fig)


def fig_cascade():
    df = pd.read_csv("results/network_cascade.csv")
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for s, g in df.groupby("stab_frac"):
        ax.plot(g["mean_degree"], g["cascade_mean"], marker="o", ms=3,
                label=f"stab. edge share {s}")
    ax.set_xlabel("mean degree (connectivity)")
    ax.set_ylabel("mean cascade size (share of network)")
    ax.set_title("Conflict cascade vs connectivity and stabilizing ties (illustrative)")
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig("results/fig_cascade.png", dpi=150); plt.close(fig)


def fig_basin():
    df = pd.read_csv("results/evolutionary_stability.csv", index_col=0)
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(df))
    ax.bar(x - 0.25, df["basin_W"], width=0.25, label="W")
    ax.bar(x, df["basin_B"], width=0.25, label="B")
    ax.bar(x + 0.25, df["basin_S"], width=0.25, label="S")
    ax.set_xticks(x); ax.set_xticklabels(df.index, rotation=25, ha="right")
    ax.set_ylabel("basin share")
    ax.set_title("Basin of attraction by payoff scenario (illustrative)")
    ax.legend(); fig.tight_layout()
    fig.savefig("results/fig_basin.png", dpi=150); plt.close(fig)


if __name__ == "__main__":
    fig_scenarios(); fig_sensitivity(); fig_cascade(); fig_basin()
    print("figures written to results/")
