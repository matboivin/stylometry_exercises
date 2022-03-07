#!/usr/bin/env python3
# Load the Federalist Papers and sort them by categories:
#  - written by Alexander Hamilton
#  - written by James Madison
#  - written by John Jay
#  - most probably co-written by Madison and Hamilton
#  - disputed between Hamilton and Madison
#  - the last one is a special case

__all__ = ["combine_files", "sort_files_per_category", "tokenize_corpus"]

## IMPORT

# Python librairies import
import nltk
from nltk.tokenize import word_tokenize

# Constants imports
from constants import *
from tools.src.removal import remove_punctuation
from tools.src.removal import remove_stopwords


### FUNCTIONS

def combine_files(file_idx):
    """Combine the files matching the given indices

    Args:
        file_idx: An array of file indices
    """
    files = []

    for idx in file_idx:
        with open(f"{DATA_DIR}/federalist_{idx}.txt") as f:
            files.append(f.read())

    return "\n".join(files)


def sort_files_per_category():
    """Create a dict of the files sorted by category"""
    idx_per_category = {
        "madison":   [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
        "hamilton":  [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                      25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                      61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                      78, 79, 80, 81, 82, 83, 84, 85],
        "jay":       [2, 3, 4, 5],
        "cowritten": [18, 19, 20],
        "disputed":  [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
        "specialcase": [64]
    }
    files_per_category = {}

    for category,idx in idx_per_category.items():
        files_per_category[category] = combine_files(idx)

    return files_per_category


def tokenize_corpus(corpus):
    """Tokenize all the corpus"""
    result = {}

    for category in CATEGORIES:
        tokens = nltk.word_tokenize(
            remove_punctuation(corpus[category]),
            language=CORPUS_LANGUAGE
        )
        tokens = tokens[1:] # Remove the number at the beginning of the document
        tokens = [token.lower() for token in tokens]
        #result[category] = remove_stopwords(CORPUS_LANGUAGE, tokens)
        result[category] = tokens

    return result
