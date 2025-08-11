# Exercise 8: Replace multiple spaces with a single space

"""
Goal
Turn messy text with multiple consecutive spaces into clean text with exactly one space between words.
"""

"""
Step-by-step thinking
Match multiple spaces

Space character is " " or \s for any whitespace (space, tab, newline).

Use + to match one or more in a row:
    \s+

Replace with a single space

In Python, use re.sub(pattern, replacement, text).
"""

# Pattern : \s+
# Replace with: " "

import re

text = "This   is    a     sentence     with  irregular   spacing."

pattern = r"\s+"
cleaned= re.sub(pattern, " ", text)

print(cleaned)

# This is a sentence with irregular spacing.

# Edge-case Improvements
"""
To also remove leading/trailing spaces, use .strip() after re.sub.

If you only want to replace spaces inside the string but keep newlines, change the pattern to:

Pattern: [ ]+
"""
