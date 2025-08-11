#  Exercise 10: Split a paragraph into sentences

"""
Goal
Split text into sentences where each sentence ends with ., ?, or !, possibly followed by spaces, but without losing the punctuation.
"""

"""
Step-by-step thinking
    Normal .split() won’t work well

        It removes the delimiter (punctuation)

        It can’t handle multiple punctuation marks easily (..., ?!)

    Regex split with lookbehind

        We can split after a punctuation mark using a positive lookbehind:
            (?<=[.?!])
    Handle following spaces

        Add \s+ to eat the spaces after punctuation.

"""

# Pattern: (?<=[.?!])\s+
"""  
    (?<= … ) → positive lookbehind (must be right after ., ?, or !)

    \s+ → one or more spaces to split on
"""

import re

text = "Hello world! How are you? I'm fine. Let's learn NLP."

pattern = r"(?<=[.?!])\s+"

"""
With positive lookbehind (?<=...)
    Regex says:

        "Only split if there’s punctuation right behind me,
        but don’t take it away — leave it where it is."

"""

sentences = re.split(pattern, text)

for s in sentences:
    print(s)
    
    
"""
Edge-case improvements
Abbreviations: This simple regex will split after Mr. or Dr. incorrectly.
Handling that perfectly requires NLP sentence tokenizers (e.g., nltk.sent_tokenize).
"""

# Important concept:: ---------------------------- must see-----------------------------------
# Let's learn some theory about the "lookaround" in regex

"""
Regex normally matches and consumes characters — meaning they become part of the match result.

Lookarounds are zero-width assertions:

        They check for a condition before (lookbehind) or after (lookahead) the current position

        But do not consume characters — they just assert something is true or false.

"""

"""
2️⃣ Positive lookbehind syntax:
        (?<=pattern)

It means:

“Match here only if there’s pattern directly before this position.”

"""

"""
3️⃣ Example: Without vs. With lookbehind
Without lookbehind
    Regex says:

        "Find punctuation and split on it."

        So it takes the punctuation away when splitting:

    
    
    import re
    text = "Hello world! How are you?"
    re.split(r"[.?!]\s+", text)
    
Problem: The punctuation is consumed — result has no ! or ? in the split parts:

output: ['Hello world', 'How are you?']

    
    
With positive lookbehind:    

    With positive lookbehind (?<=...)
        Regex says:

            "Only split if there’s punctuation right behind me,
            but don’t take it away — leave it where it is."


        So it looks behind the split point for ., ?, or !:
        
        
        import re
        text = "Hello world! How are you?"
        re.split(r"(?<=[.?!])\s+", text)
        
    Here:

(?<=[.?!]) means "only split where the previous character is ., ?, or !"

The punctuation stays before the split point, so it’s still part of the sentence.

    Output: ['Hello world!', 'How are you?']



"""



"""
Think of it like:
    Normal regex match = eat the thing

    Lookbehind = just peek at the thing before you, don’t eat it.

"""

# Negative lookbehind syntax
"""
    (?<!pattern)

It means:

“Match here only if the text right behind me does not match pattern.”


"""



# --------------------------Lookahead----------------------------------------

"""
Easy definition
    Lookbehind → peek behind me without taking anything

    Lookahead → peek ahead of me without taking anything

Positive Lookahead syntax:

    (?=pattern)

It means:

“Match here only if there’s pattern directly ahead.”
"""
    
# -----------------example-----------

"""
Example
Say we have:
        Price: $100, $250, $300.
We want to match only the numbers that are followed by a comma.

Without lookahead:
If we match \d+ normally, we’ll get all numbers:

            import re
            text = "Price: $100, $250, $300."
            print(re.findall(r"\d+", text))
            # ['100', '250', '300']


With positive lookahead (?=,):

            print(re.findall(r"\d+(?=,)", text))
            # ['100', '250']   # only numbers followed by a comma


Here:

\d+ matches the number

(?=,) peeks ahead to see if a comma is there — but doesn’t include it in the match.
"""

"""
Analogy
Lookbehind: “Before I step, I check what’s behind me.”

Lookahead: “Before I step, I check what’s ahead of me.”


Positive vs Negative
    (?=...) → positive lookahead = must be followed by pattern

    (?!...) → negative lookahead = must not be followed by pattern

"""
    
    