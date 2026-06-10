import pandas as pd

def top_runs(df, n=10):
    top_accuracy = df.nlargest(n, "val_accuracy")[['run_id', 'model_type', 'dataset', 'val_accuracy', 'is_overfit']]
    return top_accuracy

def best_run_per_model(df):
    idx = df.groupby("model_type")["val_accuracy"].idxmax()
    values = df.loc[idx]
    return values

def merge_with_registry(runs_df, registry_df):
    df = pd.merge(runs_df, registry_df, on="model_type", how="left")
    only_true = df[df["is_approved"] == True]
    only_false = df[df["is_approved"] == False]
    counts = len(only_true), len(only_false)
    return counts