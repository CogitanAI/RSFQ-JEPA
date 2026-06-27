"""Thin client example for RSFQ-JEPA.

This script is a thin client. It loads an example cell JSON, POSTs it to the
RSFQ-JEPA inference API, and prints the returned predictions. The model itself
runs server-side and is not distributed with this repository.

The real endpoint and an API key are provided on access request. Email
dylan@cogitan.ai.
"""

import json
import os
from pathlib import Path

import requests

# Base URL of the inference API. This is a placeholder. The real endpoint and an
# API key are provided on access request (dylan@cogitan.ai).
BASE_URL = "https://api.cogitan.ai"

# The API key is read from the environment so it is never hardcoded here.
API_KEY = os.environ.get("COGITAN_API_KEY", "your-api-key-here")

# Path to the example cells shipped in this repository.
EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"


def load_cell(cell_filename):
    """Load a cell JSON file from the examples directory."""
    cell_path = EXAMPLES_DIR / cell_filename
    with open(cell_path, "r", encoding="utf-8") as f:
        return json.load(f)


def predict(cell):
    """POST a cell to the inference API and return the predictions."""
    response = requests.post(
        f"{BASE_URL}/predict",
        headers={
            "X-API-Key": API_KEY,
            "Content-Type": "application/json",
        },
        json=cell,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def main():
    # Load one of the worked example cells.
    cell = load_cell("RSFF_DEMO_001.json")

    # Request predictions from the server-side model.
    predictions = predict(cell)

    # Print the returned predictions (17 heads plus calibrated uncertainty).
    print(json.dumps(predictions, indent=2))


if __name__ == "__main__":
    main()
