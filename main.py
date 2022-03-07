#!/usr/bin/env python3
# Main file
# Introduction to stylometry techniques to determine authorship

### IMPORT

# Utils import
import sys

# Data utils import
from load_data import tokenize_corpus

# Analysis functions import
from word_spectrum import compute_word_spectrum
from chisquared import chi_square_test


## FUNCTIONS

def main(argv):
    if len(argv) != 2 or argv[0] == "-h":
        print(f"""Usage: python {argv[0]} <number>
    1: Mendenhall's Characteristic Curves of Composition
    2: Kilgariff's Chi-Squared Method""")

    elif argv[1] not in "123":
        print(f"Error: invalid argument.\nTry 'python {argv[0]} -h' for more information.")

    else:
        # Sort and tokenize all the papers
        corpus = tokenize_corpus()

        # First approach: Mendenhall's Characteristic Curves of Composition
        if argv[1] == "1":
            print("Mendenhall's Characteristic Curves of Composition")
            compute_word_spectrum(corpus)

        # Second approach: Kilgariff's Chi-Squared Method
        elif argv[1] == "2":
            print("Kilgariff's Chi-Squared Method")
            chi_square_test(500, corpus["hamilton"], corpus["madison"], corpus["disputed"])

        # Third approach: John Burrows' Delta Method
        else:
            print("John Burrows' Delta Method")


if __name__ == "__main__":
    main(sys.argv)
