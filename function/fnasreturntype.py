from nltk import word_tokenize, sent_tokenize

def get_tokens(whatdoyouwant):
    if whatdoyouwant == 'words':
        def tokenize_words(content):
            return word_tokenize(content)
        return tokenize_words
    elif whatdoyouwant == 'sentences':
        def tokenize_sentences(content):
            return sent_tokenize(content)
        return tokenize_sentences

content = "This is a sentence. This is another sentence."

tokenize = get_tokens('sentences')

print(tokenize(content))