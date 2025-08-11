# Problem Statement:
# Exercise 1 — Match all capitalized words in a sentence
# Goal: find words that start with a capital letter (e.g., “London”, “Alice”), regardless of where they appear in the sentence.

import re

text = "Alice met Dr. Brown in New York; they visited the USA and iPhone stores."

pattern = r"\b[A-Z][a-z]+"
print(re.findall(pattern, text))

text1 = "This is Alice and Bob going to New-York with NASA."
text2 = "mr Smith met Dr. Brown at the USA Expo."

text3 = "iPhone sales in Europe grew as Apple launched Vision Pro."

pattern1 = r"\b[A-Z][a-z]+(?:-[A-Z][a-z]+)*\b"
print(re.findall(pattern1, text1))

pattern2 = r"\b([A-Z][a-z]+|[A-Z]{2,})\b"
print(re.findall(pattern2, text2))

pattern3 = r"\b(?:[A-Z][a-z]+|[A-Z]{2,})\.?"
print(re.findall(pattern3, text3))


# Official Solution
"""
official solution the hyphen/acronym version, because:

    It covers names with hyphens like New-York.

    It catches acronyms like USA, NLP.

    It’s still compact enough to memorize.
"""
# ✅ Official pattern:
"""
\b(?:[A-Z][a-z]+|[A-Z]{2,})(?:-[A-Z][a-z]+)*\b

"""
# Breakdown of the Pattern
"""
    \b – start at a word boundary.
    
    (?:[A-Z][a-z]+|[A-Z]{2,}) – either a normal capitalized word (e.g., London) or an all-caps acronym (e.g., NASA).
    
    (?:-[A-Z][a-z]+)* – optionally match one or more hyphenated parts.
    
    \b – end at a word boundary.
    
"""

official_pattern = r"\b(?:[A-Z][a-z]+|[A-Z]{2,})(?:-[A-Z][a-z]+)*\b"

text = "Alice met Dr. Brown in New-York; NASA sent them an invite."

print(re.findall(official_pattern, text))


