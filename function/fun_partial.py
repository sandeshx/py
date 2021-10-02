from functools import partial
from nltk import word_tokenize
from typing import List
import wikipedia
from wikipedia.wikipedia import summary

# x, y, z


def get_summary(topic: str, no_sentences: int) -> List[str]:
    return wikipedia.summary(topic, no_sentences)


topic = 'Natural Language Processing'
summary_topic = partial(get_summary, topic)

# asd;lkas;dlask

summary = summary_topic(2)
print(summary)

