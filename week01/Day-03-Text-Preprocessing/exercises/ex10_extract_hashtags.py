"""
Exercise 10 — Extract hashtags

Goal: Remove or clean hashtags (#topic) and mentions (@username) from text.
"""
import re
text = "Loving #AI #NLP and #MachineLearning in 2025!"
print(re.findall(r"#\w+", text))


