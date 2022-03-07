#!/usr/bin/env python3
# Main file
# Introduction to stylometry techniques to determine authorship

### IMPORT

# Utils import
import sys
from constants import CATEGORIES
from utils import print_usage

# Data utils import
from load_data import tokenize_corpus
from load_data import sort_files_per_category

# Analysis functions import
from word_spectrum import compute_word_spectrum
from chisquared import chi_square_test
from delta_method import apply_delta_method


## FUNCTIONS

def main(argv):
    if len(argv) != 2 or argv[1] == "-h":
        print_usage(argv[0])

    elif argv[1] not in "123":
        print(f"Error: invalid argument.\nTry 'python {argv[0]} -h' for more information.")

    else:
        # Sort and tokenize all the papers
        corpus = sort_files_per_category()
        tokens = tokenize_corpus(corpus)

        # First approach: Mendenhall's Characteristic Curves of Composition
        if argv[1] == "1":
            print("Mendenhall's Characteristic Curves of Composition")
            compute_word_spectrum(tokens)

        # Second approach: Kilgariff's Chi-Squared Method
        elif argv[1] == "2":
            print("Kilgariff's Chi-Squared Method")
            chi_square_test(500, tokens["hamilton"], tokens["madison"], tokens["disputed"])

        # Third approach: John Burrows' Delta Method
        else:
            print("John Burrows' Delta Method")
            apply_delta_method(30, tokens, CATEGORIES, CATEGORIES[-1:])


if __name__ == "__main__":
    main(sys.argv)
