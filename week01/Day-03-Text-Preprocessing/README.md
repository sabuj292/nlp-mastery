# NLP Mastery — Day 3: Text Preprocessing & Cleaning

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

## Quickstart
Create a virtual environment and install basics:
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install nltk spacy emoji unidecode beautifulsoup4
python -m spacy download en_core_web_sm  # needed for spaCy lemmatization
python -c "import nltk; [__import__('nltk').download(pkg) for pkg in ['punkt','stopwords','wordnet']]"
```

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

## How to run
Each `ex*.py` is standalone. For example:
```bash
python exercises/ex11_tokenizer_preserve_emojis.py
```
Mini-project:
```bash
python mini_project/tweet_cleaner.py --input data/sample_tweets.txt --output cleaned_tokens.json
```

## Practice checklist
- [ ] I can build a pipeline with toggles (lowercase, punctuation, numbers, stopwords, emojis).
- [ ] I can preserve negations while removing other stopwords.
- [ ] I can demojize and/or keep emojis as tokens.
- [ ] I can produce clean tokens suitable for sentiment/topic modeling.

## Next steps
- Benchmark with/without each step on a small classifier (Day 4 preview).
- Write a short blog post summarizing lessons + code snippets.
