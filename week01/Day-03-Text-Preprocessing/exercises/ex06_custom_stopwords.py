"""
Exercise 06 — Remove stopwords WITHOUT nltk list (custom)
"""
text = "this is a simple test for custom stopword removal in nlp"
custom_stop = {"a","the","is","in","for","this"}
tokens = text.split()
print([t for t in tokens if t not in custom_stop])
