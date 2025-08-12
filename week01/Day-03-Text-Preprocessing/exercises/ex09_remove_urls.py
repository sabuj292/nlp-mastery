import re
text = "Check https://example.com"
print(re.sub(r"http\S+", "", text))
