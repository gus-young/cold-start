import pandas as pd
from analysis.loader import load_data
from analysis.cleaner import clean
from analysis.aggregator import accuracy_by_model_and_dataset, accuracy_stats, overfit_rate_by_model, speed_by_model
from analysis.reporter import top_runs, best_run_per_model, merge_with_registry

runs_df, registry_df = load_data()
runs_df = clean(runs_df)
#print(f"Clean dataset: {len(runs_df)} runs")
#print(accuracy_stats(runs_df))
#print(accuracy_by_model_and_dataset(runs_df))
#print(overfit_rate_by_model(runs_df))
#print(speed_by_model(runs_df))
#print(top_runs(runs_df))
#print(best_run_per_model(runs_df))
print(merge_with_registry(runs_df, registry_df))