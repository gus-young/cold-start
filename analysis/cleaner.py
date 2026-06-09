def filter_completed(df):
    mask = df['status'] == "completed"
    filtered_df = df[mask]
    return filtered_df

def drop_incomplete_metrics(df):
    df = df.dropna(subset=["val_accuracy"])
    return df

def normalize_model_type(df):
    df["model_type"] = df["model_type"].str.strip().str.lower()
    return df

def flag_ovefitting(df, threshold=0.05):
    df['is_overfit'] = df['train_accuracy'] - df['val_accuracy'] > threshold
    return df

def clean(df):
    dafa_filtered = filter_completed(df)
    data_no_incomplete = drop_incomplete_metrics(dafa_filtered)
    data_normalized = normalize_model_type(data_no_incomplete)
    data_complete = flag_ovefitting(data_normalized)
    return data_complete