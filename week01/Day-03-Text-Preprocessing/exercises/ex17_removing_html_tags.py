



import re
text = "<h1>Welcome</h1><p>This is <b>NLP</b> &amp; text cleaning.</p>"

# 1) Remove Tag:
no_tags = re.sub(r'<[^>]+>', ' ', text)

# collapse extra spaces
clean_text = re.sub(r'\s+', ' ', no_tags).strip()
print(clean_text)




# option - 2 Safer way

from bs4 import BeautifulSoup
text = "<h1>Welcome</h1><p>This is <b>NLP</b> &amp; text cleaning.</p>"

clean_text = BeautifulSoup(text, "html.parser").get_text(separator=" ")
clean_text = " ".join(clean_text.split())
print(clean_text)



"""
Regex is fine for quick cleanup; BeautifulSoup is more robust for real webpages.

After removing tags, always collapse whitespace.
"""

"""
 Pattern: r'<[^>]+>'
Let’s decode it character by character:
| Part   | Meaning                                                                                                                                |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `<`    | Matches the starting `<` of an HTML tag.                                                                                               |
| `[^>]` | `[^...]` means “match anything **except** what's inside the brackets.” Here, `[^>]` means “match any character that is **not** a `>`.” |
| `+`    | Means “**one or more**” of the preceding thing (`[^>]`), so keep matching characters until you reach a `>`.                            |
| `>`    | Matches the closing `>` of the tag.                                                                                                    |


"""