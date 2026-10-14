# 05 — Gate 12: Keystone Existence and Self-Undermining Dynamics

## Definition (non-circular)

K is defined *independently of the outcome*: the exogenously measurable
stock (fiscal reserves + external coalition supply + mobilizable materiel)
whose positive level is **causally necessary** for c ≥ C_W to be
maintained. Necessity is operationalized: if K ≤ K_min the process exits W
regardless of q, v, or selection rule — i.e., will cannot substitute for
stock. This avoids defining the keystone as "whatever ends the war".

## Sufficient condition (finite-lag exit)

Let burn rate b = κ·c·m + r_b·d and replenishment ρ = sponsor + release.
If b > ρ sustained, then

```
t_exit ≤ (K₀ + S_p₀ − K_min) / (b − ρ)        (upper bound)
```

Numerical check (`gate12_bound.csv`): every run exits; observed exit times
lie well below the bound (e.g. κ=0.045, sponsor=0: bound 111, observed 31 —
the bound uses the conservative c_min·m_min product, reality burns faster).

## Instantaneous vs lagged vs attrition

- **Instantaneous collapse** (onset ⇒ immediate K→K_min) is *rejected*:
  no mechanism in the model or literature produces it; discard.
- **Finite lag** (the modeled regime): burn exceeds replenishment after
  stockpile exhaustion; exit in tens of periods.
- **Slow attrition** (κ ≤ sponsor): K asymptotes, never crosses K_min —
  war persists to dur_max; the lever is inactive.

## Counterexample (most damaging)

Sponsor-rich adversary: sponsor = 0.05, S_p0 = 3.0, s_release = 0.15,
K0 = 1.5 (`adversarial_failure.csv`). Replenishment exceeds burn
indefinitely → P(K-exit) = 0, spells run to duration cap, cumulative harm
mean 0.62 and civilian_ok = 0. **The lever fails when K-replenishment is
structurally unbounded** — external sponsors that scale with aggression
defeat it. This is the same bypass pathway the prompt requires we model;
it is a genuine failure mode, not a patched one.

## Comparison to adjacent mechanisms

| mechanism | target | is it a keystone? |
|-----------|--------|-------------------|
| attrition | capacity degradation | same family; lever adds the *onset-triggered* asymmetry |
| sanctions | external ρ → 0 | exogenous; bypassable (black markets, substitution) |
| deterrence | raises ex-ante cost | affects selection, not sustainment |
| endogenous termination (Slantchev) | information/beliefs | belief-based; ours is stock-based and rule-agnostic |

**Gate 12: CONDITIONAL PASS.** A non-tautological K with a verifiable
finite-lag bound exists *if and only if* burn can exceed replenishment;
the sufficient condition is stated and the falsifying parameter region is
identified and simulated.
