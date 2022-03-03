#!/usr/bin/env python3
# Main file
# Introduction to stylometry techniques to determine authorship

### IMPORT

# Utils import
from load_data import tokenize_corpus
from word_spectrum import compute_word_spectrum


## FUNCTIONS

def main():
    # Sort and tokenize all the papers
    corpus = tokenize_corpus()
    # First approach: Mendenhall’s Characteristic Curves of Composition
    compute_word_spectrum(corpus)

if __name__ == "__main__":
    main()
