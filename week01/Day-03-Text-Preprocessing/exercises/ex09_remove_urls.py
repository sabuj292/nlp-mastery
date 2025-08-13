import re
text = "Check https://example.com"
print(re.sub(r"http\S+", "", text))


"""
http\S+ → matches http or https followed by any non-space characters.

www\.\S+ → matches www. followed by any non-space characters.

\S+@\S+ → matches an email format: something@something.
"""