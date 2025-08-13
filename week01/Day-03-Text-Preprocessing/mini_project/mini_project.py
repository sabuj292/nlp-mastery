# STEP 1 — Setup & Dataset Load (Tweets)
# --------------------------------------
# If you haven't installed NLTK: pip install nltk
import random
import pandas as pd
import nltk

# Download once (keeps things cached)
nltk.download('twitter_samples')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import twitter_samples

# Load positive & negative tweets (small, clean English sample)
pos = twitter_samples.strings('positive_tweets.json')
neg = twitter_samples.strings('negative_tweets.json')

# Build a DataFrame
df_raw = pd.DataFrame(
    {"label": ["pos"] * len(pos) + ["neg"] * len(neg),
     "text":  pos + neg}
)

# Shuffle for variety and take a manageable subset if you like
df_raw = df_raw.sample(frac=1.0, random_state=42).reset_index(drop=True)
# Optionally subsample to 2,000 rows to keep it snappy:
df_raw = df_raw.head(2000)

print("Loaded dataset shape:", df_raw.shape)
print("\nFirst 5 rows:")
print(df_raw.head(5).to_string(index=False))

print("\nRandom 5 examples:")
print(df_raw.sample(5, random_state=7)[["label","text"]].to_string(index=False))



# STEP 2 — Explore the raw dataset
import pandas as pd

print("Rows:", len(df_raw))
print("Columns:", df_raw.columns.tolist())

print("\nClass balance:")
print(df_raw["label"].value_counts())

print("\nFirst 10 rows:")
print(df_raw.head(10).to_string(index=False))

# Quick length probes (rough, pre-clean)
df_raw["len_chars"]  = df_raw["text"].str.len()
df_raw["len_tokens"] = df_raw["text"].str.split().apply(len)

print("\nLength (chars) — min/mean/median/max:")
print(df_raw["len_chars"].min(), df_raw["len_chars"].mean(), df_raw["len_chars"].median(), df_raw["len_chars"].max())

print("\nLength (tokens) — min/mean/median/max:")
print(df_raw["len_tokens"].min(), df_raw["len_tokens"].mean(), df_raw["len_tokens"].median(), df_raw["len_tokens"].max())

print("\nRandom 5 raw examples:")
print(df_raw.sample(5, random_state=101)[["label","text"]].to_string(index=False))
