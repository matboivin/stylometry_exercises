#!/usr/bin/env python3
# Style analysis

__all__ = ["compute_word_spectrum"]

### IMPORT

# Python librairies import
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Utils import
from constants import *
from tools.src.removal import remove_punctuation


## FUNCTIONS

# Mendenhall’s Characteristic Curves of Composition

def get_word_len_dist(text):
    """Get the distribution of word lengths from a given text"""
    tokens = nltk.word_tokenize(remove_punctuation(text), language=CORPUS_LANGUAGE)
    tokens = tokens[1:] # remove number
    word_lengths = [len(token) for token in tokens]
    return FreqDist(word_lengths)

def save_graph(fdist, category):
    """Save a graphic representation of the distribution"""
    filename = OUTPUT_DIR + "/" + category + ".png"
    plt.ion()
    fig = plt.figure(figsize=(12,6))
    fdist.plot(15, title=category)
    fig.savefig(filename, bbox_inches = "tight")
    plt.ioff()
    print(f"Saved graph in '{filename}'.")

def compute_word_spectrum(files):
    """Arrange the words using their length and frequency

    Args:
        files: the files sorted by category
    """
    for category in CATEGORIES:
        save_graph(get_word_len_dist(files[category]), category)
