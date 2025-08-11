"""
Goal
Find every hashtag in text (e.g., #NLP, #MachineLearning, #AI_2025) without grabbing the rest of the sentence.
"""

# Step-by-step thinking

"""
    Start with #
        Literal # → #

    Followed by allowed hashtag characters

        On Twitter/Instagram, hashtags can contain:

            Letters (A–Z, a–z)

            Digits (0–9)

            Underscores _

        They stop at spaces, punctuation, or the end of the text.

    Regex for that: \w+ (equivalent to [A-Za-z0-9_])

    Avoid matching just # without content
        Add + to require at least one word character after #.

"""

# Basic Pattern: #\w+


import re

tweet = """
Loving #Python and #MachineLearning in 2025! #AI_2025 #100DaysOfCode
Also check out #NLP, but not # (empty).
"""

pattern = r"#\w+"
hashtags = re.findall(pattern, tweet)

print(hashtags)

"""

Edge-case improvements
    Case-insensitive match: use re.IGNORECASE flag

    Avoid matching hashtags in the middle of words (rare):
    Use a word boundary or negative lookbehind:
"""

# for allowing hyphen in hashtags 
    # then pattern will be :: #\w[\w-]*
    
    
# Official Pattern for extracting hashtag:


pattern = r"(?<!\w)#\w+"
hashtags = re.findall(pattern, tweet)
print(hashtags)

# comment on official pattern

"""
Ensures hashtag is not preceded by another letter/digit/underscore.

Captures all valid Twitter-style hashtags.
"""
