# Exercise: stemming
"""
Goal: Reduce words to their root form (without caring about grammar or dictionary correctness).
This helps group similar words: "running", "runs", "ran" → "run".
"""





import nltk
from nltk.stem import PorterStemmer
# nltk.download("punkt")
ps = PorterStemmer()
text = "running runs runner"
print([ps.stem(w) for w in nltk.word_tokenize(text)])


# Stemming:
"""
 Definition: Heuristic chopping of word endings to get a base form (stem).

Fast, rule-based; no dictionary lookup.
 """
 
"""
❌ Can produce non-words: "better" → "better" (not "good"), "studies" → "studi".
"""

"""
Key Points:

    PorterStemmer → simple, rule-based, works fast but can distort words.

    LancasterStemmer → more aggressive, may cut too much.

    SnowballStemmer → balanced, supports multiple languages.

"""