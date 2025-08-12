"""
Exercise 08 — Lemmatization with spaCy (requires en_core_web_sm)
"""
import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise SystemExit("Please run: python -m spacy download en_core_web_sm")
doc = nlp("The striped bats are hanging on their feet for best")
print([(t.text, t.lemma_) for t in doc])
