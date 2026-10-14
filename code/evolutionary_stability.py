"""
Adaptive stability analysis for strategies W (military coercion),
B (bargaining), S (structural substitution) under replicator dynamics.

Replicator dynamics are used ONLY as an illustrative adaptive-selection
metaphor for institutional/strategic diffusion, NOT as a literal model of
interstate politics (population mapping is not justified; see
08_EVOLUTIONARY_STABILITY.md).

Questions:
  - Is S locally stable (ESS-like) against W and B invaders?
  - How large is its basin of attraction?
  - Does it recover after shocks (leader change, resource shortage,
    aggressive invasion, misperception)?
"""
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

RNG = np.random.default_rng(7)
STRATS = ["W", "B", "S"]


def payoff_matrix(alpha=0.4, beta=0.5, gamma=0.3, exploit=0.35):
    """
    Payoff matrix A[i,j]: row strategy i vs column j.

    W vs W: mutual war is costly           -> -0.3
    W vs B: coercion exploits bargaining   -> 0.6 + exploit
    W vs S: coercion exploits substitution -> 0.6 + exploit (S vulnerable to aggression)
    B vs W: bargainer loses vs coercion    -> 0.1
    B vs B: negotiated settlement          -> beta
    B vs S: bargainer benefits mildly      -> beta - 0.05
    S vs W: substitution still loses to aggression -> 0.15
    S vs B: substitution gains efficiency  -> beta + alpha
    S vs S: structural substitution stable payoff   -> beta + gamma + alpha

    alpha: efficiency premium of substitution; beta: bargaining surplus;
    gamma: resilience bonus of S vs S; exploit: aggressor's gain vs nonviolence.
    """
    A = np.array([
        [-0.30,            0.60 + exploit,      0.60 + exploit],
        [ 0.10,            beta,                beta - 0.05],
        [ 0.15,            beta + alpha,        beta + gamma + alpha],
    ])
    return A


def replicator(t, x, A):
    f = A @ x
    phi = x @ f
    return x * (f - phi)


def is_ess(A, i, tol=1e-9):
    """ESS check (Maynard Smith): strict better reply, or equal vs itself and
    better vs the mutant in the mutant population."""
    n = A.shape[0]
    for j in range(n):
        if j == i:
            continue
        if A[i, i] < A[j, i] - tol:
            return False
        if abs(A[i, i] - A[j, i]) <= tol and A[i, j] <= A[j, j] + tol:
            return False
    return True


def basin_size(A, n_grid=26):
    """Estimate basin of attraction of each pure vertex via simplex grid."""
    counts = np.zeros(3)
    for i in range(n_grid + 1):
        for j in range(n_grid + 1 - i):
            k = n_grid - i - j
            x0 = np.array([i, j, k], float) / n_grid
            if (x0 == 1).any():
                counts[np.argmax(x0)] += 1
                continue
            sol = solve_ivp(replicator, (0, 300), x0, args=(A,),
                            rtol=1e-8, atol=1e-10)
            counts[np.argmax(sol.y[:, -1])] += 1
    return counts / counts.sum()


def shock_recovery(A, x_eq, T=150):
    """After an S-dominated equilibrium, inject W invaders (15%) and measure
    the return time to within 2% of the pre-shock S share (recovery), not
    merely S-majority — majority is already held right after the shock."""
    x0 = x_eq.copy()
    w_add = 0.15
    x0 = x0 * (1 - w_add)
    x0[0] += w_add
    sol = solve_ivp(replicator, (0, T), x0, args=(A,), rtol=1e-8, atol=1e-10)
    s_series = sol.y[2]
    target = max(x_eq[2] - 0.02, 0.0)
    t_rec = np.where(s_series >= target)[0]
    return float(sol.t[t_rec[0]]) if t_rec.size else np.inf, s_series[-1]


def run():
    rows = []
    grid = {
        "baseline":      dict(alpha=0.4, beta=0.5, gamma=0.3, exploit=0.35),
        "weak_S":        dict(alpha=0.1, beta=0.5, gamma=0.1, exploit=0.35),
        "strong_S":      dict(alpha=0.6, beta=0.5, gamma=0.5, exploit=0.35),
        "high_exploit":  dict(alpha=0.4, beta=0.5, gamma=0.3, exploit=0.70),
        "instit_shock":  dict(alpha=0.4, beta=0.3, gamma=0.3, exploit=0.50),
    }
    for name, kw in grid.items():
        A = payoff_matrix(**kw)
        ess = {s: is_ess(A, i) for i, s in enumerate(STRATS)}
        basin = basin_size(A)
        # equilibrium near S corner
        sol = solve_ivp(replicator, (0, 400), np.array([0.05, 0.15, 0.80]),
                        args=(A,), rtol=1e-9, atol=1e-11)
        x_eq = sol.y[:, -1]
        t_rec, s_final = shock_recovery(A, x_eq)
        rows.append(dict(
            scenario=name, ess_W=ess["W"], ess_B=ess["B"], ess_S=ess["S"],
            basin_W=basin[0], basin_B=basin[1], basin_S=basin[2],
            eq_W=x_eq[0], eq_B=x_eq[1], eq_S=x_eq[2],
            shock_return_time=t_rec, S_after_shock=s_final,
        ))
    df = pd.DataFrame(rows).set_index("scenario")
    df.to_csv("results/evolutionary_stability.csv")
    return df


def misperception_robustness(n=2000):
    """Bounded rationality: add noise to expected payoffs, measure frequency
    with which W still invades an S-dominated population."""
    A = payoff_matrix()
    invaded = 0
    for _ in range(n):
        noise = RNG.normal(0, 0.15, size=A.shape)
        A_hat = A + noise
        # does perceived payoff of W vs S exceed S vs S?
        if A_hat[0, 2] > A_hat[2, 2]:
            invaded += 1
    rate = invaded / n
    pd.DataFrame([{"misperceived_invasion_rate": rate}]).to_csv(
        "results/misperception.csv", index=False)
    return rate


if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    df = run()
    print(df.round(3))
    print("\nMisperceived W-invasion rate:", round(misperception_robustness(), 3))
