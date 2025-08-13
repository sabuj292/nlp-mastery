import nltk
nltk.download("punkt")
# once run the above line, comment this other wise terminal will try to fetch the download will slow the actual task
text = "I love NLP"
print(nltk.word_tokenize(text))


from nltk.tokenize import word_tokenize
words = word_tokenize("Hello world! This is NLP.")
print(words)