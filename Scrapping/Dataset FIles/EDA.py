import pandas as pd
import numpy as np
import re


df = pd.read_csv("Dataset.csv")

print(df.info())
print(df.count())
print(df.head())
# print(df["Timestamp"])

print(df.columns)


# df.dropna(inplace=True)
# df.drop_duplicates(inplace=True)

# print(df.count())

# df.to_csv("Dataset.csv", index=False)

# df = df.drop_duplicates()

# df = df.dropna()

# print("**********************************************************")

# df.info()
# print(df.count())


# def clean_article_text(article):
#     # Replace all newline characters with an empty string
#     return re.sub(r"\n", "", article).strip()


# Example usage
# Assuming df is your DataFrame and 'Article_Content' is the column name
# articles = np.array(df["Article_Content"])
# cleaned_articles = np.array([clean_article_text(article) for article in articles])

# # If you want to update the DataFrame with the cleaned content:
# df["Article_Content"] = cleaned_articles

# # Print the cleaned articles
# print(cleaned_articles)
