import numpy as np

docs = ["I love NLP", "I love AI", "AI loves me"]

# Step -01: build vocabulary

vocab = sorted(set(
    word.lower() for doc in docs for word in doc.split()
))
