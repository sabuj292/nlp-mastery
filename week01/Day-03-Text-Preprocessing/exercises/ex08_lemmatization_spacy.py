"""
Exercise 08 — Lemmatization with spaCy (requires en_core_web_sm)
"""
"""
Goal: Reduce words to their dictionary form (lemma) while considering grammar and meaning.
E.g., "better" → "good", "running" → "run".
"""



import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise SystemExit("Please run: python -m spacy download en_core_web_sm")
doc = nlp("The striped bats are hanging on their feet for best")
print([(t.text, t.lemma_) for t in doc])



"""
Lemmatization
Definition: Uses vocabulary + morphology to get a valid base form (lemma).

Requires POS tagging to get accurate results.


Lemmatization preserves true dictionary form, ensuring consistent meaning in highly sensitive contexts.
"""

"""
Expert advice:

For search engines or quick text normalization, use stemming.
For tasks needing semantic precision (QA systems, summarization), use lemmatization.
"""

# ---------------Terminologies------------------

# POS Tagging (Part-of-Speech Tagging)
"""
Definition: The process of labeling each word in a sentence with its grammatical category (noun, verb, adjective, etc.).

Why important for lemmatization?

The base form (lemma) of a word depends on its POS.

"better" → lemma "good" (when adjective) vs "better" → lemma "better" (when verb, e.g., to better something).
"""




# en_core_web_sm
"""
A small English model for spaCy.

Contains:

    Tokenizer rules

    POS tagger

    Lemmatizer

    Named Entity Recognizer (NER)

Why “small”?

It’s lighter and faster but less accurate than en_core_web_md (medium) or en_core_web_lg (large).
"""

"""
 Expert note:
For production tasks needing high accuracy in POS tagging & lemmatization, use en_core_web_md or en_core_web_lg (they have word vectors and richer context).
"""


"""
What is spaCy?
    spaCy is an industrial-strength NLP library in Python.

    Built for production use: fast, efficient, and easy to integrate into real-world applications.

    Maintained by Explosion AI.


"""