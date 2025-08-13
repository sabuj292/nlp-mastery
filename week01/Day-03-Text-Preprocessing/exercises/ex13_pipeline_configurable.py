"""
Exercise 13 — Build a configurable preprocessing pipeline
"""
import re
import unicodedata
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def preprocess(text, lowercase=True, remove_punct=True, remove_nums=False,
               normalize_unicode=True, remove_stop=True, stemming=False,
               emoji_mode="keep"):  # keep, demojize, drop

    if normalize_unicode:
        text = unicodedata.normalize("NFKD", text)

    if lowercase:
        text = text.lower()

    if emoji_mode == "demojize":
        text = emoji.demojize(text)
    elif emoji_mode == "drop":
        text = emoji.replace_emoji(text, replace="")

    if remove_punct:
        text = re.sub(r"[^\w\s]", "", text)

    if remove_nums:
        text = re.sub(r"\d+", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text)

    if remove_stop:
        stop_words = set(stopwords.words("english")) - {"not", "no", "never"}
        tokens = [w for w in tokens if w not in stop_words]

    if stemming:
        ps = PorterStemmer()
        tokens = [ps.stem(w) for w in tokens]

    return tokens


# if __name__ == "__main__":
#     s = "I ❤️ NLP! It's amazing... I scored 100% in my first test. 🚀"
#     print(preprocess(s, remove_numbers=True))

sample = "I LOVE NLP!!! ❤️ It's amazing... 100%"
print(preprocess(sample, lowercase=True, emoji_mode="demojize", stemming=True))




# -------------------------------theory--------------------------------------

"""
Why a Configurable Pipeline?
    Different tasks require different cleaning rules.

    A single “remove everything” approach is dangerous — you might destroy useful features.

    A configurable pipeline lets you toggle steps on/off depending on the project.

"""


"""
Core Components (Typical Order)
        Lowercasing (optional)

        Unicode normalization (always recommended early)

        Special character handling (keep/drop selectively)

        Punctuation removal (optional)

        Number handling (remove, keep, normalize)

        Whitespace normalization

        Tokenization (word/sentence/subword)

        Stopword removal (with negation strategy)

        Stemming or Lemmatization (one or both depending on task)

        Emoji handling (keep/demojize/drop)

"""

"""
Why This Order?
        Unicode normalization first → ensures all text is in a consistent form before regex/token rules.

        Case, punctuation, numbers early → affects token boundaries.

        Whitespace normalization before tokenization → prevents empty/malformed tokens.

        Stopword removal and stemming/lemmatization after tokenization → work on clean token lists.
"""


"""
Making your pipeline configurable saves you from rewriting cleaning code for every project. It also lets you run A/B tests on preprocessing choices.

"""



# Why is it safer to normalize Unicode before removing punctuation?


"""
1) Unicode before punctuation
        Your reasoning is good: Without normalization, some accented letters or symbols (é, ñ) may be stored as multi-byte sequences or decomposed into base letter + combining mark.

        If you remove punctuation/special chars first, those combining marks could get stripped, leaving corrupted text (café → caf).

        Normalizing first makes sure punctuation removal is safe.

"""


"""
Why skip stemming in NER?
        NER depends on the exact surface form of a name or term.

        "Washington" stemmed might still be "washington", but "Hastings" could be chopped incorrectly.

        "McDonald's" might lose apostrophe or capitalization cues.

        Stemming can distort named entities, making recognition harder for the model.

        Best practice: For NER, keep tokens intact and rely on the model’s embedding/context.
"""