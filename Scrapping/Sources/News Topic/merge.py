import pandas as pd
import os

dir = "./"

dataframes = []

for filename in os.listdir(dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(dir, filename)
        print(f"Reading {file_path}")
        df = pd.read_csv(file_path)
        dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)

merged_df.to_csv("dataset.csv", index=False)

print("All CSV files have been merged into dataset.csv")
