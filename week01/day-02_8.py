# Exercise 7: Find all words starting with 'a' or 'A'

# Goal: Match every word that starts with 'a' or 'A' in a text

"""

Step-by-step thinking
Word boundary at start

Use \b to make sure we match the start of a word, not inside it.

First letter is ‘a’ or ‘A’

[aA] matches both lowercase and uppercase a.

Or we could just use re.IGNORECASE.

Rest of the word

\w* matches zero or more letters, digits, or underscores after the first letter.
"""


import re

text = "Alice and Bob are amazing artists at an Academy in Africa."

pattern = r"\ba\w*"
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(matches)

pattern1 = r"\b[aA]\w*"

# if we use flags = re.IGNORECASE which is equivalent to it if fetch the word no matter it's uppercase or lowercase

matches = re.findall(pattern1, text)
print(matches)

# if we want only letters after 'a' (no digits / underscore)
# then pattern will be: \b[aA][a-zA-Z]