# Exercise 13: Replace all digits with #

"""
Goal
Take any text with numbers and replace each digit with the # character.
"""
"""
Step-by-step thinking
What matches a digit?

\d matches any digit (0–9).

If you want to be extra explicit, you can use [0-9].

Replace all occurrences

Use re.sub(pattern, replacement, text).

Replacement is simply "#".

Make sure all digits are replaced individually

Since \d matches one digit, adding + will replace consecutive digits with a single # unless you want one # per digit.

So:

Per digit → \d

Per number (single # for 123) → \d+

"""


#  per digit replacing 
import re

text = "Order 123 will arrive in 4 days at 2025 Main Street."
pattern = r"\d"
result = re.sub(pattern, "#", text)
print(result)
# Order ### will arrive in # days at #### Main Street.


# per number replacing

pattern = r"\d+"
result = re.sub(pattern, "#", text)
print(result)
# Order # will arrive in # days at # Main Street.

