"""Helper functions."""

from argparse import ArgumentParser, ArgumentTypeError, Namespace
from typing import List, Tuple

from nltk import FreqDist


def parse_args() -> Namespace:
    """Parse the program's arguments.

    Returns
    -------
    argparse.Namespace
        The program's arguments.

    Raises
    ------
    ArgumentTypeError
        If the method number is not 1, 2 or 3.

    """
    parser: ArgumentParser = ArgumentParser(
        prog="stylometer",
        description="Run stylometry methods on the Federalist Papers.",
    )

    parser.add_argument(
        "method_number",
        type=int,
        help="""A number to select one of the three methods.\n

1: Mendenhall's Characteristic Curves of Composition
2: Kilgariff's Chi-Squared Method
3: John Burrows' Delta Method
""",
    )

    args: Namespace = parser.parse_args()

    if args.method_number not in [1, 2, 3]:
        raise ArgumentTypeError(
            "Select a method by entering either 1, 2 or 3."
        )

    return args


def get_n_most_frequent_words_occs(
    n: int, corpus: List[str]
) -> List[Tuple[str, int]]:
    """Get the n most frequent words and their frequency occurence from corpus.

    Parameters
    ----------
    n : int
        The n most common words between the two texts.
    corpus : list of str
        A list of texts.

    Returns
    -------
    list of (str, int)
        The n most frequent words and their frequency occurence.

    """
    fdist: FreqDist = FreqDist(corpus)
    words_occs: List[Tuple[str, int]] = list(fdist.most_common(n))

    return words_occs
