import unicodedata
text = "café"
normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
print(normalized)


import unicodedata

def normalize_text(text, remove_accents=True):
    # Make characters consistent
    text = unicodedata.normalize("NFC", text)
    
    # Fix common smart quotes/dashes
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("…", "...")

    # Optional: remove accents (fold to plain letters)
    if remove_accents:
        text = ''.join(
            c for c in unicodedata.normalize("NFKD", text)
            if not unicodedata.combining(c)
        )

    # Remove extra spaces
    text = " ".join(text.split())
    return text

# Example
text = "“Résumé” — with  smart quotes  and accents!"
print(normalize_text(text))
# Output: "Resume - with smart quotes and accents!"
