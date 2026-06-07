import pandas as pd

def load_data():
    runs_df = pd.read_csv("output/runs.csv")
    registry_df = pd.read_csv("output/model_registry.csv")
    return (runs_df, registry_df)

    