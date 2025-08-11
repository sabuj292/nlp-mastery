# Problem Statement: Extract all URLs from HTML content
# Goals:
"""
Pull out every HTTP/HTTPS (and optionally www.) link from mixed text/HTML without swallowing trailing punctuation or quotes.
"""
import re

html = """
<p>Docs: https://example.com/guide?ref=home#intro</p>
<a href="https://sub.domain.org/path/file.html">link</a>
Text with www.site.co.uk/page), and a sentence end: https://foo.bar/baz().
Bad: http:/oops and mailto:someone@example.com should not match.

"""

# for only http/https:
pattern = r"(?<!\w)https?://[^ \t\r\n\"'<>)]+"
urls = re.findall(pattern, html)
print(urls)

# fot http/https + www.:
pattern = r'(?<!\w)(?:https?://|www\.)[^ \t\r\n"\'<>)]+'

urls = re.findall(pattern, html)
cleaned = [u.rstrip('.,)(;:!?"\'') for u in urls]

print(urls)



# Official Solution for this exercise

pattern = r"(?<!\w)(?:https?://|www\.)[^ \t\r\n"'<>)]+"

