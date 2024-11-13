import pandas as pd
import numpy as np


filename = "trt_articles_Merged_with_content.csv"
df = pd.read_csv(filename)

print(df.count())

df = df.dropna()


print(df.head())
print(df.count())

# articles = df["Article_Content"]

# for article in articles:
#     print(article)
#     print("----------------------------------------")
