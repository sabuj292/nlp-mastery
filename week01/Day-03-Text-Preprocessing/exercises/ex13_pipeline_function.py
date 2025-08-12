def preprocess(text, lowercase=True):
    if lowercase:
        text = text.lower()
    return text
print(preprocess("Hello NLP"))
