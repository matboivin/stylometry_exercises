"""Program's entrypoint."""

from argparse import Namespace
from typing import Dict, List

from .chisquared import chi_square_test
from .constants import CATEGORIES
from .delta_method import apply_delta_method
from .helpers import parse_args
from .load_data import sort_files_per_category, tokenize_corpus
from .word_spectrum import compute_word_spectrum


def main(method_number: int) -> None:
    """Run program.

    Parameters
    ----------
    method_number : int
        A number corresponding to one of the three following methods:
        1: Mendenhall's Characteristic Curves of Composition
        2: Kilgariff's Chi-Squared Method
        3: John Burrows' Delta Method

    """
    # Sort and tokenize all the papers
    corpus: Dict[str, str] = sort_files_per_category()
    tokens: Dict[str, List[str]] = tokenize_corpus(corpus)

    # First approach: Mendenhall's Characteristic Curves of Composition
    if method_number == 1:
        compute_word_spectrum(tokens)

    # Second approach: Kilgariff's Chi-Squared Method
    elif method_number == 2:
        chi_square_test(500, tokens, "hamilton", "madison", "disputed")

    # Third approach: John Burrows' Delta Method
    elif method_number == 3:
        apply_delta_method(30, tokens, CATEGORIES[:-1], CATEGORIES[-1])


def entrypoint() -> None:
    """Program's entrypoint."""
    args: Namespace = parse_args()

    main(args.method_number)


if __name__ == "__main__":
    entrypoint()
