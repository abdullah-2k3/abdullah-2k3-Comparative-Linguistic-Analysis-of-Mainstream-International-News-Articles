import pandas as pd
import numpy as np
import re

file = "AlJazeera_articles_US_elections.csv"
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


def clean_article_text(article):
    return re.sub(r"\n+", "", str(article)).strip()


cleaned_articles = np.array([clean_article_text(article) for article in articles])

df["Article_Content"] = cleaned_articles


timestamps = np.array(df["Timestamp"])

# Filter the timestamps to keep only the date (YYYY-MM-DD)
filtered_timestamps = [
    ts.split()[0] for ts in timestamps
]  # Splitting and taking only the date part

# Update the "Timestamp" column in the DataFrame
df["Timestamp"] = filtered_timestamps

# Optionally, you can save the modified DataFrame back to a CSV file
df.to_csv(file, index=False)

print("Timestamps filtered successfully and saved to filtered_dataset.csv.")

# df.to_csv("AlJazeera_articles___.csv", index=False)
