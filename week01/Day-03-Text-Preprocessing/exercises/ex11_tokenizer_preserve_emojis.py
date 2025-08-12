"""
Exercise 11 — Custom tokenizer that preserves emojis & hashtags
"""
import re
# Tokenize words, hashtags, mentions, emojis (basic range), and keep punctuation out
pattern = re.compile(
    r"(@\w+|#\w+|[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]|\w+)", 
    flags=re.UNICODE
)
text = "Hey @john 😍 I love #NLP and #AI!!!"
print(pattern.findall(text))
