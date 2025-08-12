import nltk
from nltk.stem import PorterStemmer
nltk.download("punkt")
ps = PorterStemmer()
text = "running runs runner"
print([ps.stem(w) for w in nltk.word_tokenize(text)])
