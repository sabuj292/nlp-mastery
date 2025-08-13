<!-- Badges -->
[![Status: Day 3 Completed](https://img.shields.io/badge/NLP%20Mastery-Day%203%20Completed-brightgreen)](./)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tools](https://img.shields.io/badge/Tools-NLTK%20%7C%20spaCy%20%7C%20Regex-lightgrey)

# NLP Mastery — Week 01 · Day 03 — Text Preprocessing & Cleaning

**Mission:** Convert raw, messy text into model‑ready form **without losing meaning**.

## Why this matters
Clean text reduces vocabulary size, improves model accuracy, and prevents noise from overpowering signal.  
Bad preprocessing → garbage in, garbage out.

---

## Topics covered
- Lowercasing, punctuation, numbers, whitespace normalization
- Tokenization: word, sentence, subword (theory)
- Stopwords: when to remove/keep (negation handling)
- Stemming vs Lemmatization (Porter, WordNet, spaCy)
- Emojis, HTML, Unicode normalization, multilingual quirks
- Robust, configurable preprocessing **pipelines**
- Mini visualizations (length histograms, token/bigram bars)
- CSV export + simple **CLI** for batch cleaning

---

## Repo layout (Day‑03)
```
Day-03-Text-Preprocessing/
├─ README.md
├─ requirements.txt                 # Day-03 deps
├─ exercises/
│  ├─ ex01_lowercase.py
│  ├─ ex02_remove_punctuation.py
│  ├─ ex03_remove_numbers.py
│  ├─ ex04_normalize_spaces.py
│  ├─ ex05_word_tokenize.py
│  ├─ ex06_custom_stopwords.py
│  ├─ ex07_stemming_porter.py
│  ├─ ex08_lemmatization_spacy.py
│  ├─ ex09_regex_remove_urls.py
│  ├─ ex10_extract_hashtags.py
│  ├─ ex11_tokenizer_preserve_emojis.py
│  ├─ ex12_emojis_to_words.py
│  ├─ ex13_pipeline_configurable.py
│  └─ ex14_unicode_normalization.py
├─ mini_project/
│  ├─ src/
│  │  └─ cleaning.py               # Basic + Advanced cleaners (importable)
│  ├─ scripts/
│  │  └─ run_cleaning.py           # CLI runner (batch clean CSV -> outputs/cleaned_cli.csv)
│  ├─ mini_project.ipynb           # Guided notebook
│  ├─ mini_project.py              # Script version (same logic as notebook)
│  ├─ cleaned_twitter_samples.csv  # (example dataset or generated)
│  ├─ cleaned_twitter_samples_advanced.csv
│  ├─ hist_len_chars_before.png
│  ├─ hist_len_chars_after.png
│  ├─ top20_tokens_after.png
│  └─ top15_bigrams_after.png
└─ data/
   └─ sample_tweets.txt
```
> **Note:** `tweet_cleaner.py` is superseded by `mini_project/src/cleaning.py` and the CLI `mini_project/scripts/run_cleaning.py`. Keep the old file only for legacy reference.

---

## Quickstart

### 1) Create & activate a virtual environment

**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install requirements
```bash
pip install -r Day-03-Text-Preprocessing/requirements.txt
```

### 3) Download NLP resources (one‑time)
**spaCy model (used in exercises):**
```bash
python -m spacy download en_core_web_sm
```

**NLTK data** (NLTK ≥ 3.9 includes `punkt_tab`):
```bash
python - << 'PY'
import nltk
for p in ["punkt","punkt_tab","stopwords","wordnet","averaged_perceptron_tagger","omw-1.4"]:
    try:
        nltk.download(p)
    except Exception as e:
        print("Failed:", p, e)
print("NLTK data downloaded.")
PY
```

> **VS Code tip:** `Ctrl+Shift+P → Python: Select Interpreter → .venv/.../python`

---

## How to run

### A) Run an exercise
```bash
python Day-03-Text-Preprocessing/exercises/ex05_word_tokenize.py
```

### B) Run the **mini‑project notebook**
Open:
```
Day-03-Text-Preprocessing/mini_project/mini_project.ipynb
```
Import the cleaner in a cell:
```python
from src.cleaning import clean_text_basic, clean_text_advanced
```

### C) Run the **mini‑project CLI** (recommended for batch CSVs)

From **inside** `Day-03-Text-Preprocessing/mini_project/`:
```bash
python scripts/run_cleaning.py --input_csv cleaned_twitter_samples.csv --out_csv outputs/cleaned_cli.csv --mode advanced
```

Or from the **repo root** (Windows path example):
```bash
python ".\Day-03-Text-Preprocessing\mini_project\scripts
un_cleaning.py" ^
  --input_csv ".\Day-03-Text-Preprocessing\mini_project\cleaned_twitter_samples.csv" ^
  --out_csv ".\Day-03-Text-Preprocessing\mini_project\outputs\cleaned_cli.csv" ^
  --mode advanced
```

**Use your own data:** your CSV must have a column named **`text`**.
```bash
python scripts/run_cleaning.py --input_csv path/to/your.csv --out_csv outputs/cleaned_your.csv --mode advanced
```

---

## Mini‑project cleaner (what it does)

**Basic (`clean_text_basic`)**
- lowercase → remove punctuation → tokenize (NLTK) → remove stopwords → POS‑tag → WordNet‑lemmatize → join

**Advanced (`clean_text_advanced`)**
- lowercase → Unicode normalization (smart quotes/dashes; optional accent folding; small emoji map)
- contractions expansion (e.g., `i'm → i am`, `can't → can not`)
- URL/HTML normalization (`<URL>` token, strip tags)
- then the same steps as **Basic**

Import in Python:
```python
from src.cleaning import clean_text_basic, clean_text_advanced
```

---

## Expected output (examples)
CLI output: `outputs/cleaned_cli.csv` with a `clean_text` column.  
Typical notebook plots:
- `hist_len_chars_before.png` vs `hist_len_chars_after.png`
- `top20_tokens_after.png`
- `top15_bigrams_after.png`

---

## Troubleshooting
**`ModuleNotFoundError: No module named 'src'`**  
Run the CLI **inside** `mini_project/` (the script also adjusts `sys.path`, but the safest is to run from the folder).

**NLTK LookupError**  
Run the NLTK download block again **in the active venv**.

**spaCy not found / model missing**  
`pip install -r requirements.txt` then `python -m spacy download en_core_web_sm`.

**CSV lacks `text` column**  
Rename your text column to exactly `text` or adapt the script.

---

## Contributing
- Keep scripts **small, runnable, documented**.
- Prefer standard libs; add dependencies only when they clearly help.
- New exercises: `exNN_description.py` with a docstring + tiny demo.

---

## Acknowledgments
Part of **NLP Mastery — Week 01 · Day 03: Text Preprocessing & Cleaning**.
