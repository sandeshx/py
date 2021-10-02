# from nltk import word_tokenize, sent_tokenize



from typing import Text


def test() -> list:
    '''
    '''
    l = [1, 2, 3]
    return l

avariable = test()
print(sum(avariable))

def get_tokens(text):
    def to_lower(text):
        return text.lower()

# def get_tokens(whatdoyouwant):
#     if whatdoyouwant == 'words':
#         def tokenize_words(content):
#             return word_tokenize(content)
#         return tokenize_words
#     elif whatdoyouwant == 'sentences':
#         def tokenize_sentences(content):
#             return sent_tokenize(content)
#         return tokenize_sentences

# content = "This is a sentence. This is another sentence."

# tokenize = get_tokens('sentences')

# print(tokenize(content))