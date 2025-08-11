# Exercise 9: Remove all punctuation from text

# Approach to deal with the problem: re.sub()

"""
Goal
Strip punctuation marks from a string, leaving only letters, numbers, and whitespace.
"""

"""

Step-by-step thinking
What is punctuation?
In regex, we can use:

\p{P} in some regex flavors (but not Python’s built-in re)

For Python re, define our own set: [^\w\s] matches anything that is not a word character or whitespace.

Why [^\w\s] works

\w = letters, digits, underscore

\s = whitespace

^ inside [] means negation
→ So [^\w\s] = characters that are not word characters and not whitespace (likely punctuation or symbols).
"""

# Pattern : [^\w\s]
# Replace with empty string : ""

import re

text = "Hello, world! This (text) has punctuation: #NLP, @AI_2025."

pattern = r"[^\w\s]"

cleaned = re.sub(pattern, "", text)
print(cleaned)

# Output: Hello world This text has punctuation NLP AI_2025

# Edge-Case Improvements or improvisation::
"""
    If we want to keep underscores _ but remove everything else:
        pattern:  [^\w\s]|_
        
    If we want to keep hashtags/mentions:
        [^\w\s#@]

"""
