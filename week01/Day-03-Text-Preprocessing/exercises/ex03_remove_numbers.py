"""
Exercise 03 — Remove numbers (optional by task)
"""
import re
text = "I scored 100 in test #2 on 2025-08-12."
print(re.sub(r"\d+", "", text))
