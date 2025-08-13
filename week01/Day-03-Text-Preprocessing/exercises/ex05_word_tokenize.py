"""
Exercise 05 — Word tokenization with NLTK
"""
import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import word_tokenize
text = "I ❤️ NLP! It's amazing..."
print(word_tokenize(text))



# ---------Sentence tokenize------------

from nltk.tokenize import sent_tokenize
sentences = sent_tokenize("Hello world! How are you? I'm fine.")
print(sentences)

# Expert tip:
"""
Modern transformer models often bypass traditional word tokenization by using subword tokenizers (BPE, WordPiece, UnigramLM). But pre-tokenization still matters for cleaning before feeding text to these tokenizers.

"""

"""
Tokenization quality heavily affects downstream performance — garbage in, garbage out. Even small mistakes (like splitting "state-of-the-art") can shift meaning.
"""