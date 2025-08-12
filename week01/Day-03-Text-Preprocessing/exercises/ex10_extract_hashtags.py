"""
Exercise 10 — Extract hashtags
"""
import re
text = "Loving #AI #NLP and #MachineLearning in 2025!"
print(re.findall(r"#\w+", text))
