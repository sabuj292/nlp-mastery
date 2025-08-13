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


# STEP 3 — Function 1: Lowercasing
def to_lower(text: str) -> str:
    return text.lower()

# We'll keep a working copy to add columns step-by-step
df_work = df_raw[["label","text"]].copy()
df_work["text_lower"] = df_work["text"].apply(to_lower)

print("Lowercasing preview (5 rows):")
print(df_work.sample(5, random_state=2025)[["text","text_lower"]].to_string(index=False))



# STEP 4 — Function 2: Punctuation removal
import string

# Include smart quotes/dashes/ellipsis beyond ASCII punctuation
SMART_PUNCT = "“”‘’—–…"
PUNCT_TABLE = str.maketrans("", "", string.punctuation + SMART_PUNCT)

def remove_punct(text: str) -> str:
    return text.translate(PUNCT_TABLE)

# Apply to the lowercased text from Step 3
df_work["text_nopunct"] = df_work["text_lower"].apply(remove_punct)

print("Punctuation removal preview (6 rows):")
print(df_work.sample(6, random_state=606)[["text_lower","text_nopunct"]].to_string(index=False))

# Quick sanity check: how many rows changed?
changed = (df_work["text_lower"] != df_work["text_nopunct"]).sum()
print(f"\nRows altered by punctuation removal: {changed} / {len(df_work)}")


# Step 5: Tokenization + Stopword removal 

# Step 5A — Tokenize

# STEP 5A — Tokenize the punctuation-stripped text
from nltk.tokenize import word_tokenize

def tokenize(text: str):
    return word_tokenize(text)

df_work["tokens"] = df_work["text_nopunct"].apply(tokenize)

print("Tokenization preview (5 rows):")
print(df_work.sample(5, random_state=505)[["text_nopunct","tokens"]].to_string(index=False))

print("\nToken count stats (before stopword removal):")
lens = df_work["tokens"].apply(len)
print("min/mean/median/max =", lens.min(), round(lens.mean(),2), lens.median(), lens.max())


#  Step 5B — Remove stopwords

# STEP 5B — Remove stopwords
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words("english"))

def remove_stopwords(tokens):
    return [t for t in tokens if t.lower() not in STOPWORDS]

df_work["tokens_nostop"] = df_work["tokens"].apply(remove_stopwords)

print("Stopword removal preview (6 rows):")
print(df_work.sample(6, random_state=606)[["tokens","tokens_nostop"]].to_string(index=False))

print("\nToken count stats (after stopword removal):")
lens2 = df_work["tokens_nostop"].apply(len)
print("min/mean/median/max =", lens2.min(), round(lens2.mean(),2), lens2.median(), lens2.max())
print("\nAverage reduction in tokens:", round((lens.mean()-lens2.mean()),2))




# STEP 6 — POS-aware lemmatization
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# 6.1 Map NLTK POS (Treebank) -> WordNet POS
def get_wordnet_pos(tag: str):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default

lemmatizer = WordNetLemmatizer()

# 6.2 POS tag and lemma
def pos_lemmatize(tokens):
    # POS tag the token list
    pos_tags = nltk.pos_tag(tokens)
    # Lemmatize using POS mapping
    return [lemmatizer.lemmatize(w, get_wordnet_pos(tag)) for w, tag in pos_tags]

df_work["tokens_lemma"] = df_work["tokens_nostop"].apply(pos_lemmatize)

print("Lemmatization preview (6 rows):")
print(
    df_work.sample(6, random_state=706)[
        ["tokens_nostop", "tokens_lemma"]
    ].to_string(index=False)
)

# Quick delta check: how many tokens changed by lemmatization?
changed_counts = [
    sum(1 for a,b in zip(a_list, b_list) if a != b)
    for a_list, b_list in zip(df_work["tokens_nostop"], df_work["tokens_lemma"])
]
print("\nAvg tokens changed by lemmatization (per row):", round(sum(changed_counts)/len(changed_counts), 3))




# STEP 7 — Whitespace cleanup & assemble final clean_text

def detokenize(tokens):
    # Join with single spaces and strip ends
    return " ".join(tokens).strip()

# Build the final clean_text column from tokens_lemma
df_work["clean_text"] = df_work["tokens_lemma"].apply(detokenize)

# Preview: before vs after for 5 random rows
import pandas as pd
pd.set_option("display.max_colwidth", 160)

preview = df_work.sample(5, random_state=777)[["text", "clean_text"]]
print("Before vs After (5 samples):")
print(preview.to_string(index=False))

# Quick sanity checks
num_empty = (df_work["clean_text"].str.len() == 0).sum()
print(f"\nEmpty cleaned rows: {num_empty} / {len(df_work)}")
