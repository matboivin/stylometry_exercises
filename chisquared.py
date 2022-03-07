#!/usr/bin/env python3
# Kilgariff's Chi-Squared Method

__all__ = ["calculate_chisquared", "chi_square_test"]

### IMPORT

# Utils import
from operator import itemgetter
from utils import get_n_most_frequent_words_occs


def calculate_chisquared(n, text_author, text_unknown):
    """Calculate Chi-Squared to determine the author of an anonymous text

    Args:
        n: The n most common words between the two texts
        text_author: Text written by an identified author
        text_unknown: Anonymous text
    """
    chisquared = 0
    combined_corpus = text_author + text_unknown
    words_occs = get_n_most_frequent_words_occs(n, combined_corpus)
    author_share = len(text_author) / len(combined_corpus)

    for word,count in words_occs:
        # Word occurences
        author_count = text_author.count(word)
        anon_count = text_unknown.count(word)
        # Expected word occurences
        expected_author_count = count * author_share
        expected_anon_count = count * (1 - author_share)
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


def chi_square_test(n, tokens, author1, author2, unknown):
    """Calculate Chi-Squared to determine the author of the disputed papers.
       The smallest distance between the disputed papers and one of the authors
       means the latest is probably the author of the disputed papers.
    """
    chisquared = dict()
    chisquared[author1] = calculate_chisquared(n, tokens[author1], tokens[unknown])
    chisquared[author2] = calculate_chisquared(n, tokens[author2], tokens[unknown])

    chisquared = dict(sorted(chisquared.items(), key=itemgetter(1)))

    for k,v in chisquared.items():
        print(f"The Chi-squared statistic for {k} papers is: {v}")
