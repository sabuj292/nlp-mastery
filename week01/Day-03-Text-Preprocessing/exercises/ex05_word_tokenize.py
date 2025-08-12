"""
Exercise 05 — Word tokenization with NLTK
"""
import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import word_tokenize
text = "I ❤️ NLP! It's amazing..."
print(word_tokenize(text))
