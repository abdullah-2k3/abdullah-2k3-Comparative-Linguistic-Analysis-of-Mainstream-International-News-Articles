import pandas as pd
import numpy as np
from datetime import datetime
import pandas as pd
import re

# Load the CSV file into a DataFrame
df = pd.read_csv("Dataset_Articles.csv")

# # Print the count of non-null entries for each column before cleaning
print("Before cleaning:")
print(df.count())

# # Drop rows where the 'Link' column has NaN values (if any)
df.dropna(inplace=True)

# # Drop duplicate rows based only on the 'Link' column
df.drop_duplicates(inplace=True)

# # Print a separator for clarity
print("***********************")

# # Print the count of non-null entries for each column after cleaning
print("After cleaning:")
print(df.count())


articles = np.array(df["Article_Content"])


def clean_article_text(article):
    return re.sub(r"\n+", "", str(article)).strip()


cleaned_articles = np.array([clean_article_text(article) for article in articles])

df["Article_Content"] = cleaned_articles

df.to_csv("Dataset.csv", index=False)

# timestamp = str(datetime.now())

# timestamp = timestamp[:10]

# size = len(df["Link"])

# timestamps = [timestamp for i in range(size)]

# print(df["Timestamp"])
# df["Timestamp"] = timestamps

# print(df["Timestamp"])
# df.to_csv("Dataset.csv", index=False)
