import pandas as pd 

def filter_completed(df):
    mask = df['status'] == "completed"
    filtered_df = df[mask]
    return filtered_df

def drop_incomplete_metrics(df):
    no_null = df.dropna(subset=["val_accuracy"])
    return no_null