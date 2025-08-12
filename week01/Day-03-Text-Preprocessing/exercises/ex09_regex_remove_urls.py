"""
Exercise 09 — Regex to remove URLs
"""
import re
text = "Check https://example.com and http://foo.bar or www.test.org please."
url_pattern = re.compile(r"(https?://\S+|www\.\S+)")
print(url_pattern.sub("", text).strip())
