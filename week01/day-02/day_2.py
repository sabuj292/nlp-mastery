import re
pattern = r"\d{3}-\d{2}-\d{4}"

text = "My SSN is 123-45-6789."
print(re.findall(pattern, text))

pattern = r"\d[0-9]"
print(re.findall(pattern, text))

pattern = r"\d+"
print(re.findall(pattern, text))

"""
\d{3} → exactly 3 digits.

\d+ → 1 or more digits (greedy match).

\d[0-9]{3} → one digit + three more digits (total 4).
"""

# breakdown of the pattern. What is says
"""
\d{3} → exactly 3 digits

- → dash

\d{2} → exactly 2 digits

- → dash

\d{4} → exactly 4 digits


[3 digits] - [2 digits] - [4 digits]

"""