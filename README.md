# RSFQ-JEPA

A neural surrogate that predicts SPICE-level electrical properties and design-rule violations of superconducting RSFQ logic cells from their layout and circuit-graph representation, in milliseconds, with calibrated uncertainty.

## What it is

RSFQ-JEPA takes a Rapid Single Flux Quantum (RSFQ) logic cell, described by its layout raster and circuit graph, and predicts the electrical behavior you would otherwise get from a SPICE-class simulator, in milliseconds. It is the deep-screening engine behind Fluxus, the superconducting design suite from [Cogitan](https://cogitan.ai). The model returns 17 predicted properties together with calibrated uncertainty, so you can triage a large cell library quickly and decide which cells warrant a full simulation.

This is a v0 surrogate. It is validated against an oracle (JoSIM), not against silicon. See [Limitations](#limitations).

## Results (held-out cells vs JoSIM)

| Metric | Result |
| --- | --- |
| Propagation delay | 14 ps RMSE |
| Peak current | 2 uA RMSE |
| Functional classification | approximately 100% |
| Design-rule-violation detection | 99.2% |
| JoSIM-calibrated margin heads (Ic margin, bias margin, max frequency) | 3 to 4% MAE |
| Conformal coverage (alpha = 0.1) | at least 89% |
| Speed | roughly 1,000x to 3,000x faster than SPICE/JoSIM per cell |

Only the heads with direct JoSIM ground truth are tabulated above. The remaining heads are bounded scores or quantities learned from analytic oracles, which do not have a single-number JoSIM RMSE.

## Architecture

At a high level, RSFQ-JEPA combines:

- A hierarchical JEPA (joint-embedding predictive architecture) backbone.
- A graph neural network over the circuit graph.
- A vision transformer over the layout raster.
- Cross-attention to fuse the graph and layout representations.

The model has 297.5M parameters and 17 prediction heads. Uncertainty is estimated with MC-dropout and calibrated with split-conformal calibration.

## Use it

- Website: [cogitan.ai](https://cogitan.ai) — Cogitan, and the Fluxus superconducting design suite.
- Live demo: [demo.cogitan.ai](https://demo.cogitan.ai).
- Programmatic use: see [usage/predict_example.py](usage/predict_example.py) for a thin client that POSTs a cell to the inference API and prints the predictions.
- Access: an API endpoint and key are provided on request. Email dylan@cogitan.ai.

## Examples

The [examples/](examples/) directory contains:

- [examples/cell_schema.md](examples/cell_schema.md): the cell JSON schema.
- Worked example cells: `examples/RSFF_DEMO_001.json` and `examples/PA_DEMO_001.json`.

## What is here, and what is not

This repository provides the public interface to RSFQ-JEPA: the cell schema, example cells, a thin client, and benchmarks.

The model weights, training code, and data-generation pipeline are proprietary and are not included in this repository. RSFQ-JEPA runs server-side; this repo does not distribute the model.

## Limitations

- This is v0.
- It is a surrogate measured against an oracle (JoSIM), not fab-calibrated and not silicon-validated.
- It predicts cell properties. It does not design cells.
- It is scoped to the SFQ5ee+ cell family.

Training data is the open ColdFlux SFQ5ee+ cell library (Stellenbosch University) with JoSIM-generated ground-truth labels, evaluated against MIT-LL SFQ5ee+ design rules.

## Citation

See [CITATION.cff](CITATION.cff).

## Contact

Questions and access requests: dylan@cogitan.ai. Repository: https://github.com/CogitanAI/RSFQ-JEPA.
