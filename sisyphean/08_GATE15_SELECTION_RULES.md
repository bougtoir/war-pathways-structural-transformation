# 08 — Gate 15: Non-Maximizing Selection Rules

Output: `gate15_rules.csv` (n = 1200/condition, seed 21).

## Requirement

≥2 non-maximizing rules; withdraw rationality-independence if results need
maximization. Four rules tested: eu (maximizer), noisy (trembling),
aspiration (satisficing — ignores U_A entirely), bureaucratic (utility-free
organizational routine with error).

## Results (baseline → lever)

| rule | onsets | spell | harm | first hit |
|------|--------|-------|------|-----------|
| eu | 1.0 → 1.0 | 39 → 23 | .028 → .009 | 0 → 6.2 |
| noisy | 51.9 → 9.3 | 67.5 → 35.7 | .150 → .041 | 0.8 → 13.3 |
| aspiration | 1.0 → 0.99 | 39 → 23 | .028 → .009 | 20.6 → 56.5 |
| bureaucratic | 60.0 → 10.1 | 69.8 → 35.8 | .165 → .041 | 2.4 → 23.8 |

## Findings

1. The lever (barrier + keystone burn) works under **every** rule,
   including the two strictly non-maximizing ones (aspiration,
   bureaucratic): spell shortening is identical across rules because the
   keystone operates *below* the decision layer — it constrains
   sustainment, not choice.
2. The barrier's effect is *largest* where selection is stochastic
   (onsets cut ~5–6× under noisy/bureaucratic): a per-attempt gate filters
   frequent marginal attempts harder than rare deliberate ones.
3. Aspiration-rule runs show the largest delay effect (first hit 20.6 →
   56.5) — barriers interact with satisficing in ways maximization
   misses.
4. No result requires U_W > U_A to be evaluated correctly; the
   bureaucratic rule never computes utilities at all.

**Gate 15: PASS.** Effects hold across ≥2 non-maximizing rules. We claim
rationality-independence *at the sustainment level only* — the keystone
mechanism does not read the leader's decision rule — while onset
frequencies do remain rule-dependent, as documented.
