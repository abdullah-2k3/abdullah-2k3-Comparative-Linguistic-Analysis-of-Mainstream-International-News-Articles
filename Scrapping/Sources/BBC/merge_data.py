import pandas as pd

# filename1 = "BBC_articles_Israel War.csv"
# df1 = pd.read_csv(filename1)

# filename2 = "BBC_articles_Ukraine War.csv"
# df2 = pd.read_csv(filename2)

# merged_df = pd.concat([df1, df2], ignore_index=True)

filename = "bbc_article_links_merged.csv"
# merged_df.to_csv(merged_filename, index=False)

# print(f"Merged DataFrame saved to {merged_filename}.")

df = pd.read_csv(filename)


print(df.head())
print(df.info())

df = df.drop_duplicates()

print("----------------")

print(df.head())
print(df.info())
