"""
Exercise 02 — Remove punctuation
"""
import string
text = "Hello!!! NLP, is fun... right?"
tbl = str.maketrans('', '', string.punctuation)
print(text.translate(tbl))
