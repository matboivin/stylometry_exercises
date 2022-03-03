#!/usr/bin/env python3
# Kilgariff’s Chi-Squared Method

__all__ = ["get_n_frequent_words", "chi_square_test"]

### IMPORT

# Python librairies import
import nltk
from nltk.probability import FreqDist

# Utils import
from constants import CORPUS_LANGUAGE


## FUNCTIONS

def get_n_frequent_words(n, corpus):
    """Get the n most frequent words from a corpus"""
    fdist = nltk.FreqDist(corpus)
    frequent_words = fdist.most_common(n)
    return frequent_words

def calculate_chisquared(n, text_author, text_unknown):
    """Calculate Chi-Squared to determine the author of an anonymous text

    Args:
        n: The n most common words between the two texts
        text_author: Text written by an identified author
        text_unknown: Anonymous text
    """
    chisquared = 0
    joint_corpus = (text_author + text_unknown)
    frequent_words = get_n_frequent_words(n, joint_corpus)
    author_share = (len(text_author) / len(joint_corpus))

    for word,count in frequent_words:
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


def chi_square_test(n, hamilton_papers, madison_papers, disputed):
    """Calculate Chi-Squared to determine the author of the disputed papers.
       The smallest distance between the disputed papers and one of the authors
       means the latest is probably the author of the disputed papers.
    """
    hamilton_chisquared = calculate_chisquared(n, hamilton_papers, disputed)
    madison_chisquared = calculate_chisquared(n, madison_papers, disputed)

    print(f"The Chi-squared statistic for Hamilton is {hamilton_chisquared}")
    print(f"The Chi-squared statistic for Madison is {madison_chisquared}")
