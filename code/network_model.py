"""
Minimal network model of conflict escalation: a Watts-type threshold
cascade on random graphs with TWO edge types:

  - destabilizing edges (security commitments, alliance triggers,
    conflict transmission): the ONLY edges that transmit conflict.
  - stabilizing edges (economic dependencies, institutional ties):
    raise a node's adoption threshold AND do not transmit.

Each node i adopts conflict when
    |active destabilizing neighbors of i| / deg(i)  >=  tau_i,
tau_i = 0.25 + 0.45 * stab_share_i, where stab_share_i is the fraction
of i's edges that are stabilizing. An exogenous seed set starts in
conflict.

Outputs: cascade size vs connectivity and vs stabilizing-edge fraction.
ILLUSTRATIVE only.
"""
import numpy as np
import networkx as nx
import pandas as pd

RNG = np.random.default_rng(99)


def typed_graph(n, z, s_bar):
    """Erdos-Renyi graph with per-edge type. Returns (G, destab, stab_share).

    Each edge is stabilizing with probability s_bar (seeded RNG).
    """
    G = nx.gnp_random_graph(n, z / n, seed=int(RNG.integers(1e9)))
    destab = {i: set() for i in G.nodes}
    stab_share = {i: 0.0 for i in G.nodes}
    stab_count = {i: 0 for i in G.nodes}
    for u, v in G.edges:
        if RNG.random() < s_bar:
            stab_count[u] += 1
            stab_count[v] += 1
        else:
            destab[u].add(v)
            destab[v].add(u)
    for i in G.nodes:
        deg = G.degree(i)
        stab_share[i] = stab_count[i] / deg if deg else 0.0
    return G, destab, stab_share


def cascade(G, destab, stab_share, seeds, w=1.0):
    """Return fraction of nodes eventually in conflict."""
    n = G.number_of_nodes()
    tau = {i: 0.25 + 0.45 * stab_share[i] for i in G.nodes}
    active = set(seeds)
    frontier = set(seeds)
    while frontier:
        new = set()
        for i in G.nodes:
            if i in active:
                continue
            deg = G.degree(i)
            if not deg:
                continue
            frac = sum(j in active for j in destab[i]) / deg
            if w * frac >= tau[i]:
                new.add(i)
        if not new:
            break
        frontier = new
        active |= new
    return len(active) / n


def run(n=400, reps=30):
    """Sweep: mean degree z x stabilizing-edge fraction s_bar."""
    rows = []
    for z in [2, 4, 6, 8, 10, 12]:
        for s_bar in [0.0, 0.2, 0.4, 0.6, 0.8]:
            sizes = []
            for _ in range(reps):
                G, destab, stab_share = typed_graph(n, z, s_bar)
                if G.number_of_nodes() == 0:
                    continue
                seeds = list(RNG.choice(list(G.nodes), size=max(1, n // 100),
                                        replace=False))
                sizes.append(cascade(G, destab, stab_share, seeds))
            rows.append({"mean_degree": z, "stab_frac": s_bar,
                         "cascade_mean": float(np.mean(sizes)),
                         "cascade_p90": float(np.quantile(sizes, 0.9)),
                         "cascade_std": float(np.std(sizes))})
    df = pd.DataFrame(rows)
    df.to_csv("results/network_cascade.csv", index=False)
    return df


def resilience_test():
    """Do stabilizing ties protect against large shocks?
    Compare cascade after a 5% exogenous seed (shock) at s_bar = 0 vs 0.6."""
    out = {}
    for s_bar in [0.0, 0.6]:
        sizes = []
        for _ in range(40):
            G, destab, stab_share = typed_graph(400, 6, s_bar)
            seeds = list(RNG.choice(list(G.nodes), size=20, replace=False))
            sizes.append(cascade(G, destab, stab_share, seeds))
        out[s_bar] = float(np.mean(sizes))
    pd.DataFrame([out]).to_csv("results/network_resilience.csv", index=False)
    return out


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    df = run()
    print(df.round(3).to_string(index=False))
    print("\nResilience (5% shock):", resilience_test())
