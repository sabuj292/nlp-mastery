import re
text = "I   love   NLP"
print(re.sub(r"\s+", " ", text).strip())


"""
\s+ matches one or more whitespace characters (spaces, tabs, newlines).

.strip() removes leading/trailing spaces.
"""