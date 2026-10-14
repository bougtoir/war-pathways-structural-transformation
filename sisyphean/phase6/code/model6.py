"""
Phase 6 — repaired appropriability model.

Objects (Gate 1):
  r   coercion INTENSITY (choice variable, r >= 0)
  L   cooperation STATE in [0,1]
  V   value FLOW produced per period: V(L) = V0*(v_min + (1-v_min)*L)
  q   legibility (institutional quality) in (0,1]
  alpha(L,q) = w_phys + w_hum*L + w_inst*L*q + w_net*L^2

Flow payoff per period:
  pi(r,L) = r*alpha(L,q)*V(L) - c1*r - c2*r**2

Four mathematically distinct objects (old T-1 conflated (b) and (d)):
  (a) dpi/dr|_L          = alpha*V - c1 - 2*c2*r
  (b) dpi/dr along L*(r) = (a) + (dpi/dL) * L*'(r)
  (c) dpi/dt             = (dpi/dL) * dL/dt   on a trajectory
  (d) pi(r, L_inf)       level — the quantity that decides abandonment

Level condition for negative payoff at intensity r:
  pi(r, L_inf) < 0   <=>   alpha(L_inf,q)*V(L_inf) < c1 + c2*r     (LVL)

Note r=0: pi(0,L)=0 identically — 'non-positive', never strictly
negative; claims about r=0 are handled separately.
"""
import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class P6:
    w_phys: float = 0.4
    w_hum: float = 0.3
    w_inst: float = 0.2
    w_net: float = 0.1
    q: float = 0.7
    V0: float = 1.0
    v_min: float = 0.3
    c1: float = 0.15
    c2: float = 0.25
    # cooperation dynamics (endogenous, Gate 2)
    L_max: float = 1.0
    L_floor: float = 0.1
    exit_cost: float = 0.2       # cost of withdrawing cooperation
    fear_gain: float = 0.0       # coercion can INCREASE compliance
    coll_action: float = 0.5     # collective-action capacity of population
    beta: float = 1.0            # responsiveness (optimizing spec)
    habit: float = 0.0           # boundedly-rational inertia (rule spec)
    dL_rate: float = 0.15


def V_of_L(L, p):
    return p.V0 * (p.v_min + (1 - p.v_min) * L)


def alpha_of(L, p):
    return (p.w_phys + p.w_hum * L + p.w_inst * L * p.q
            + p.w_net * L * L)


def pi(r, L, p):
    return r * alpha_of(L, p) * V_of_L(L, p) - p.c1 * r - p.c2 * r * r


def dpi_dr_fixed_L(r, L, p):
    """(a) partial derivative wrt intensity at fixed state."""
    return alpha_of(L, p) * V_of_L(L, p) - p.c1 - 2 * p.c2 * r


def dpi_dL(r, L, p):
    a, aL = alpha_of(L, p), p.w_hum + p.w_inst * p.q + 2 * p.w_net * L
    v, vL = V_of_L(L, p), p.V0 * (1 - p.v_min)
    return r * (aL * v + a * vL)


def L_star_opt(r, p):
    """Cooperation best response under coercion intensity r.

    Voluntary cooperation chosen weighing its return in the produced-
    value share retained by the population vs exit_cost and the
    collective-action constraint. Coercion can RAISE observed compliance
    via fear_gain (distinguishing compliance from cooperation):
      L* = clip(L_max - coll_action * r / (exit_cost + eps) + fear_gain*r)
    solved as the stable rest point of the population's coordination
    problem; sign of dL*/dr is an OUTCOME.
    """
    if p.coll_action <= 0:
        return p.L_max
    slope = p.fear_gain - p.coll_action / max(p.exit_cost, 1e-9)
    raw = p.L_max + slope * r
    return float(np.clip(raw, p.L_floor, p.L_max))


def L_star_rule(r, p):
    """Boundedly rational / rule-of-thumb response: cooperation decays
    toward a habit-anchored level — exits only above a salience
    threshold, never optimizing the margin."""
    thresh = p.exit_cost + p.habit
    if r <= thresh:
        return p.L_max
    return float(np.clip(p.L_max - (r - thresh), p.L_floor, p.L_max))


def dpi_dr_total(r, p, spec="opt", h=1e-5):
    """(b) total derivative along response equilibrium (envelope: the
    direct effect plus the induced cooperation response)."""
    Ls = L_star_opt if spec == "opt" else L_star_rule
    L0 = Ls(r, p)
    Lp = (Ls(r + h, p) - Ls(r - h, p)) / (2 * h)
    return dpi_dr_fixed_L(r, L0, p) + dpi_dL(r, L0, p) * Lp


def L_inf(r, p, spec="opt", T=500):
    """Long-run cooperation level under sustained r (trajectory limit)."""
    Ls = L_star_opt if spec == "opt" else L_star_rule
    L = p.L_max
    for _ in range(T):
        tgt = Ls(r, p)
        L += p.dL_rate * (tgt - L)
    return L


def pi_inf(r, p, spec="opt"):
    """(d) long-run payoff level — the object Gate-1 cares about."""
    return pi(r, L_inf(r, p, spec), p)


def level_condition(r, p, spec="opt"):
    L = L_inf(r, p, spec)
    lhs = alpha_of(L, p) * V_of_L(L, p)
    return lhs, p.c1 + p.c2 * r, lhs < p.c1 + p.c2 * r
