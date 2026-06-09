import pandas as pd 

def filter_completed(df):
    mask = df['status'] == "completed"
    filtered_df = df[mask]
    return filtered_df

def drop_incomplete_metrics(df):
    no_null = df.dropna(subset=["val_accuracy"])
    return no_null

def normalize_model_type(df):
    normalized_df = df["model_type"].str.strip().str.lower()
    return normalized_df

def flag_ovefitting(df, threshold=0.05):
    return df['is_overfit'] = df['train_accuracy'] - df ['val_accuracy'] > threshold
     