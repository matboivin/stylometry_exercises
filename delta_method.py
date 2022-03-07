#!/usr/bin/env python3
# John Burrows' Delta Method

__all__ = ["get_feature_freqs", "get_feature_stats", "get_feature_zscores", "apply_delta_method"]

### IMPORT

# Python librairies import
import math
from statistics import mean
from statistics import stdev
from statistics import NormalDist

# Utils import
from utils import get_n_most_frequent_words_occs


## FUNCTIONS

def get_feature_freqs(tokens, features, categories):
    """Calculate frequencies of each feature in each category

    Args:
        tokens: The tokenized corpus
        features: The selected features
        categories: The categories of the features
    """
    feature_freqs = dict()

    for category in categories:
        feature_freqs[category] = dict()
        tokens_count = len(tokens[category])

        for feature in features:
            feature_count = tokens[category].count(feature)
            feature_freqs[category][feature] = feature_count / tokens_count

    return feature_freqs


def get_feature_stats(features, categories, freqs):
    """Calculate the mean and standard deviation for each feature

    Args:
        features: The selected features
        categories: The categories of the features
        freqs: The frequencies of each feature
    """
    corpus_stats = dict()

    for feature in features:
        corpus_stats[feature] = dict()

        corpus_stats[feature]["mean"] = mean([freqs[category][feature] for category in categories])
        corpus_stats[feature]["stdev"] = stdev([freqs[category][feature] for category in categories])

    return corpus_stats


def get_feature_zscores(features, categories, stats, freqs):
    """Apply z-score to each feature in each category

    Args:
        features: The selected features
        categories: The categories of the features
        stats: The mean and standard deviation for each feature
        freqs: The frequencies of each feature
    """
    feature_zscores = dict()

    for category in categories:
        feature_zscores[category] = dict()

        for feature in features:
            feature_zscore = NormalDist(
                    stats[feature]["mean"],
                    stats[feature]["stdev"]
                ).zscore(freqs[category][feature])
            feature_zscores[category][feature] = feature_zscore

    return feature_zscores


def apply_delta_method(n, corpus, categories, specialcase):
    combined_corpus = list()

    categories = [category for category in categories if category not in specialcase]

    # Select the most frequent tokens to be used as features
    for category in categories:
        combined_corpus += corpus[category]
    words_occs = get_n_most_frequent_words_occs(n, combined_corpus)
    features = [word for word,count in words_occs]

    # Get the proportion of each feature per category
    feature_freqs = get_feature_freqs(corpus, features, categories)
    # Calculate the mean and standard deviation for each feature
    corpus_stats = get_feature_stats(features, categories, feature_freqs)
    # Calculate z-score for each feature per category
    feature_zscores = get_feature_zscores(features, categories, corpus_stats, feature_freqs)
    # Same for special case
    specialcase_freqs = get_feature_freqs(corpus, features, specialcase)
    specialcase_zscores = get_feature_zscores(features, specialcase, corpus_stats, specialcase_freqs)
