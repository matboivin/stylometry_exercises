#!/usr/bin/env python3

# Load the Federalist Papers and sort them by categories:
#  - written by Alexander Hamilton
#  - written by James Madison
#  - written by John Jay
#  - most probably co-written by Madison and Hamilton
#  - disputed between Hamilton and Madison
#  - the last one is a special case

### FUNCTIONS

def combine_files(file_idx):
    """Combine the files matching the given indices
    
    Args:
        file_idx: an array of file indices
    """
    files = []

    for idx in file_idx:
        with open(f"data/federalist_{idx}.txt") as f:
            files.append(f.read())
    return "\n".join(files)

def sort_files_per_category():
    idx_per_category = {
        "madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
        "hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                    61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                    78, 79, 80, 81, 82, 83, 84, 85],
        "jay": [2, 3, 4, 5],
        "cowritten": [18, 19, 20],
        "disputed": [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
        "specialcase": [64]
    }
    files_per_category = {}

    for category,idx in idx_per_category.items():
        files_per_category[category] = combine_files(idx)
    return files_per_category