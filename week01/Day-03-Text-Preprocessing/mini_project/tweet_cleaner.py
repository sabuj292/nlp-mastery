"""
Mini-Project: Tweet Cleaner
Usage:
  python mini_project/tweet_cleaner.py --input data/sample_tweets.txt --output cleaned_tokens.json
"""

import re, json, argparse
from typing import List
import nltk

import nltk
def _ensure_nltk():
    try: nltk.data.find('tokenizers/punkt')
    except LookupError: nltk.download('punkt', quiet=True)
    try: nltk.data.find('tokenizers/punkt_tab')
    except LookupError: nltk.download('punkt_tab', quiet=True)
    try: nltk.data.find('corpora/stopwords')
    except LookupError: nltk.download('stopwords', quiet=True)
_ensure_nltk()

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import emoji

URL = re.compile(r"(https?://\S+|www\.\S+)")
MENTION = re.compile(r"@\w+")
HASHTAG = re.compile(r"#(\w+)")  # capture word only

def clean_tweet(text: str, keep_emojis: bool = True, demojize: bool = False) -> List[str]:
    # 1) normalize case
    text = text.lower()
    # 2) remove urls and mentions
    text = URL.sub("", text)
    text = MENTION.sub("", text)
    # 3) keep words from hashtags (#love -> love)
    text = HASHTAG.sub(r"\1", text)
    # 4) tokenize
    tokens = word_tokenize(text)
    # 5) optional emoji handling
    if demojize:
        tokens = [emoji.demojize(t) for t in tokens]
    elif not keep_emojis:
        tokens = [t for t in tokens if not any(ch in emoji.EMOJI_DATA for ch in t)]
    # 6) remove stopwords (preserve negations)
    neg_keep = {"not","no","nor","n't"}
    stops = set(stopwords.words("english"))
    stops = {w for w in stops if w not in neg_keep}
    tokens = [t for t in tokens if t.isalpha() and t not in stops]
    return tokens

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--demojize", action="store_true", help="convert emojis to words")
    ap.add_argument("--drop-emojis", action="store_true", help="remove emojis")
    args = ap.parse_args()

    cleaned = []
    with open(args.input, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tokens = clean_tweet(line, keep_emojis=not args.drop_emojis, demojize=args.demojize)
            cleaned.append({"original": line, "tokens": tokens})

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(cleaned)} cleaned tweets to {args.output}")

if __name__ == "__main__":
    main()
