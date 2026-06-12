# ML Experiment Log Analyzer

A Python data pipeline that generates synthetic ML experiment logs, cleans them, and produces aggregated performance reports.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) ![pandas](https://img.shields.io/badge/pandas-2.x-green)

## Features

- Synthetic data generator producing 101 experiment runs across four model types
- Multi-step cleaning pipeline that filters incomplete runs, normalizes fields, and flags overfitting
- Accuracy aggregations by model type and dataset — pivot tables, stats, and overfit rate
- Model registry join enriching runs with team ownership and approval status
- Accuracy tier classification (`high`, `medium`, `low`) and top-N run ranking
- Export to both CSV and Parquet

## Getting Started

**Requirements:** Python 3.8+, pandas, pyarrow

```bash
git clone https://github.com/gus-young/cold-start.git
cd cold-start
pip install pandas pyarrow
python data/generate.py
python main.py
```

## Project Structure

```
├── main.py                       # Pipeline entry point and console output
├── data/
│   └── generate.py               # Synthetic data generator
├── analysis/
│   ├── loader.py                 # CSV ingestion
│   ├── cleaner.py                # Filtering, normalization, overfitting flags
│   ├── aggregator.py             # Accuracy and speed aggregations
│   └── reporter.py               # Top runs, best-per-model, registry merge
└── output/
    ├── runs.csv                  # Raw experiment runs
    ├── model_registry.csv        # Model metadata
    └── experiment_results.csv / .parquet
```