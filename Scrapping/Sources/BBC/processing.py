import pandas as pd
import numpy as np
import re


filename = "bbc_articles_US_elections.csv"
df = pd.read_csv(filename)

# timestamps = np.array(df["Timestamp"])

# # Filter the timestamps to keep only the date (YYYY-MM-DD)
# filtered_timestamps = [
#     ts.split()[0] for ts in timestamps
# ]  # Splitting and taking only the date part

# # Update the "Timestamp" column in the DataFrame
# df["Timestamp"] = filtered_timestamps

# # Optionally, you can save the modified DataFrame back to a CSV file

# print("Timestamps filtered successfully and saved to filtered_dataset.csv.")

print(df.count())

df = df.drop_duplicates()
df = df.dropna()


print(df.head())
print(df.count())

df.to_csv(filename, index=False)

# articles = np.array(df["Article_Content"])

# print(articles[0])

# print("***************************************************888")

# def clean_article_text(article):
#     return re.sub(r"\n+", "", article).strip()


# cleaned_articles = np.array([clean_article_text(article) for article in articles])

# df["Article_Content"] = cleaned_articles

# df.to_csv("CNN_articles_US_elections.csv", index=False)
