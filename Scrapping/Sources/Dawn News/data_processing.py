import pandas as pd
import numpy as np
import re

file = "AlJazeera_articles.csv"
df = pd.read_csv(file)

# print(df.info())
# print(df.count())
# df.drop_duplicates(inplace=True)
# df.dropna(inplace=True)

# print("-----------------------")
# print(df.info())
# print(df.count())


articles = np.array(df["Article_Content"])

print(articles[0])

print("***************************************************888")


# def clean_article_text(article):
#     return re.sub(r"\n+", "\n", article).strip()


# cleaned_articles = np.array([clean_article_text(article) for article in articles])

# df["Article_Content"] = cleaned_articles

# df.to_csv("AlJazeera_articles___.csv", index=False)

# print(cleaned_articles[0])

# authors = ["AlJazeera" for i in range(len(articles))]
# df["Author"] = authors
# df.to_csv("AlJazeera_articles___.csv", index=False)
