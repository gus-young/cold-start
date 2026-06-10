def accuracy_by_model(df):    
    model_means = df.groupby("model_type")["val_accuracy"].mean().sort_values(ascending = False)
    return model_means

def accuracy_stats(df):
    model_stats = df.groupby('model_type')['val_accuracy'].agg(['std', 'min', 'max', 'count'])
    return model_stats

def accuracy_by_model_and_dataset(df):
    model_and_dataset = df.groupby(['model_type', 'dataset'])['val_accuracy'].mean()
    model_and_dataset_df = model_and_dataset.unstack()
    return model_and_dataset_df

def overfit_rate_by_model(df):
    overfit_pct = df['is_overfit'].mean()
    return overfit_pct

def speed_by_model(df):
    speeds = df.groupby('model_type')['train_time_seconds'].agg(['mean', 'median']).sort_values(by = 'mean', ascending = True)
    return speeds