import pandas as pd
from analysis.loader import load_data
from analysis.cleaner import clean
from analysis.aggregator import accuracy_by_model_and_dataset, accuracy_stats

runs_df, registry_df = load_data()
runs_df = clean(runs_df)
#print(f"Clean dataset: {len(runs_df)} runs")
#print(accuracy_stats(runs_df))
print(accuracy_by_model_and_dataset(runs_df))