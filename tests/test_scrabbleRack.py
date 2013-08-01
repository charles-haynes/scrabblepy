from unittest import TestCase, TestLoader, TextTestRunner
from ScrabbleRack import ScrabbleRack, ScrabbleWord

__author__ = 'chaynes'


class TestScrabbleRack(TestCase):
    def test_blank_contains_one_letter_different(self):
        self.assertTrue(
            ScrabbleRack.RackFromWord("ace", 1).contains(ScrabbleWord.FromWord("aef")))

    def test_blank_does_not_contains_two_letters_different(self):
        self.assertFalse(
            ScrabbleRack.RackFromWord("ace", 1).contains(ScrabbleWord.FromWord("abef")))


suite = TestLoader().loadTestsFromTestCase(TestScrabbleRack)
TextTestRunner(verbosity=2).run(suite)
