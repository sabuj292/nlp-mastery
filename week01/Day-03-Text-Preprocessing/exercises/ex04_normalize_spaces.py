"""
Exercise 04 — Normalize whitespace
"""
import re
text = "I    love   NLP \n\n so   much!"
print(re.sub(r"\s+", " ", text).strip())
