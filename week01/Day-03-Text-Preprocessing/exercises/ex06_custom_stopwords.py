"""
Exercise 06 — Remove stopwords WITHOUT nltk list (custom)
"""
text = "this is a simple test for custom stopword removal in nlp"
custom_stop = {"a","the","is","in","for","this"}
tokens = text.split()
print([t for t in tokens if t not in custom_stop])


"""
In many ML pipelines, stopword removal is task-driven, not blanket-applied. For transformer models (BERT, GPT), we rarely remove stopwords at all — the model’s attention mechanism can learn to down-weight them.
"""

"""
 Pro tip: In critical NLP tasks, never remove negations without handling them explicitly.
"""

"""
Stopword lists vary — NLTK, SpaCy, sklearn all have different sets.

Removing stopwords can sometimes hurt performance (e.g., “not good” → removing “not” changes meaning).

Use task-dependent judgment — for sentiment analysis, negations like “not” are critical.
"""