# Problem Statement:: Extracting all numbers from a paragraph \
    
# Goal::
"""
Find all numeric values in text, including:

Whole numbers (42, 1000)

Decimals (3.14, 0.99)

Possibly numbers with commas (1,234) if we choose to support them.
"""

"""
Step-by-step thinking
Digits → \d+ matches one or more digits.

Optional decimal part → (?:\.\d+)? matches . followed by digits, zero or one time.

Optional comma grouping → If needed, allow digits in groups of three after a comma:
(?:,\d{3})*

"""

# uses of '(?' why to use or not
"""
Think of ( as “grab this part and save it in a container”.
Think of (?: as “group these tokens for my own convenience, but don’t save them”.
Think of (?something as “this isn’t a normal container — it’s a special instruction for matching”.
"""

import re

text = """
The population is 1,234,567 and growing by -3.5% annually.
Last year it was 1,200,000 with a GDP per capita of 42.75.
"""

# for dealing with negative number we need to add - prefix

# official pattern
pattern = r"-?\d{1,3}(?:,\d{3})*(?:\.\d+)?"
numbers = re.findall(pattern, text)
print(numbers)


# Breakdown of the pattern = r"\d{1,3}(?:,\d{3})*(?:\.\d+)?"
"""

    \d{1,3} → first group (1–3 digits)

    (?:,\d{3})* → zero or more groups of comma + 3 digits

    (?:\.\d+)? → optional decimal
"""


# Pattern for scientific notation (1.23e4, 4.56E-7, 3e8, etc.)

"""
Pattern breakdown
Base number — can be:

    An integer: 123

    A decimal: 1.23
    Pattern:   \d+(?:\.\d+)?

Exponent marker — e or E: [eE]

Exponent value — integer, can be negative or positive: [+-]?\d+
    Optional sign [+-]?

    One or more digits \d+


"""

# Full scientific notation Pattern

pattern = r"-?\d+(?:\.\d+)?[eE][+-]?\d+"

text = """
Speed of light ≈ 3e8 m/s, Planck's constant = 6.626e-34 J·s,
Avogadro's number = 6.022E23 mol^-1, example: -1.23e4
"""

matches = re.findall(pattern, text)
print(matches)

# ['3e8', '6.626e-34', '6.022E23', '-1.23e4']


# combining the scientific notation pattern with common pattern 
# Universal Number Extractor that handles:
"""
integers

decimals

comma-separated numbers

scientific notation
"""


import re

text = """
Values: 42, 3.14, .75, 1,234, 1,234.56, -12,345.00,
scientific: 3e8, -1.23e-4, 6.022E23, and edge 1234.56
"""

uni_pattern = r"""(?x)           # verbose mode must be first!
-?                               # optional sign
(?:
    \d+(?:\.\d+)?[eE][+-]?\d+    # scientific: 1.23e4, 3e8, -4E-7
  |                              # OR
    (?:
        (?:\d{1,3}(?:,\d{3})+|\d+)  # 1,234 or 1234
        (?:\.\d+)?                  # optional decimal
      | \.\d+                       # leading-dot decimal (.75)
    )
)
"""

matches = re.findall(uni_pattern, text)
print(matches)

# Expected:
# ['42', '3.14', '.75', '1,234', '1,234.56', '-12,345.00',
#  '3e8', '-1.23e-4', '6.022E23', '1234.56']