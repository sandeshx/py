from nltk import word_tokenize, sent_tokenize

text = "This is a sentence. This is another sentence."

text_updated = text

functions = [
    str.lower,
    word_tokenize
]


for function in functions:
    text_updated = function(text_updated)

print(text_updated)
