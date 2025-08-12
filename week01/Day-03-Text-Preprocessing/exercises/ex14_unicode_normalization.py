"""
Exercise 14 — Unicode normalization (accents/compatibility)
"""
from unidecode import unidecode
text = "Café naïve coöperate — résumé"
print(unidecode(text))  # -> Cafe naive cooperate -- resume
