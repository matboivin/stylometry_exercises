# Stylometry exercises

Determine authorship in Python.

## Requirements

* Python 3.9 or greater
* [`poetry`](https://python-poetry.org/)

## Installation

Clone the repository and change it to your working directory.

```console
$ poetry install
```

## Usage

```console
stylometer [-h] method_number

Run stylometry methods on the Federalist Papers.

positional arguments:
  method_number  A number to select one of the three methods.
                 1: Mendenhall's Characteristic Curves of Composition
                 2: Kilgariff's Chi-Squared Method
                 3: John Burrows' Delta Method

optional arguments:
  -h, --help     show this help message and exit
```

## Acknowledgements

Lesson by François Dominic Laramée on [Programming Historian](https://programminghistorian.org/en/lessons/introduction-to-stylometry-with-python)
