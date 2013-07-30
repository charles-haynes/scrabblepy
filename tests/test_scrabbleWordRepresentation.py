from unittest import TestCase
from ScrabbleWordRepresentation import ScrabbleWordRepresentation

__author__ = 'chaynes'


class TestScrabbleWordRepresentation(TestCase):
    def test_empty_contains_empty(self):
        self.assertTrue(ScrabbleWordRepresentation.FromWord("").contains(ScrabbleWordRepresentation.FromWord("")))

    def test_non_empty_contains_empty(self):
        self.assertTrue(ScrabbleWordRepresentation.FromWord("a").contains(ScrabbleWordRepresentation.FromWord("")))

    def test_empty_does_not_contains_empty(self):
        self.assertFalse(ScrabbleWordRepresentation.FromWord("").contains(ScrabbleWordRepresentation.FromWord("a")))

    def test_contains_itself(self):
        self.assertTrue(ScrabbleWordRepresentation.FromWord("ace").contains(ScrabbleWordRepresentation.FromWord("ace")))

    def test_contains_subset(self):
        self.assertTrue(ScrabbleWordRepresentation.FromWord("ace").contains(ScrabbleWordRepresentation.FromWord("ce")))

    def test_does_not_contains_superset(self):
        self.assertFalse(
            ScrabbleWordRepresentation.FromWord("ace").contains(ScrabbleWordRepresentation.FromWord("abce")))

    def test_does_not_contains_different(self):
        self.assertFalse(
            ScrabbleWordRepresentation.FromWord("ace").contains(ScrabbleWordRepresentation.FromWord("aef")))

    def test_blank_contains_one_letter_different(self):
        self.assertTrue(
            ScrabbleWordRepresentation.FromWord("ace", 1).contains(ScrabbleWordRepresentation.FromWord("aef")))

    def test_blank_does_not_contains_two_letters_different(self):
        self.assertFalse(
            ScrabbleWordRepresentation.FromWord("ace", 1).contains(ScrabbleWordRepresentation.FromWord("abef")))

    def test___sub__(self):
        self.assertEqual(ScrabbleWordRepresentation.FromWord("abcde") - ScrabbleWordRepresentation.FromWord("eca"),
                         ScrabbleWordRepresentation.FromWord("db"))