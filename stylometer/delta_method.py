"""John Burrows' Delta Method in order to compare Federalist 64, the special
case, to other categories
"""

from operator import itemgetter
from typing import Dict, List

from math import fabs
from statistics import mean
from statistics import stdev
from statistics import NormalDist

from .helpers import get_n_most_frequent_words_occs


def get_feature_freqs(tokens: Dict[str, List[str]], features,
                      categories: List[str]):
    """Calculate frequencies of each feature in each category.

    Parameters
    ----------
    tokens : Dict of str and list of str
        The tokenized corpus.
    features
        The selected features.
    categories : list of str
        The categories of the features.

    Returns
    -------
    dict
        The frequencies of each feature in each category.

    """
    feature_freqs = dict()

    for category in categories:
        feature_freqs[category] = dict()
        tokens_count = len(tokens[category])

        for feature in features:
            feature_count = tokens[category].count(feature)
            feature_freqs[category][feature] = feature_count / tokens_count

    return feature_freqs


def get_feature_stats(features, categories: List[str], freqs):
    """Calculate the mean and standard deviation for each feature.

    Parameters
    ----------
    features
        The selected features.
    categories : list of str
        The categories of the features.
    freqs
        The frequencies of each feature.

    Returns
    -------
    dict
        The mean and standard deviation for each feature.

    """
    corpus_stats = dict()

    for feature in features:
        corpus_stats[feature] = dict()

        corpus_stats[feature]["mean"] = mean(
            [freqs[category][feature] for category in categories])
        corpus_stats[feature]["stdev"] = stdev(
            [freqs[category][feature] for category in categories])

    return corpus_stats


def get_feature_zscores(features, categories: List[str], stats, freqs):
    """Apply z-score to each feature in each category.

    Parameters
    ----------
    features
        The selected features.
    categories : list of str
        The categories of the features.
    stats
        The mean and standard deviation for each feature.
    freqs
        The frequencies of each feature.

    Returns
    -------
    dict
        The z-score for each feature.

    """
    feature_zscores = dict()

    for category in categories:
        feature_zscores[category] = dict()

        for feature in features:
            feature_zscore = NormalDist(stats[feature]["mean"],
                                        stats[feature]["stdev"]).zscore(
                                            freqs[category][feature])
            feature_zscores[category][feature] = feature_zscore

    return feature_zscores


def calculate_delta_scores(features, categories, zscores, specialcase):
    """Calculate Delta scores for each category.

    Parameters
    ----------
    features
        The selected features.
    categories
        The categories of the features.
    zscores
        z-scores of all categories except the special case.
    specialcase
        z-scores of the special case.

    Returns
    -------
    dict
        The Delta scores for each feature.

    """
    delta = dict()
    feature_count = len(features)

    for category in categories:
        score = [
            fabs(specialcase[feature] - zscores[category][feature])
            for feature in features
        ]
        delta[category] = sum(score) / feature_count
    return dict(sorted(delta.items(), key=itemgetter(1)))


def apply_delta_method(n: int, tokens: Dict[str, List[str]],
                       categories: List[str], special_case: str) -> None:
    """Apply John Burrows' Delta Method.

    Parameters
    ----------
    n : int
        The n most common words between the two texts.
    tokens : Dict of str and list of str
        The tokenized corpus.
    categories : list of str
        The names of the categories of the corpus.
    special_case : str
        The name of the special case category.

    """
    combined_corpus = list()

    # Select the most frequent tokens to be used as features
    for category in categories:
        combined_corpus += tokens[category]
    words_occs = get_n_most_frequent_words_occs(n, combined_corpus)
    features = [word for word, count in words_occs]

    feature_freqs = get_feature_freqs(tokens, features, categories)
    corpus_stats = get_feature_stats(features, categories, feature_freqs)
    feature_zscores = get_feature_zscores(features, categories, corpus_stats,
                                          feature_freqs)

    special_freqs = get_feature_freqs(tokens, features, list(special_case))
    special_zscores = get_feature_zscores(features, list(special_case),
                                          corpus_stats, special_freqs)

    # The first entry will be the lowest score and thus, the most likely author
    # of Federalist 64
    delta_scores = calculate_delta_scores(features, categories,
                                          feature_zscores,
                                          special_zscores[special_case])

    for k, v in delta_scores.items():
        print(f"The Delta score for {k} papers is: {v}")
