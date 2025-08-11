#  Exercise 6: Validate if a string is a phone number


# Goals:: we'll make a regex that validates phone numbers in multiple formats such as ---
"""
    123-456-7890

    (123) 456-7890

    123 456 7890

    +1-123-456-7890

    +44 20 7946 0958

"""

import re

numbers = [
    "+1-202-555-0143",
    "202-555-0143",
    "(202) 555-0143",
    "202 555 0143",
    "+44 20 7946 0958",
    "5550143",  # invalid
]

pattern = r"^(\+\d{1,3}[- ]?)?(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$"

for num in numbers:
    if re.match(pattern, num):
        print(f"valid: {num}")
    else:
        print(f"Invalid: {num}")