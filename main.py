#!/usr/bin/env python3
# Main file
# Introduction to stylometry techniques to determine authorship

### IMPORT

# Utils import
from load_data import sort_files_per_category
from word_spectrum import compute_word_spectrum


## FUNCTIONS

def main():
    # Sort the papers by author and other categories
    files = sort_files_per_category()
    # First approach: Mendenhall’s Characteristic Curves of Composition
    compute_word_spectrum(files)

if __name__ == "__main__":
    main()
