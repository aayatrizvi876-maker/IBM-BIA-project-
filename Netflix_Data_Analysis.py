# NETFLIX MOVIES & TV SHOWS — DATA ANALYSIS AND VISUALIZATION
# Student: Aayat Rizvi | UU ID: 250510217 | BBA-IBM
# Dataset note: bundled CSV is a synthetic educational sample, not Netflix's real catalog.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("netflix_sample_dataset.csv")
print("Dataset dimensions:", df.shape)
print("\\nData types:")
print(df.dtypes)
print("\\nMissing values before cleaning:")
print(df.isna().sum())

# 2. Data cleaning
df = df.drop_duplicates()
for col in ["director", "country", "rating"]:
    df[col] = df[col].fillna("Not Specified")
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

print("\\nMissing values after cleaning:")
print(df.isna().sum())

# 3. Descriptive analysis
print("\\nContent type counts:")
print(df["type"].value_counts())
print("\\nRelease-year descriptive statistics:")
print(df["release_year"].describe())
print("\\nTop countries:")
print(df["country"].value_counts().head(10))
print("\\nGenre counts:")
print(df["listed_in"].value_counts())
print("\\nRating by content type:")
print(pd.crosstab(df["type"], df["rating"]))

# 4. Visualization
sns.set_theme(style="whitegrid")

df["type"].value_counts().plot(kind="bar", title="Titles by Content Type")
plt.xlabel("Content Type"); plt.ylabel("Count"); plt.xticks(rotation=0); plt.tight_layout(); plt.show()

df["release_year"].value_counts().sort_index().plot(kind="line", figsize=(10,4), marker="o")
plt.title("Titles by Release Year"); plt.xlabel("Release Year"); plt.ylabel("Count"); plt.tight_layout(); plt.show()

df["country"].value_counts().head(8).sort_values().plot(kind="barh", figsize=(8,4))
plt.title("Top Countries by Title Count"); plt.xlabel("Count"); plt.ylabel("Country"); plt.tight_layout(); plt.show()

df["listed_in"].value_counts().sort_values().plot(kind="barh", figsize=(8,4))
plt.title("Genre Distribution"); plt.xlabel("Count"); plt.ylabel("Genre"); plt.tight_layout(); plt.show()

pd.crosstab(df["type"], df["rating"]).plot(kind="bar", stacked=True, figsize=(9,4))
plt.title("Ratings by Content Type"); plt.xlabel("Content Type"); plt.ylabel("Count"); plt.tight_layout(); plt.show()

# 5. Export tables
df["type"].value_counts().to_csv("content_type_counts.csv")
df["country"].value_counts().head(10).to_csv("top_countries.csv")
pd.crosstab(df["type"], df["rating"]).to_csv("rating_by_content_type.csv")
