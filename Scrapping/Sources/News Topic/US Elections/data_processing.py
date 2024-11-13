import pandas as pd
import numpy as np
import re

filename = "US_Elections_Dataset.csv"
df = pd.read_csv(filename)

print(df.info())
print(df.count())
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("-----------------------")
print(df.info())
print(df.count())

df.to_csv(filename, index=False)

# articles = np.array(df["Article_Content"])

# print(articles[0])

# print("***************************************************")


# def clean_article_text(article):
#     return re.sub(r"\n+", "\n", str(article)).strip()


# cleaned_articles = np.array([clean_article_text(article) for article in articles])

# df["Article_Content"] = cleaned_articles


# print(cleaned_articles[0])
