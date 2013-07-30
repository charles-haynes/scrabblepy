#! /usr/bin/env python
from ScrabbleWord import ScrabbleWord

__author__ = 'chaynes'

import sys

def words_for_rack(rack, word_list):
    rack_bag = ScrabbleWord.FromWord(rack, rack.count("."))
    for word in word_list:
        word = word.rstrip("\r\n")
        word_bag = ScrabbleWord.FromWord(word)
        if rack_bag.contains(word_bag):
            yield word

def main():
    """
    main program

    :rtype : none
    """

    word_list_file_name = "/users/chaynes/projects/Personal/scrabble/twl06.txt"
    for word in words_for_rack(sys.argv[1], open(word_list_file_name)):
        print word

if __name__ == "__main__":
    main()