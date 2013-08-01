#! /usr/bin/env python

__author__ = 'chaynes'

import re
import sys

blank_pattern = "\([^)]*\)|[A-Z]"

letters = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
           'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,
           '.': 0}


def score(word):
    """
    returns the scrabble score for a word, including bingo bonus

    :param word:
    :type word: str
    :rtype: int
    """

    word_length_with_blanks = len(re.sub("[()]", "", word))
    word_minus_blanks = re.sub(blank_pattern, "", word)
    letter_value = sum(letters[letter] for letter in word_minus_blanks)
    return letter_value + 50 if word_length_with_blanks >= 7 else letter_value


def main():
    """
    run the main program

    """
    for line in sys.stdin.read().split():
        print score(line), line


if __name__ == "__main__":
    main()