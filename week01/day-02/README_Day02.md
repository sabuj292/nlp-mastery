# NLP Mastery – Day 02: Regex & Text Handling

Welcome to **Day 02** of my NLP Mastery journey!  
This day is dedicated to mastering **Regular Expressions (Regex)** for text handling in Natural Language Processing.

---

## 📚 Overview

Regular Expressions are powerful tools for pattern matching and text manipulation.  
In NLP, regex is often the **first step** in preprocessing: cleaning, tokenizing, validating, and extracting text patterns.

---

## 📂 What's Inside

This directory contains:
- **`Day_02_Regex_and_Text_Handling.pdf`** – Theory and exercises (beautifully organized for offline study)
- **`NLP_Mastery_Day02_Regex_Handbook.pdf`** – Full handbook with explanations, examples, and key takeaways
- Example Python scripts demonstrating regex patterns for NLP preprocessing

---

## 🏆 Key Topics Covered

- **Basic Regex Syntax** – literals, metacharacters, quantifiers
- **Character Classes** – `\d`, `\w`, `\s`, custom classes
- **Anchors & Boundaries** – `^`, `$`, `\b`, `\B`
- **Groups & Alternation** – `()`, `(?:)`, `|`
- **Lookarounds** – lookahead `(?=...)`, negative lookahead `(?!...)`, lookbehind `(?<=...)`, negative lookbehind `(?<!...)`
- **Practical NLP Patterns**:
  - Matching capitalized words
  - Extracting emails & URLs
  - Handling hashtags
  - Number & date extraction
  - Phone number validation
  - Removing punctuation
  - Sentence splitting

---

## 📝 Exercises

There are **15 hands-on exercises** included in the handbook:

1. Match All Capitalized Words  
2. Extract All Emails from Text  
3. Extract All URLs from HTML Content  
4. Extract All Hashtags from a Tweet  
5. Extract All Numbers from a Paragraph  
6. Validate if a String is a Phone Number  
7. Find All Words Starting with 'a'  
8. Replace Multiple Spaces with a Single Space  
9. Remove All Punctuation from Text  
10. Split a Paragraph into Sentences  
11. Find All Dates in Format DD/MM/YYYY  
12. Extract Domain Name from an Email  
13. Replace All Digits with #  
14. Find Duplicate Words in a Sentence  
15. Extract All Words Ending with 'ing'  

Each exercise in the PDF includes:
- Problem statement
- Final regex pattern
- Step-by-step explanation
- Example inputs & outputs
- Key takeaways

---

## 🚀 Usage

To run the regex examples:
```bash
python exercise_X.py
```
Replace `X` with the exercise number.

Make sure you have **Python 3.7+** installed.

---

## 📌 Quick Reference

Common regex tokens:

| Token | Meaning |
|-------|---------|
| `\d` | Digit [0-9] |
| `\w` | Word char [a-zA-Z0-9_] |
| `\s` | Whitespace |
| `.` | Any char (except newline) |
| `^` / `$` | Start / End of string |
| `\b` / `\B` | Word boundary / Non-boundary |
| `+`, `*`, `?`, `{n,m}` | Quantifiers |
| `(...)` | Capturing group |
| `(?:...)` | Non-capturing group |
| `a|b` | Alternation |
| `(?=...)` | Lookahead |
| `(?!...)` | Negative lookahead |
| `(?<=...)` | Lookbehind |
| `(?<!...)` | Negative lookbehind |

---

## ✍ Author
**Shahriar Mahmud Sabuj**  
Part of my mission: *"No one on Earth will surpass my NLP skills."*

---

## 📅 Next Step
In **Day 03**, we will move into **Tokenization & Normalization** – taking our raw text and preparing it for advanced NLP models.

