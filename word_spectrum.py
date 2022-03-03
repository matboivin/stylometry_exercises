#!/usr/bin/env python3
# Mendenhall’s Characteristic Curves of Composition

__all__ = ["compute_word_spectrum"]

### IMPORT

# Python librairies import
import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Utils import
from constants import *


## FUNCTIONS

def get_word_len_dist(words):
    """Get the distribution of word lengths from a list of words"""
    word_lengths = [len(w) for w in words]
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

def compute_word_spectrum(corpus):
    """Arrange the words using their length and frequency"""
    for category in CATEGORIES:
        save_graph(get_word_len_dist(corpus[category]), category)
