#!/usr/bin/env python3

__all__ = ["print_usage", "get_n_most_frequent_words_occs"]

### IMPORT

# Python librairies import
import nltk
from nltk.probability import FreqDist


## FUNCTIONS

def print_usage(program_name):
    print(f"""Usage: python {program_name} <number>
    1: Mendenhall's Characteristic Curves of Composition
    2: Kilgariff's Chi-Squared Method
    3: John Burrows' Delta Method""")


def get_n_most_frequent_words_occs(n, corpus):
    """Get the n most frequent words from a corpus with their frequency occurence"""
    fdist = nltk.FreqDist(corpus)
    words_occs = list(fdist.most_common(n))
    return words_occs
