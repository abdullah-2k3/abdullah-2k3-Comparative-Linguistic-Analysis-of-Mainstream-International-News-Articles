import pandas as pd
import numpy as np
from datetime import datetime
import re

df = pd.read_csv("Islamophobia_Dataset.csv")

print(df.count())

df.dropna(subset="Article_Content", inplace=True)
df.drop_duplicates(subset=["Headline", "Article_Content"], inplace=True)
df.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12"], inplace=True)

print("***********************")

print(df.count())

df.to_csv("Islamophobia_Dataset.csv", index=False)

# articles = np.array(df["Article_Content"])


# def clean_article_text(article):
#     return re.sub(r"\n+", "", str(article)).strip()


# cleaned_articles = np.array([clean_article_text(article) for article in articles])

# df["Article_Content"] = cleaned_articles

# timestamp = str(datetime.now())

# timestamp = timestamp[:10]

# size = len(df["Link"])

# timestamps = [timestamp for i in range(size)]

# df["Timestamp"] = timestamps

# df.to_csv("trt_articles_Islamophobia.csv", index=False)
