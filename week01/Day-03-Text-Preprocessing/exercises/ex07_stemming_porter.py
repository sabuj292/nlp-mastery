"""
Exercise 07 — Porter stemming
"""
import nltk
nltk.download('punkt', quiet=True)
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
text = "connections connected connecting connection"
ps = PorterStemmer()
print([ps.stem(w) for w in word_tokenize(text)])
