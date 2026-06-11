import pandas as pd
from analysis.loader import load_data
from analysis.cleaner import clean
from analysis.aggregator import accuracy_by_model_and_dataset, accuracy_stats, overfit_rate_by_model, speed_by_model
from analysis.reporter import top_runs, best_run_per_model, merge_with_registry, classify_accuracy, run_number_extract

runs_df, registry_df = load_data()
runs_df = clean(runs_df)
#print(f"Clean dataset: {len(runs_df)} runs")
#print(accuracy_stats(runs_df))
#print(accuracy_by_model_and_dataset(runs_df))
#print(overfit_rate_by_model(runs_df))
#print(speed_by_model(runs_df))
#print(top_runs(runs_df))
#print(best_run_per_model(runs_df))

# Merges two CSVs 
runs_merge = merge_with_registry(runs_df, registry_df)

# Generages additional columns
runs_merge["accuracy_tier"] = runs_df["val_accuracy"].apply(classify_accuracy)
runs_merge["run_number"] = run_number_extract(runs_df["run_id"]).astype(int)

# Exports df as CSV to file path in exports
runs_merge.to_csv("output/experiment_results.csv", index=False)

#Exports df as paraquet to file path 
runs_merge.to_parquet("output/experiment_results.parquet", index=False)

# Read back the paraquet file 
print(pd.read_parquet("output/experiment_results.parquet").shape)
print(runs_merge)