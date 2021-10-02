from typing import List
from nltk import sent_tokenize, word_tokenize

text = "This is a sentence. This is another sentence."
TOKENIZE_WORD = True

# # function 1
# def tokenize_word(text) -> List[str]:
#     return word_tokenize(text)

# # function 2
# def tokenize_sentence(text) -> List[str]:
#     return sent_tokenize(text)


# Functions as data
tokenize = word_tokenize if TOKENIZE_WORD else sent_tokenize
tokens = tokenize(text)

print(tokens)