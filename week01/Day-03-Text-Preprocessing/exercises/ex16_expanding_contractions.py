contractions_dict = {
    "can't": "cannot",
    "won't": "will not",
    "i'm": "i am",
    "it's": "it is",
    "he's": "he is",
    "she's": "she is",
    "they're": "they are",
    "we're": "we are",
    "that's": "that is",
    "what's": "what is",
    "let's": "let us",
    "n't": " not",
    "'re": " are",
    "'s": " is",
    "'d": " would",
    "'ll": " will",
    "'ve": " have",
    "'m": " am"
}

def expand_contractions_simple(text):
    text = text.lower()  # make matching easier
    words = text.split() # split into words
    
    expanded_words = []
    for word in words:
        if word in contractions_dict:
            expanded_words.append(contractions_dict[word])
        else:
            expanded_words.append(word)
    
    return " ".join(expanded_words)

# Example
text = "I'm learning NLP and I can't stop now."
print(expand_contractions_simple(text))
