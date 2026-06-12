import pandas as pd
from analysis.loader import load_data
from analysis.cleaner import clean
from analysis.aggregator import accuracy_by_model_and_dataset, accuracy_stats, overfit_rate_by_model, speed_by_model
from analysis.reporter import top_runs, best_run_per_model, merge_with_registry, classify_accuracy, run_number_extract

runs_df, registry_df = load_data()
runs_df = clean(runs_df)

# Merges two CSVs 
runs_merge = merge_with_registry(runs_df, registry_df)

# Generages additional columns
runs_merge["accuracy_tier"] = runs_merge["val_accuracy"].apply(classify_accuracy)
runs_merge["run_number"] = run_number_extract(runs_df["run_id"]).astype(int)

# Exports df as CSV to file path in exports
runs_merge.to_csv("output/experiment_results.csv", index=False)

#Exports df as paraquet to file path 
runs_merge.to_parquet("output/experiment_results.parquet", index=False)

# Output 
#Dataset Summary
print("--- Dataset Summary ---")
print(f"Clean dataset: {len(runs_df)} runs")
print("")

#Accuracy by model type (mean, std, count)
print("--- Accuracy Stats per Model ---")
print(accuracy_stats(runs_df))
print("")

#Accuracy by model type and dataset (the unstacked pivot)
print("--- Accuracy by Model and Dataset ---")
print(accuracy_by_model_and_dataset(runs_df))
print("")

#Overfitting rate by model type
print("--- Overfitting rate by Model Type")
print(overfit_rate_by_model(runs_df))
print("")

#Top 10 runs overall
print("--- Top 10 Runs Overall ---")
print(top_runs(runs_df, 10))
print("")

#Best run per model type
print("--- Best run per Model ---")
print(best_run_per_model(runs_df))
print("")

#Accuracy tier distribution
print("--- Accuracy Tier Distribution ---")
#accuracy_distribution = runs_merge.groupby('model_type')['accuracy_tier'].value_counts()
accuracy_distribution = runs_merge["accuracy_tier"].value_counts()
print(accuracy_distribution)
print("")

#Approved vs non-approved run counts
only_true = runs_merge[runs_merge["is_approved"] == True]
only_false = runs_merge[runs_merge["is_approved"] == False]
counts = len(only_true), len(only_false)
print("--- Approved vs Non-Approved Runs ---")
print(f"Approved: {counts[0]}")
print(f"Non-Approved: {counts[1]}")