# Exercise 14: Find duplicate words in a sentence 🔁


"""
Goal
Detect immediate word repetitions like:

“This is is fine.” → is is

“Very very good.” → very very
"""

"""
Key idea: Backreference
    (\w+) captures a word.

    \1 refers back to the exact same text captured by group 1.

    Between them allow spaces (or punctuation+space) as needed.

Core pattern (case‑insensitive):
        \b(\w+)\s+\1\b

"""


# -----------------------------code---------------------------


import re

text = "This is is fine. Very very good! Nope nope? YES yes!"
pattern = r"\b(\w+)\s+\1\b"
dups = re.findall(pattern, text, flags=re.IGNORECASE)
print(dups)  # ['is', 'very', 'nope', 'yes']
