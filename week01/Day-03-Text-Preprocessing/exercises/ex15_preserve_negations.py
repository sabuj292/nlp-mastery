"""
Exercise 15 — Stopword removal that preserves negations
"""
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

neg_keep = {"not","no","nor","n't"}
stops = set(stopwords.words("english"))
stops = {w for w in stops if w not in neg_keep}

text = "I am not happy with this product and I do not recommend it"
tokens = text.lower().split()
print([t for t in tokens if t not in stops])
