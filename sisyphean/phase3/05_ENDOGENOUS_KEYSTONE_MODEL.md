# 05 — Endogenous Keystone Model (Gate 19–21 formalization)

## Minimal state (per dyad)

(q, c, m, V_G, U_L-implicit, K, S_p, ρ, h, d, L, pos, patron∈{0,1})

See `code/model.py` docstring for full equations. Key laws:

**Consent (Channel A):**
habitual: L → L_floor while war_on (rate L_decay), recovers L_recover.
threshold: cumulative observed harm τ accumulates c; when τ > τ_i
(heterogeneous per run), L → L_floor. Both rules non-maximizing; both
produce collapse (g19).

**Objective efficacy:**
V_G = pos·(0.3+0.7L) for consent-dependent goals
(territory/status/identity/security); V_G = pos (regime_survival);
V_G = 0.2+0.8·pos (intrinsic). Goals not needing consent cannot be
hollowed — war can continue despite "value collapse" claims; the model
predicts exactly where this boundary lies (g20).

**Endogenous replenishment (Channel B):**
ρ(t) = ρ_dom + patron_flow·1[patron] + sub_rate·1[¬patron]
patron exits when e = c·ext > tol_patron; re-enters when e < reenter.
Balancer adds defender support ∝ c. Sponsor entry/exit, substitution
opening, and a permanent-failure counterexample (tolerant patron +
large stockpile → ρ ≥ burn forever) all implemented (g21).

**Sustainment:** dK = −κ·c·m − r_b·d + ρ + release(S_p).

**Battlefield position:** dpos = 0.05·(m−d) — success can coincide with
efficacy collapse when L falls (Channel A operates independent of pos).

## Why smallest

Each element exists to satisfy one gate requirement; removing any
(state or actor) breaks a named gate. No utility maximization is needed
anywhere except the optional 'eu' reference rule.
