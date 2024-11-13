import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv("dataset.csv")

print(df.count())

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print("***********************")

print(df.count())

timestamp = str(datetime.now())

timestamp = timestamp[:10]

size = len(df["Link"])

timestamps = [timestamp for i in range(size)]

df["Timestamp"] = timestamps

df.to_csv("dataset.csv", index=False)
