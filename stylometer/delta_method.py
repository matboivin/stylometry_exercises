"""John Burrows' Delta Method.

Compare Federalist 64, the special case, to other categories
"""

from math import fabs
from operator import itemgetter
from statistics import NormalDist, mean, stdev
from typing import Dict, List, Tuple

from .helpers import get_n_most_frequent_words_occs


def get_feature_freqs(
    tokens: Dict[str, List[str]], categories: List[str], features: List[str]
) -> Dict[str, Dict[str, float]]:
    """Calculate frequencies of each feature in each category.

    Parameters
    ----------
    tokens : Dict of str and list of str
        The tokenized corpus.
    categories : list of str
        The categories of the features.
    features : list of str
        The selected features.

    Returns
    -------
    dict of str, dict of str, float
        The frequencies of each feature in each category.

    """
    feature_freqs: Dict[str, Dict[str, float]] = {}

    for category in categories:
        feature_freqs[category] = {}
        tokens_count: int = len(tokens[category])

        for feature in features:
            feature_count: int = tokens[category].count(feature)
            feature_freqs[category][feature] = feature_count / tokens_count

    return feature_freqs


def get_feature_stats(
    categories: List[str],
    features: List[str],
    freqs: Dict[str, Dict[str, float]],
) -> Dict[str, Dict[str, float]]:
    """Calculate the mean and standard deviation for each feature.

    Parameters
    ----------
    categories : list of str
        The categories of the features.
    features : list of str
        The selected features.
    freqs : dict of str, dict of str, float
        The frequencies of each feature.

    Returns
    -------
    dict of str, dict of str, float
        The mean and standard deviation for each feature.

    """
    corpus_stats: Dict[str, Dict[str, float]] = {}

    for feature in features:
        corpus_stats[feature] = {}

        corpus_stats[feature]["mean"] = mean(
            [freqs[category][feature] for category in categories]
        )
        corpus_stats[feature]["stdev"] = stdev(
            [freqs[category][feature] for category in categories]
        )

    return corpus_stats


def get_feature_zscores(
    features: List[str],
    categories: List[str],
    freqs: Dict[str, Dict[str, float]],
    stats: Dict[str, Dict[str, float]],
) -> Dict[str, Dict[str, float]]:
    """Apply z-score to each feature in each category.

    Parameters
    ----------
    features : list of str
        The selected features.
    categories : list of str
        The categories of the features.
    freqs : dict of str, dict of str, float
        The frequencies of each feature.
    stats : dict of str, dict of str, float
        The mean and standard deviation for each feature.

    Returns
    -------
    dict of str, dict of str, float
        The z-score for each feature.

    """
    feature_zscores: Dict[str, Dict[str, float]] = {}

    for category in categories:
        feature_zscores[category] = {}

        for feature in features:
            feature_zscore: float = NormalDist(
                stats[feature]["mean"], stats[feature]["stdev"]
            ).zscore(freqs[category][feature])
            feature_zscores[category][feature] = feature_zscore

    return feature_zscores


def calculate_delta_scores(
    categories: List[str],
    features: List[str],
    zscores: Dict[str, Dict[str, float]],
    specialcase: Dict[str, float],
) -> Dict[str, float]:
    """Calculate Delta scores for each category.

    Parameters
    ----------
    categories : list of str
        The categories of the features.
    features : list of str
        The selected features.
    zscores : dict of str, dict of str, float
        z-scores of all categories except the special case.
    specialcase : dict of str, float
        z-scores of the special case.

    Returns
    -------
    dict of str, float
        The Delta scores for each feature.

    """
    delta: Dict[str, float] = {}
    feature_count: int = len(features)

    for category in categories:
        score: List[float] = [
            fabs(specialcase[feature] - zscores[category][feature])
            for feature in features
        ]
        delta[category] = sum(score) / feature_count
    return dict(sorted(delta.items(), key=itemgetter(1)))


def apply_delta_method(
    n: int,
    tokens: Dict[str, List[str]],
    categories: List[str],
    special_case: str,
) -> None:
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
    combined_corpus: List[str] = []
    for category in categories:
        combined_corpus += tokens[category]

    # Select the most frequent tokens to be used as features
    words_occs: List[Tuple[str, int]] = get_n_most_frequent_words_occs(
        n, combined_corpus
    )
    features: List[str] = [word for word, count in words_occs]

    feature_freqs: Dict[str, Dict[str, float]] = get_feature_freqs(
        tokens, categories, features
    )
    corpus_stats: Dict[str, Dict[str, float]] = get_feature_stats(
        categories, features, feature_freqs
    )
    feature_zscores: Dict[str, Dict[str, float]] = get_feature_zscores(
        features, categories, feature_freqs, corpus_stats
    )

    special_freqs: Dict[str, Dict[str, float]] = get_feature_freqs(
        tokens, [special_case], features
    )
    special_zscores: Dict[str, Dict[str, float]] = get_feature_zscores(
        features, [special_case], special_freqs, corpus_stats
    )

    # The first entry will be the lowest score and thus, the most likely author
    # of Federalist 64
    delta_scores: Dict[str, float] = calculate_delta_scores(
        categories, features, feature_zscores, special_zscores[special_case]
    )

    for category, score in delta_scores.items():
        print(f"The Delta score for {category} papers is: {score}")
