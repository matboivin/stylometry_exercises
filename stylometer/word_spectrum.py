"""Mendenhall's Characteristic Curves of Composition"""

from typing import Dict, List

from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure

from .constants import CATEGORIES, OUTPUT_DIR


def get_word_len_dist(words: List[str]) -> FreqDist:
    """Get the distribution of word lengths from a list of words.

    Parameters
    ----------
    words : list of str
        Words.

    Returns
    -------
    FreqDist
        The frequency distribution.

    """
    word_lengths: List[int] = [len(w) for w in words]

    return FreqDist(word_lengths)


def save_graph(fdist: FreqDist, category: str) -> None:
    """Save a graphic representation of a frequency distribution.

    Parameters
    ----------
    fdist : FreqDist
        The frequency distribution.
    category : str
        The category name to be used for filename and graph title.

    """
    filename: str = OUTPUT_DIR + "/" + category + ".png"

    plt.ion()
    fig: Figure = plt.figure(figsize=(12, 6))
    fdist.plot(15, title=category)
    fig.savefig(filename, bbox_inches="tight")
    plt.ioff()

    print(f"Saved graph in '{filename}'")


def compute_word_spectrum(tokens: Dict[str, List[str]]) -> None:
    """Arrange the words using their length and frequency.

    Parameters
    ----------
    tokens : Dict of str and list of str
        The tokenized corpus.

    """
    for category in CATEGORIES:
        fdist: FreqDist = get_word_len_dist(tokens[category])
        save_graph(fdist, category)
