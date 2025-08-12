import re
text = "I ❤️ NLP #AI"
print(re.findall(r"[\w#]+|[\U0001F600-\U0001F64F]", text))
