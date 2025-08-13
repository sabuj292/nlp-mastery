"""
Exercise 02 — Remove punctuation
"""
import string
text = "Hello!!! NLP, is fun... right?"
tbl = str.maketrans('', '', string.punctuation)
print(text.translate(tbl))


"""
str.maketrans('', '', string.punctuation) → creates a mapping table to remove punctuation.

We’re not splitting/joining words yet; just removing punctuation.
"""