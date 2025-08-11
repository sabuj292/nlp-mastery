# Exercise 15: Extract all words ending with ing 



"""

Goal
Find every word that ends with ing — e.g., running, sing, learning.

Step-by-step thinking
Start of a word

Use \b to ensure we’re at a word boundary (no partial matches inside bigger strings).

Middle part of the word

[a-zA-Z]+ matches one or more letters before ing.

We can make it more flexible by using \w if we want to allow digits or underscores.

End with ing

Literal: ing

End of the word

Another \b to ensure we stop at the end of the word.
"""

# Pattern:
#           \b\w+ing\b



# -----------------------------------------Code-------------------------------


import re

text = "I am running, singing, and learning coding while eating pudding."
pattern = r"\b\w+ing\b"
matches = re.findall(pattern, text)
print(matches)
# ['running', 'singing', 'learning', 'eating', 'pudding']
