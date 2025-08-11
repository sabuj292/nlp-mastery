# Goal
"""
Find every email address in a given text — even if it has dots, dashes, underscores, or numbers in the username or domain.
"""

# Step by Step Thinking

"""
Step-by-step thinking
    1) Username part (before the @)

        Can include letters, digits, underscores, dots, hyphens.

        Pattern: [\w\.-]+

            \w → letters, digits, underscore

            . and - included explicitly inside the class

            + → one or more times

    2) @ symbol

        Literal @ → @

    3) Domain name (before the final dot)

        Same allowed chars as username (but no spaces): [\w\.-]+

    4) Top-level domain (TLD)

        Letters/digits, at least 2 characters: \.\w+
        (We escape the dot \. because dot in regex means “any character”)

"""

# Full Basic Pattern
"""
[\w\.-]+@[\w\.-]+\.\w+

"""
import re

text = """
Contact us: hello@example.com, support@mail-service.org,
and sales.team_2025@company.co.uk for more info.
"""

pattern = r"[\w\.-]+@[\w\.-]+\.\w+"

emails = re.findall(pattern, text)

print(emails)

# Final Pattern 

text = """
Contact us: hello@example.com, support@mail-service.org,
and sales.team_2025@company.co.uk for more info.
"""

# Robust email pattern using raw string
pattern = r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}\b"

emails = re.findall(pattern, text)
print(emails)

# Break Down of pattern

"""
    [\w\.-]+ → username: letters, digits, underscores, dots, hyphens
    @ → literal at symbol
    [\w\.-]+ → domain name: same character set as username
    \.[a-zA-Z]{2,} → TLD: at least 2 letters
    \ b → word boundary so punctuation doesn’t sneak in

"""