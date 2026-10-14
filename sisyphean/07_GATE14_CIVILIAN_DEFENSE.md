# 07 — Gate 14: Civilian Constraints and Asymmetric Defense

Output: `gate14_civilian.csv` (n = 1500/condition, seed 11).

## Hard constraints implemented

- Civilian harm dh = −harm_c·c·(1−protect) is a **metric and constraint**,
  never an instrument: no mechanism in the model lowers h to raise the
  aggressor's costs.
- Defender sustainment is **asymmetric**: defensive buildup dd grows toward
  d_max, is financed by civilian functionality (gated on h > 0.6·h_min),
  and never draws down the aggressor-side keystone accounting for the
  defender. Aggression drains K; defense drains nothing of the defender's
  sustainment to zero.
- Defender resistance adds to the *attacker's* burn (resist_burn·d): a
  stronger defender accelerates the aggressor's self-exhaustion — defense
  and the lever are complements.

## Results

| scenario | mean spell | harm mean | h_final | defender_ok | civilian_ok |
|----------|-----------|-----------|---------|-------------|-------------|
| baseline | 39.0 | 0.028 | 0.85 | 1.0 | 1.0 |
| lever | 23.0 | 0.009 | 0.91 | 1.0 | 1.0 |
| lever + defensive boost | 16.0 | 0.004 | 0.94 | 1.0 | 1.0 |
| deprivation (FORBIDDEN reference) | 23.0 | **1.21** | **0.00** | 1.0 | **0.0** |

The forbidden comparator shows the same spell length as the lever but with
40× the harm and total civilian collapse — demonstrating the constraint is
load-bearing: the lever achieves cessation *without* the deprivation
signature.

**Gate 14: PASS.** Aggressor-deterred-while-defender-capable is achieved in
simulation; deprivation is shown only as a rejected comparator and produces
measurably worse outcomes on the civilian constraint.
