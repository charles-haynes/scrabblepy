from unittest import TestCase
from scrabble import words_for_rack, representation

__author__ = 'chaynes'


class TestWords_for_rack(TestCase):
    def setUp(self):
        self.word_list = {representation("spot"): ["spot", "pots", "stop", "tops"],
                          representation("stops"): ["stops", "spots"],
                          representation("pot"): ["pot"],
                          representation("ports"): ["ports"],
                          representation("sporty"): ["sporty"],
                          representation("stroppy"): ["stroppy"]}

    def test_words_for_rack(self):
        word_list_expected = ["spot", "pots", "stop", "tops", "stops", "spots", "pot"]

        self.assertItemsEqual(words_for_rack("spots", self.word_list), word_list_expected)

    def test_words_for_rack_with_blank(self):
        word_list_expected = ["spot", "pots", "stop", "tops", "stops", "spots", "pot", "ports"]

        self.assertItemsEqual(words_for_rack("spots.", self.word_list), word_list_expected)

    def test_words_for_rack_with_two_blank(self):
        word_list_expected = ["spot", "pots", "stop", "tops", "stops", "spots", "pot", "ports", "sporty"]

        self.assertItemsEqual(words_for_rack("spots..", self.word_list), word_list_expected)