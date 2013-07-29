from unittest import TestCase, TestLoader, TextTestRunner
from scrabble import words_for_rack
from tests.test_score import TestScore

__author__ = 'chaynes'


class TestWords_for_rack(TestCase):
    def setUp(self):
        self.word_list = ["spot", "pots", "stop", "tops", "stops", "spots", "pot", "ports", "sporty", "stroppy"]

    def test_words_for_rack(self):
        word_list_expected = ["spot", "pots", "stop", "tops", "stops", "spots", "pot"]

        self.assertItemsEqual(words_for_rack("spots", self.word_list), word_list_expected)

    def test_words_for_rack_with_blank(self):
        word_list_expected = ["spot", "pots", "stop", "tops", "stops", "spots", "pot", "ports"]

        self.assertItemsEqual(words_for_rack("spots.", self.word_list), word_list_expected)

    def test_words_for_rack_with_two_blank(self):
        word_list_expected = ["spot", "pots", "stop", "tops", "stops", "spots", "pot", "ports", "sporty"]

        self.assertItemsEqual(words_for_rack("spots..", self.word_list), word_list_expected)


suite = TestLoader().loadTestsFromTestCase(TestWords_for_rack)
TextTestRunner(verbosity=2).run(suite)