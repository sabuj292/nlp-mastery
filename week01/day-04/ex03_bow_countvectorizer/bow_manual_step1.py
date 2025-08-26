# bow_manual_step1.py
import re
from pathlib import Path

# 1) read docs (one line per doc)
p = Path("data/tiny_corpus.txt")
docs = [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

# 2) simple normalizer: lowercase + replace urls/emails + normalize punctuation
def simple_normalize(s: str) -> str:
    s = s.lower()
    s = re.sub(r"https?://\S+", " URL ", s)    # replace urls
    s = re.sub(r"\S+@\S+\.\S+", " EMAIL ", s)  # replace emails
    s = s.replace("…", " ").replace("—", " ").replace("–", " ")
    return s

# 3) token pattern: words made of letters/numbers/hyphens
TOKEN_RE = re.compile(r"[a-z0-9\-]+")

def tokenize(s: str):
    return TOKEN_RE.findall(simple_normalize(s))

# 4) tokenize each doc and print
for i, d in enumerate(docs):
    toks = tokenize(d)
    print(f"doc {i}: {toks}")
