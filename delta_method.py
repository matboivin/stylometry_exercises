#!/usr/bin/env python3
# John Burrows’ Delta Method

__all__ = ["apply_delta_method"]

### IMPORT

# Utils import
from utils import get_n_most_frequent_words_occs


## FUNCTIONS

def apply_delta_method(n, corpus, categories):
    # Select the categories and store the number of tokens per category
    combined_corpus = list()
    tokens_count = dict()

    for category in categories:
        combined_corpus += corpus[category]
        tokens_count[category] = len(corpus[category])

    # Select the most frequent tokens to be used as features
    words_occs = get_n_most_frequent_words_occs(n, combined_corpus)
    features = [word for word,count in words_occs]

    # Get the total number of tokens per category
    feature_freqs = dict()

    for category in categories:
        feature_freqs[category] = dict()

        for feature in features:
            share = corpus[category].count(feature)
            feature_freqs[category][feature] = (share / tokens_count[category])
