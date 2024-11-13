import pandas as pd
import numpy as np

file = "bbc_articles_cleaned.csv"

df = pd.read_csv(file)

df.head()


size = np.array(df["Author"])

authors = ["BBC" for i in range(len(size))]

df["Author"] = authors

df.to_csv("BBC_articles.csv", index=False)
print("File saved...")
