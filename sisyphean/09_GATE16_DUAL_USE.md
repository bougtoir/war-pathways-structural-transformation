# 09 — Gate 16: Dual-Use Constraint Interaction

Output: `gate16_dualuse.csv` (grid: o ∈ [0,0.8] × spill ∈ [0,0.5],
n = 800/cell, seed 31).

## Two channels, no stipulated sign

Mobilization target m_target = 0.6 + spill − 0.4·o:

- **opportunity-cost channel** (o): capability diverted to civilian
  production lowers m — a real constraint on war capacity;
- **scale/learning channel** (spill): civilian-capacity growth spills into
  mobilizable capacity — the bypass pathway.

The sign of the net effect is *emergent*, not assumed.

## Findings

- P(hit W) = 1 for all o < 0.4 regardless of spill (up to 0.5): below the
  threshold, dual-use is **war-facilitating or neutral** — the constraint
  never binds, and spillover simply grows mobilization.
- P(hit W) = 0 for all o ≥ 0.4 at any spill ≤ 0.5: above threshold the
  opportunity-cost channel dominates and onsets vanish entirely.
- The reversal region is a sharp edge at o ≈ 0.4 (given m_req): the same
  civilian-mobilization economy is pro-war below the threshold and
  anti-war above it. **This is a genuine mechanism-reversal region**, the
  object Gate 16 requires us to exhibit.
- Caveat: the reversal is driven by feasibility (m < m_req), not by
  selection — dual-use suppresses war through the *capacity* margin even
  when leaders still want it.

**Gate 16: PASS.** Both channels modeled, sign emergent, reversal region
identified and reported (rather than tuned away).
