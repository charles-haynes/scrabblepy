#! /usr/bin/env python
from ScrabbleRack import ScrabbleRack, ScrabbleWord

__author__ = 'chaynes'

import sys


def words_for_rack(rack, word_list):
    rack_bag = ScrabbleRack.RackFromWord(rack, rack.count("."))
    for word in word_list:
        word_bag = ScrabbleWord.FromWord(word)
        if rack_bag.contains(word_bag):
            yield word


def main():
    """
    main program

    :rtype : none
    """

    for word in words_for_rack(sys.argv[1], sys.stdin.read().split()):
        print word


if __name__ == "__main__":
    main()