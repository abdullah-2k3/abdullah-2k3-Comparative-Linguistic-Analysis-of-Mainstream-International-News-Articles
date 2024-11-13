import pandas as pd
import numpy as np

filename1 = "Dawn News_articles_Israel War.csv"
df1 = pd.read_csv(filename1)

filename2 = "Dawn News_articles_Ukraine War.csv"
df2 = pd.read_csv(filename2)

merged_df = pd.concat([df1, df2], ignore_index=True)


timestamps = np.array(merged_df["Timestamp"])

# Filter the timestamps to keep only the date (YYYY-MM-DD)
filtered_timestamps = [
    ts.split()[0] for ts in timestamps
]  # Splitting and taking only the date part

# Update the "Timestamp" column in the DataFrame
merged_df["Timestamp"] = filtered_timestamps

merged_filename = "Dawn_links_merged.csv"
merged_df.to_csv(merged_filename, index=False)

print(f"Merged DataFrame saved to {merged_filename}.")

# df = pd.read_csv(filename)


# print(df.head())
# print(df.info())

# df = df.drop_duplicates()

# print("----------------")

# print(df.head())
# print(df.info())
