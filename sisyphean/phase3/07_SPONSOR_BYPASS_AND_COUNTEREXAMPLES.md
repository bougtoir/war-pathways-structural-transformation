# 07 — Sponsors, Bypass, and Counterexamples (Gate 21)

Output: `results/g21_sponsors.csv` (n=800, seed 17).

## Two sponsor types, independent objectives

- **Patron** (aggressor-side): provides ρ flow while its externality
  price e = c·ext stays below tolerance; exits when exceeded, re-enters
  when intensity subsides. Models a sponsor with reputational/economic
  costs, not a loyal ally.
- **Balancer** (defender-side): support ∝ c — rises with aggression,
  strengthens the defender and adds to attacker burn via resist_burn.
- **Substitution market**: opens at bounded rate when patron exits —
  black markets exist, are bounded, and cannot scale.

## Results

| scenario | mean spell | p_K_exit | patron retained |
|----------|-----------|----------|-----------------|
| baseline | 56 | 1.0 | 1.0 |
| intolerant patron | 55 | 1.0 | — |
| tolerant patron | 80 | **0.0** | — |
| permanent failure | 80 | **0.0** | — |
| strong balancer | 53 | 1.0 | — |

## Permanent-failure counterexample (required)

Tolerant patron (tol ≥ max externality) + K0=2 + S_p0=2 + s_release=0.15:
ρ ≥ burn forever, no K-exit ever, war runs to cap, civilians still harmed.
**The lever fails permanently when external resourcing scales with
aggression** — proxy war is the archetype. This boundary is a theorem
(R4), not a tuning failure.

## Bypass table

| pathway | modeled? | verdict |
|---------|----------|---------|
| sponsor exit/entry | yes (endogenous) | lever's boundary is here |
| substitution/black market | bounded sub_rate | raises floor; fatal only if ≥ burn−ρ_dom |
| proxy relocation | sub_rate + tolerant patron | permanent failure region |
| institutional capture | via e_b on bureaucratic rule | changes onset count, not sustainment |
| technological adaptation | spill channel (gate25) | war-facilitating |
| defender strengthening | balancer (endogenous) | complements lever; safe asymmetry |
