"""
Exercise 09 — Regex to remove URLs
"""
import re
text = "Check https://example.com and http://foo.bar or www.test.org please."
url_pattern = re.compile(r"(https?://\S+|www\.\S+)")
print(url_pattern.sub("", text).strip())

"""
http\S+ → matches http or https followed by any non-space characters.

www\.\S+ → matches www. followed by any non-space characters.

\S+@\S+ → matches an email format: something@something.

"""
