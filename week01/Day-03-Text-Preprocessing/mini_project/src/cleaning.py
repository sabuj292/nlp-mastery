# src/cleaning.py
import re, string, unicodedata
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# ------- helpers -------
SMART_PUNCT = "“”‘’—–…"
PUNCT_TABLE = str.maketrans("", "", string.punctuation + SMART_PUNCT)
STOPWORDS = set(stopwords.words("english"))
LEMM = WordNetLemmatizer()

def get_wordnet_pos(tag: str):
    if tag.startswith('J'): return wordnet.ADJ
    if tag.startswith('V'): return wordnet.VERB
    if tag.startswith('N'): return wordnet.NOUN
    if tag.startswith('R'): return wordnet.ADV
    return wordnet.NOUN

# ------- upgrades (for advanced) -------
_CONTRACTIONS = {
    "ain't":"am not","aren't":"are not","can't":"can not","can't've":"can not have",
    "could've":"could have","couldn't":"could not","couldn't've":"could not have",
    "didn't":"did not","doesn't":"does not","don't":"do not","hadn't":"had not",
    "hasn't":"has not","haven't":"have not","he'd":"he would","he'll":"he will","he's":"he is",
    "i'd":"i would","i'll":"i will","i'm":"i am","i've":"i have","isn't":"is not",
    "it'd":"it would","it'll":"it will","it's":"it is","let's":"let us","ma'am":"madam",
    "might've":"might have","mightn't":"might not","must've":"must have","mustn't":"must not",
    "needn't":"need not","o'clock":"of the clock","shan't":"shall not","she'd":"she would",
    "she'll":"she will","she's":"she is","should've":"should have","shouldn't":"should not",
    "that'd":"that would","that's":"that is","there'd":"there would","there's":"there is",
    "they'd":"they would","they'll":"they will","they're":"they are","they've":"they have",
    "wasn't":"was not","we'd":"we would","we'll":"we will","we're":"we are","we've":"we have",
    "weren't":"were not","what's":"what is","when's":"when is","where's":"where is","who's":"who is",
    "why's":"why is","won't":"will not","would've":"would have","wouldn't":"would not",
    "y'all":"you all","you'd":"you would","you'll":"you will","you're":"you are","you've":"you have"
}
_APOS = ("'", "’")
_CONTR_RE = re.compile(r"\b(" + "|".join(map(re.escape, sorted(_CONTRACTIONS, key=len, reverse=True))) + r")\b", re.I)

_URL_RE = re.compile(r"(https?://\S|www\.)\S*", re.I)
_HTML_TAG_RE = re.compile(r"<[^>]+>")

_EMOJI_MAP = {
    "😀":"<POS_EMOJI>","😄":"<POS_EMOJI>","🙂":"<POS_EMOJI>","😍":"<POS_EMOJI>","👍":"<POS_EMOJI>",
    "😢":"<NEG_EMOJI>","😤":"<NEG_EMOJI>","👎":"<NEG_EMOJI>","🚚":"<DELIVERY>","🔋":"<BATTERY>"
}

def expand_contractions(text: str) -> str:
    norm = text
    for apos in _APOS[1:]:
        norm = norm.replace(apos, _APOS[0])
    def _r(m): return _CONTRACTIONS.get(m.group(0).lower(), m.group(0))
    return _CONTR_RE.sub(_r, norm)

def normalize_urls_and_html(text: str, replace_url_with="<URL>") -> str:
    text = _URL_RE.sub(replace_url_with, text)
    text = _HTML_TAG_RE.sub(" ", text)
    return text

def normalize_unicode(text: str, remove_accents=True) -> str:
    text = (text.replace("“", '"').replace("”", '"')
                .replace("‘", "'").replace("’", "'")
                .replace("–", "-").replace("—", "-")
                .replace("…", "..."))
    text = "".join(_EMOJI_MAP.get(ch, ch) for ch in text)
    text = unicodedata.normalize("NFC", text)
    if remove_accents:
        text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))
    return " ".join(text.split())

# ------- basic (Exercise-15 faithful) -------
def clean_text_basic(text: str) -> str:
    text = text.lower()
    text = text.translate(PUNCT_TABLE)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS]
    pos_tags = nltk.pos_tag(tokens)
    lemmas = [LEMM.lemmatize(w, get_wordnet_pos(tag)) for w, tag in pos_tags]
    return " ".join(lemmas).strip()

# ------- advanced (with upgrades) -------
def clean_text_advanced(text: str) -> str:
    text = text.lower()
    text = normalize_unicode(text, remove_accents=True)
    text = expand_contractions(text)
    text = normalize_urls_and_html(text, replace_url_with="<URL>")
    text = text.translate(PUNCT_TABLE)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS]
    pos_tags = nltk.pos_tag(tokens)
    lemmas = [LEMM.lemmatize(w, get_wordnet_pos(tag)) for w, tag in pos_tags]
    return " ".join(lemmas).strip()
