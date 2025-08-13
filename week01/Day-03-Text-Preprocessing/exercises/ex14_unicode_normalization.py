"""
Exercise 14 — Unicode normalization (accents/compatibility)
"""
from unidecode import unidecode
text = "Café naïve coöperate — résumé"
print(unidecode(text))  # -> Cafe naive cooperate -- resume





samples = [
    "Café vs Café",                  # visually same, different codepoints
    "ﬁnancial (ﬁ ligature)",          # ligature
    "Non‑breaking space inside",      # NBSP & narrow NBSP
    "“Smart quotes”… and—dashes",     # punctuation variants
    "résumé, niño, faç̧ade"           # accents
]
for s in samples:
    print("IN: ", s)
    print("OUT:", unicode_normalize(s, fold_accents=True))
    print()
