"""Constant values."""

from typing import List

__all__: List[str] = [
    "CATEGORIES", "CORPUS_LANGUAGE", "DATA_DIR", "OUTPUT_DIR"
]

CATEGORIES: List[str] = [
    "madison", "hamilton", "jay", "cowritten", "disputed", "specialcase"
]
CORPUS_LANGUAGE: str = "english"
DATA_DIR: str = "data"
OUTPUT_DIR: str = "output"
