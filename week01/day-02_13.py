# Exercise 12: Extract domain name from an email

"""
Goal
From emails like:
    john.doe99@mail.com
    support@company.org


we want to extract only the domain name part:

    mail.com
    company.org


Step-by-step thinking
    Match the whole email

        [ \w\.-]+ → username part (letters, digits, _, ., -)

        @ → literal at symbol

        [\w\.-]+ → domain part before TLD

        \.\w+ → top-level domain (.com, .org, etc.)

    Capture only the domain

        We don’t need the username, so we make it non-capturing:

            (?:[\w\.-]+@)
        Then capture the domain and TLD in one capturing group:
            ([\w\.-]+\.\w+)

"""


"""
Pattern: 
    (?:[\w\.-]+@)([\w\.-]+\.\w+)

    
    (?: … ) → non-capturing for username + @

    ([ … ]) → capturing for the domain part

"""


import re

text = """
Emails: test.user@example.com, admin@my-site.io,
sales.team_2025@company.co.uk
"""

pattern = r"(?:[\w\.-]+@)([\w\.-]+\.\w+)"
domains = re.findall(pattern, text)
print(domains)
# ['example.com', 'my-site.io', 'company.co.uk']
