# Benchmark

## Validation methodology

RSFQ-JEPA is evaluated on held-out cells from the open ColdFlux SFQ5ee+ cell library (Stellenbosch University). Predictions are compared against JoSIM ground truth, with design-rule-violation detection measured against MIT-LL SFQ5ee+ design rules. The held-out cells are not used during training.

## Results (held-out cells vs JoSIM)

| Metric | Result |
| --- | --- |
| Propagation delay | 14 ps RMSE |
| Peak current | 2 uA RMSE |
| Functional classification | approximately 100% |
| Design-rule-violation detection | 99.2% |
| JoSIM-calibrated margin heads (Ic margin, bias margin, max frequency) | 3 to 4% MAE |
| Conformal coverage (alpha = 0.1) | at least 89% |
| Speed | over 1000x faster than SPICE/JoSIM per cell |

## Caveats

- This is v0.
- These numbers are surrogate-versus-oracle: the comparison baseline is JoSIM, not silicon.
- The model is not fab-calibrated and not silicon-validated.
- It predicts cell properties and does not design cells.
- It is scoped to the SFQ5ee+ cell family.
