import pandas as pd
from analysis.loader import load_data
from analysis.cleaner import filter_completed

data = load_data()
df = data[0]
print(filter_completed(df))