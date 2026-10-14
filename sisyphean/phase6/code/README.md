# phase6/code — mathematical repair + checks

`pip install -r requirements.txt && pytest tests && python checks6.py`

- `model6.py`: repaired definitions — r intensity, L state, V flow;
  the four distinct objects (a) partial dpi/dr, (b) total along L*(r),
  (c) dpi/dt, (d) level pi(r,L_inf); two behavioral specs (opt/rule).
- `checks6.py`: numerical verification of repaired propositions,
  T-1 counterexample, asset-mix boundary, boundary cases (r=0),
  stable high/low appropriability regimes.
- `tests/test_model6.py`: pytest checks for boundaries and sign claims.
No real data. All parameters illustrative.
