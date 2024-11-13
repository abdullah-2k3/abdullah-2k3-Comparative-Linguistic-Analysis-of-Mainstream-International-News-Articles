import pandas as pd


filename = "cnn_articles_israel_updated.csv"
df = pd.read_csv(filename)

print(df.count())

print("Nulls....")
print(df.isna().sum())

df_cleaned = df.dropna()

df_withna = df[df["Article_Content"].isna()]


print("df Cleaned...")
print(df_cleaned.count())
print(df_cleaned.isna().sum())
print(df_cleaned.head())


print("df with na...")
print(df_withna.count())
print(df_withna.isna().sum())
print(df_withna.head())

# df_cleaned.to_csv("cnn_articles_israel_cleaned.csv", index=False)
df_withna.to_csv("cnn_articles_israel_fetch.csv", index=False)

print("csv files created")
