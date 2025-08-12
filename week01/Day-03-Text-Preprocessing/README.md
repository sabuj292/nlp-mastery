<!-- Badges -->
[![Status: Day 3 Completed](https://img.shields.io/badge/NLP%20Mastery-Day%203%20Completed-brightgreen)](./)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tools](https://img.shields.io/badge/Tools-NLTK%20%7C%20spaCy%20%7C%20Regex-lightgrey)

# NLP Mastery — Week 01 · Day 03 — Text Preprocessing & Cleaning

**Mission:** Convert raw, messy text into model-ready form without losing meaning.

## Why this matters
Clean text reduces vocabulary size, improves model accuracy, and prevents noise from dominating signal.
Bad preprocessing = garbage in, garbage out.

## Topics covered
- Lowercasing, punctuation, numbers, whitespace normalization
- Tokenization: word, sentence, subword (theory)
- Stopwords: when to remove/keep (negation handling)
- Stemming vs Lemmatization (Porter, WordNet, spaCy)
- Emojis, HTML, Unicode normalization, multilingual quirks
- Robust, configurable preprocessing pipelines




## Repo layout
```
Day-03-Text-Preprocessing/
├── README.md
├── requirements.txt
├── exercises/
│   ├── ex01_lowercase.py
│   ├── ex02_remove_punctuation.py
│   ├── ex03_remove_numbers.py
│   ├── ex04_normalize_spaces.py
│   ├── ex05_word_tokenize.py
│   ├── ex06_custom_stopwords.py
│   ├── ex07_stemming_porter.py
│   ├── ex08_lemmatization_spacy.py
│   ├── ex09_regex_remove_urls.py
│   ├── ex10_extract_hashtags.py
│   ├── ex11_tokenizer_preserve_emojis.py
│   ├── ex12_emojis_to_words.py
│   ├── ex13_pipeline_configurable.py
│   ├── ex14_unicode_normalization.py
│   ├── ex15_preserve_negations.py
├── mini_project/
│   └── tweet_cleaner.py
└── data/
    └── sample_tweets.txt
```
## Quickstart
Create a virtual environment and install basics:
<!-- ```bash
python -m venv .venv && source .venv/bin/activate  
pip install nltk spacy emoji unidecode beautifulsoup4
python -m spacy download en_core_web_sm  # needed for spaCy lemmatization
python -c "import nltk; [__import__('nltk').download(pkg) for pkg in ['punkt','stopwords','wordnet']]"
``` -->

> **Windows (PowerShell)**
```powershell
python -m venv .venv; .\.venv\Scriptsctivate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -c "import nltk; [nltk.download(p) for p in ['punkt','punkt_tab','stopwords','wordnet']]"
python .\mini_project	weet_cleaner.py --input .\data\sample_tweets.txt --output cleaned_tokens.json
```

> **macOS / Linux**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python - <<'PY'
import nltk
for p in ["punkt","punkt_tab","stopwords","wordnet"]:
    nltk.download(p)
PY
python ./mini_project/tweet_cleaner.py --input ./data/sample_tweets.txt --output cleaned_tokens.json
```

> **VS Code tip:** `Ctrl+Shift+P → Python: Select Interpreter → .venv/.../python`.

---

## 🧰 Requirements
- Python **3.10+**, `pip`
- Packages (installed via `requirements.txt`): `nltk`, `spacy`, `emoji`, `unidecode`, `beautifulsoup4`
- spaCy model: `en_core_web_sm`
- NLTK data: `punkt`, **`punkt_tab`** (NLTK ≥ 3.9), `stopwords`, `wordnet`

---

## 🏃 How to Run

### Exercises
```bash
# example: word tokenization
python ./exercises/ex05_word_tokenize.py
```

### Mini-Project: Tweet Cleaner (CLI)
Cleans tweets by removing URLs/mentions, stripping `#` while keeping words, handling emojis, and removing stopwords (preserves negations: “not”, “no”, “n't”).

**Basic**
```bash
python ./mini_project/tweet_cleaner.py --input ./data/sample_tweets.txt --output cleaned_tokens.json
```

**Options**
```text
--demojize      Convert emojis to words (e.g., ❤️ -> :red_heart:)
--drop-emojis   Remove emojis entirely
```

**Examples**
```bash
python ./mini_project/tweet_cleaner.py --input ./data/sample_tweets.txt --output cleaned_demojized.json --demojize
python ./mini_project/tweet_cleaner.py --input ./data/sample_tweets.txt --output cleaned_noemoji.json --drop-emojis
```

---

## ✅ Expected Output (mini-project)
`cleaned_tokens.json` (snippet):
```json
[
  {"original": "@John I ❤️ NLP! Check https://nlp.com #AI #NLP", "tokens": ["love","nlp","check","ai","nlp"]},
  {"original": "Feeling great today 😀😀 #happy", "tokens": ["feeling","great","today","happy"]}
]
```

---

## 🔧 Troubleshooting

**NLTK: `Resource 'punkt_tab' not found`**  
```bash
python -c "import nltk; nltk.download('punkt_tab')"
```

**`ModuleNotFoundError` (e.g., `spacy`, `emoji`)**  
Ensure venv is active and run:
```bash
pip install -r requirements.txt
```

**VS Code runs the wrong Python**  
`Ctrl+Shift+P → Python: Select Interpreter → .venv/Scripts/python.exe`.

---

## How to run
Each `ex*.py` is standalone. For example:
```bash
python exercises/ex11_tokenizer_preserve_emojis.py
```
Mini-project:
```bash
python mini_project/tweet_cleaner.py --input data/sample_tweets.txt --output cleaned_tokens.json
```

## 🤝 Contributing
- Keep scripts **small, runnable, documented**.
- Prefer standard libs; add dependencies only when it clearly helps.
- New exercises: `exNN_description.py` with a short docstring and a tiny demo.



## ⭐ Acknowledgments
Part of **NLP Mastery** — Week 01 · **Day 03: Text Preprocessing & Cleaning**.
