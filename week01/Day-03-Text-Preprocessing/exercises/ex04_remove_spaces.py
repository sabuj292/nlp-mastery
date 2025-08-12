import re
text = "I   love   NLP"
print(re.sub(r"\s+", " ", text).strip())
