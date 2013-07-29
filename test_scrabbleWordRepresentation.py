from unittest import TestCase

from ScrabbleWordRepresentation import ScrabbleWordRepresentation

__author__ = 'chaynes'


class TestScrabbleWordRepresentation(TestCase):
    def test_len_of_empty_is_zero(self):
        self.assertEqual(len(ScrabbleWordRepresentation.fromString("")), 0)

    def test_len_of_non_empty_is_non_zero(self):
        self.assertEqual(len(ScrabbleWordRepresentation.fromString("abc")), 3)

    def test_len_of_with_dups_ignores_dups(self):
        self.assertEqual(len(ScrabbleWordRepresentation.fromString("aabcc")), 3)