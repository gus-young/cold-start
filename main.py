import pandas as pd
from analysis.loader import load_data
from analysis.cleaner import clean, normalize_model_type

runs_df, registry_df = load_data()
runs_df = clean(runs_df)
print(f"Clean dataset: {len(runs_df)} runs")
