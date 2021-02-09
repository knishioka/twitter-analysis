from collections import Counter

import MeCab


def mecab():
    """Create mecab tokenizer"""
    return MeCab.Tagger('-Ochasen --eos-format=""')


def count_word_class(original):
    """Tokenize string and count word classes.

    Args:
        original (str): target string.

    Returns:
        collections.Counter: keys are word class and values are frequency.

    """
    m = mecab()
    return Counter([line.split()[-1] for line in m.parse(original).splitlines()])


def extract_list_of_words(original, word_class="名詞"):
    """Extract words only in word class list.

    Args:
        original (str): target string.
        word_class (str): target word class.

    Returns:
        `list` of `str`

    """
    m = mecab()
    return [line.split()[0] for line in m.parse(original).splitlines() if word_class in line.split()[-1]]
