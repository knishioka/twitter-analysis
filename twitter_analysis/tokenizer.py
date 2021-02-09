from collections import Counter

import MeCab


def mecab():
    """Create mecab tokenizer"""
    return MeCab.Tagger('-Ochasen --eos-format=""')


def word_class_count(original):
    """Tokenize string and count word classes.

    Args:
        original (str): target string.

    Returns:
        collections.Counter: keys are word class and values are frequency.

    """
    m = mecab()
    return Counter([line.split()[-1] for line in m.parse(original).splitlines()])
