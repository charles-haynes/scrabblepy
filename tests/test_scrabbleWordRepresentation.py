from unittest import TestCase, TestLoader, TextTestRunner
from ScrabbleWord import ScrabbleWord

__author__ = 'chaynes'


class TestScrabbleWord(TestCase):
    def test_representation_unordered(self):
        self.assertEqual(ScrabbleWord.FromWord("spot"), ScrabbleWord.FromWord("stop"))

    def test_representation_keeps_repetition(self):
        self.assertNotEquals(ScrabbleWord.FromWord("stops"), ScrabbleWord.FromWord("stop"))

    def test_empty_contains_empty(self):
        self.assertTrue(ScrabbleWord.FromWord("").contains(ScrabbleWord.FromWord("")))

    def test_non_empty_contains_empty(self):
        self.assertTrue(ScrabbleWord.FromWord("a").contains(ScrabbleWord.FromWord("")))

    def test_empty_does_not_contains_empty(self):
        self.assertFalse(ScrabbleWord.FromWord("").contains(ScrabbleWord.FromWord("a")))

    def test_contains_itself(self):
        self.assertTrue(ScrabbleWord.FromWord("ace").contains(ScrabbleWord.FromWord("ace")))

    def test_contains_subset(self):
        self.assertTrue(ScrabbleWord.FromWord("ace").contains(ScrabbleWord.FromWord("ce")))

    def test_does_not_contains_superset(self):
        self.assertFalse(
            ScrabbleWord.FromWord("ace").contains(ScrabbleWord.FromWord("abce")))

    def test_does_not_contains_different(self):
        self.assertFalse(
            ScrabbleWord.FromWord("ace").contains(ScrabbleWord.FromWord("aef")))

    def test_blank_contains_one_letter_different(self):
        self.assertTrue(
            ScrabbleWord.FromWord("ace", 1).contains(ScrabbleWord.FromWord("aef")))

    def test_blank_does_not_contains_two_letters_different(self):
        self.assertFalse(
            ScrabbleWord.FromWord("ace", 1).contains(ScrabbleWord.FromWord("abef")))

    def test___sub__(self):
        self.assertEqual(ScrabbleWord.FromWord("abcde") - ScrabbleWord.FromWord("eca"),
                         ScrabbleWord.FromWord("db"))


suite = TestLoader().loadTestsFromTestCase(TestScrabbleWord)
TextTestRunner(verbosity=2).run(suite)