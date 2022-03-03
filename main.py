#!/usr/bin/env python3

# Main file

### IMPORT

# Utils import
from load_data import sort_files_per_category
from analysis import compute_word_spectrum

def main():
    files = sort_files_per_category()
    compute_word_spectrum(files)

if __name__ == "__main__":
    main()
