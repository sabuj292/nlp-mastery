import unicodedata
text = "café"
normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
print(normalized)
