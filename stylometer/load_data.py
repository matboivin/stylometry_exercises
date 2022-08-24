"""Load the Federalist Papers and sort them by categories.

- written by Alexander Hamilton
- written by James Madison
- written by John Jay
- most probably co-written by Madison and Hamilton
- disputed between Hamilton and Madison
- the last one is a special case
"""

from typing import Dict, List

import nltk

from textools.removal import remove_punctuation, remove_stopwords

from .constants import CATEGORIES, CORPUS_LANGUAGE, DATA_DIR


def combine_files(indices: List[int]) -> str:
    """Combine all the files of a category using their indices.

    Parameters
    ----------
    indices : list of int
        Indices of a category.

    Returns
    -------
    str
        The combined files as string.

    """
    files: List[str] = []

    for index in indices:
        with open(
            f"{DATA_DIR}/federalist_{index}.txt", encoding="utf-8"
        ) as file_handle:
            files.append(file_handle.read())

    return "\n".join(files)


def sort_files_per_category() -> Dict[str, str]:
    """Create a dict of the files sorted by category.

    Returns
    -------
    dict of str
        The files sorted per category.

    """
    category_indices: Dict[str, List[int]] = {
        "madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
        "hamilton": [
            1,
            6,
            7,
            8,
            9,
            11,
            12,
            13,
            15,
            16,
            17,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            59,
            60,
            61,
            65,
            66,
            67,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
        ],
        "jay": [2, 3, 4, 5],
        "cowritten": [18, 19, 20],
        "disputed": [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
        "specialcase": [64],
    }
    files_per_category: Dict[str, str] = {}

    for category, indices in category_indices.items():
        files_per_category[category] = combine_files(indices)

    return files_per_category


def tokenize_corpus(corpus: Dict[str, str]) -> Dict[str, List[str]]:
    """Tokenize all the corpus.

    Parameters
    ----------
    corpus : dict of str
        The corpus ordered by categories.

    Returns
    -------
    Dict of str and list of str
        The tokenized corpus.

    """
    corpus_tokens: Dict[str, List[str]] = {}

    for category in CATEGORIES:
        tokens: List[str] = nltk.word_tokenize(
            remove_punctuation(corpus[category]), language=CORPUS_LANGUAGE
        )
        # Remove the number at the beginning of the document
        tokens = [token.lower() for token in tokens[1:]]
        corpus_tokens[category] = remove_stopwords(CORPUS_LANGUAGE, tokens)

    return corpus_tokens
