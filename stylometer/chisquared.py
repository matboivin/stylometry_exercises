"""Kilgariff's Chi-Squared Method."""

from operator import itemgetter
from typing import Dict, List, Tuple

from .helpers import get_n_most_frequent_words_occs


def calculate_chisquared(
    n: int, text_author: List[str], text_unknown: List[str]
) -> float:
    """Calculate Chi-Squared to determine the author of an anonymous text.

    Parameters
    ----------
    n : int
        The n most common words between the two texts.
    text_author : list of str
        Text written by an identified author.
    text_unknown : list of str
        Anonymous text.

    Returns
    -------
    float
        The chisquared value.

    """
    chisquared: float = 0
    combined_corpus: List[str] = text_author + text_unknown
    words_occs: List[Tuple[str, int]] = get_n_most_frequent_words_occs(
        n, combined_corpus
    )
    author_share: float = len(text_author) / len(combined_corpus)

    for word, count in words_occs:
        # Word occurences
        author_count: int = text_author.count(word)
        anon_count: int = text_unknown.count(word)
        # Expected word occurences
        expected_author_count: float = count * author_share
        expected_anon_count: float = count * (1 - author_share)
        # Update Chi-squared statistic
        chisquared += (
            (author_count - expected_author_count)
            * (author_count - expected_author_count)
            / expected_author_count
        )
        chisquared += (
            (anon_count - expected_anon_count)
            * (anon_count - expected_anon_count)
            / expected_anon_count
        )
    return chisquared


def chi_square_test(
    n: int,
    tokens: Dict[str, List[str]],
    author1: str,
    author2: str,
    unknown: str,
) -> None:
    """Calculate Chi-Squared to determine the author of the disputed papers.

       The smallest distance between the disputed papers and one of the authors
       means the latest is probably the author of the disputed papers.

    Parameters
    ----------
    n : int
        The n most common words between the two texts.
    tokens : Dict of str and list of str
        The tokenized corpus.
    author1 : str
        First author key in corpus.
    author2 : str
        Second author key in corpus.
    unknown : str
        Unknown author key in corpus.

    """
    chisquared: Dict[str, float] = {}
    chisquared[author1] = calculate_chisquared(
        n, tokens[author1], tokens[unknown]
    )
    chisquared[author2] = calculate_chisquared(
        n, tokens[author2], tokens[unknown]
    )

    chisquared = dict(sorted(chisquared.items(), key=itemgetter(1)))

    for author, value in chisquared.items():
        print(f"The Chi-squared statistic for {author} papers is: {value}")
