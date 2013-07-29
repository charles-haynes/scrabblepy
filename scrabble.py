#! /usr/bin/env python

__author__ = 'chaynes'

from ScrabbleWordRepresentation import ScrabbleWordRepresentation
import sys

def representation(word):
    return ScrabbleWordRepresentation.fromString(word)

def words_for_rack(rack, word_list):
    rack_bag = representation(rack)
    blanks = rack.count('.')
    for word in word_list:
        word = word.rstrip("\r\n")
        word_bag = representation(word)
        blanks_needed = len(word_bag - rack_bag)
        if blanks_needed <= blanks:
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