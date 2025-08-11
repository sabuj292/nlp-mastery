# Exercise 11: Find all dates in format DD/MM/YYYY 📅

"""
Goal
Extract dates where:

Day = 01–31

Month = 01–12

Year = exactly 4 digits
"""

"""
Step-by-step thinking
    Day part (01–31)

        0[1-9] → 01 to 09

        1\d → 10 to 19

        2\d → 20 to 29

        3[01] → 30 or 31
        Combined:
            (0[1-9]|[12]\d|3[01])

    Month part (01–12)

        0[1-9] → 01 to 09

        1[0-2] → 10 to 12
        Combined:
            (0[1-9]|1[0-2])

    Year part (4 digits)
            \d{4}

    Separators

        Exactly / in this exercise: /
        
 """
 
#  Full Pattern:

#       \b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}\b




# ---------------------------------Code-----------------------------------


import re

text = """
Valid: 01/01/2025, 15/12/1999, 31/08/2020
Invalid: 32/01/2020, 29/13/2019, 5/5/2020
"""
# the following pattern will only produce the tuples (day,  month) because of groups
pattern = r"\b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}\b"

dates = re.findall(pattern, text)
print(dates)

# output: [('01', '01'), ('15', '12'), ('31', '08')]

# for Full match or Full date Formation:
# we need to wrap the whole thing in one big group or use re.finditer



text = """Valid: 01/01/2025, 15/12/1999, 31/08/2020
Invalid: 32/01/2020, 29/13/2019, 5/5/2020"""

# Easiest Way: use Non-capturing groups + findall
pattern = r"\b(?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/\d{4}\b"
print(re.findall(pattern, text))

# wrap the whole date in one group and use group(1) or (group(0) for the whole match)

pattern = r"\b((?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/\d{4})\b"
dates = [m.group(1) for m in re.finditer(pattern, text)]
print(dates)

"""
Use (?: … ) when:

You need grouping for operators like |, +, *, ?, {n,m}

But you don’t want that part in .groups() output
"""