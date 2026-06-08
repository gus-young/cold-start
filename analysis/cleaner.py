import pandas as pd 

def filter_completed(df):
    mask = df['status'] == "completed"
    filtered_df = df[mask]
    return filtered_df