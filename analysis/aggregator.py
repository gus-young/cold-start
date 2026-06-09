def accuracy_by_model(df):
    #df.groupby - groups by values in column 
    # .mean() calculates mean of "val_accuracy" values in the grous
    # .sort_values(ascending = False) sorts the values descending
    
    model_means = df.groupby("model_type")["val_accuracy"].mean().sort_values(ascending = False)
    return model_means

def accuracy_stats(df):
    model_stats = df.groupby('model_type')['val_accuracy'].agg(['std', 'min', 'max', 'count'])
    return model_stats