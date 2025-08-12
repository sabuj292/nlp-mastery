"""
Exercise 13 — Build a configurable preprocessing pipeline
"""
import re, string
from typing import List

def preprocess(
    text: str,
    lowercase: bool = True,
    remove_punct: bool = True,
    remove_numbers: bool = False,
    normalize_spaces: bool = True
) -> str:
    if lowercase:
        text = text.lower()
    if remove_punct:
        text = text.translate(str.maketrans('', '', string.punctuation))
    if remove_numbers:
        text = re.sub(r"\d+", "", text)
    if normalize_spaces:
        text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    s = "I ❤️ NLP! It's amazing... I scored 100% in my first test. 🚀"
    print(preprocess(s, remove_numbers=True))
