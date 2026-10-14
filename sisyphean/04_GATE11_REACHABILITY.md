# 04 — Gate 11: Reachability of the War Set

**Question.** Can a high onset barrier keep the state out of W, and does a
keystone-burn mechanism shorten residence in W — across shock regimes?

**Method.** Monte Carlo (n = 1500/condition, seed 42) over T = 300 periods,
first-hitting probability of W, normal vs Cauchy shock tails.
Code: `sisyphean/code/experiments.py::gate11_reachability`.
Output: `sisyphean/code/results/gate11_reachability.csv`.

## Results

| scenario | P(hit W) | mean first hit | mean spell | p90 harm |
|----------|----------|----------------|------------|----------|
| baseline | 1.00 | 0.0 | 39.0 | 0.028 |
| barrier (B=3) | 1.00 | 19.1 | 39.0 | 0.028 |
| keystone burn | 1.00 | 0.0 | 23.0 | 0.009 |
| combined | 1.00 | 19.1 | 23.0 | 0.009 |
| sponsor-rich (counterexample) | 1.00 | 19.1 | 69.3 | 0.093 |

Cauchy tails add ≈ +1.2 periods to first-hit under barrier; no qualitative
change. Blocked barrier attempts reroute: mean ≈ 6.7–7.2 displacement
events per 300-period run when B is high.

## Findings

1. **P(hit W) is not suppressible to near-zero** by any configuration we
   tested — over a 300-period horizon a barrier delays onset (~19 periods
   at B=3) rather than preventing it. We therefore make **no universal
   near-zero onset claim**. The honest claim is rate/delay reduction.
2. Keystone burn does not change reachability; it changes *residence*
   (spell 39 → 23 periods, p90 harm 0.028 → 0.009). Onset prevention and
   sustainment degradation are **separable levers** — consistent with the
   Phase-1 conjunction insight.
3. The combined lever is strictly better than either alone on
   (delay, spell, harm) — additive, not multiplicative, here.
4. Sponsor-rich replenishment restores mean spell to ≈69 and worsens harm:
   the lever fails exactly where Gate 12 predicts it must.

**Gate 11: PASS (conditional).** Reachability analysis delivered; the
deliverable truthfully reports that barriers delay rather than prevent.
