from nltk import word_tokenize, sent_tokenize


def get_words(text):
    return word_tokenize(text)


def get_sents(text):
    return sent_tokenize(text)


text = "This is a sentence. This is another sentence."


def get_tokens(funct, text):
    return funct(text)

# passing function as argument
print(get_tokens(get_words, text))