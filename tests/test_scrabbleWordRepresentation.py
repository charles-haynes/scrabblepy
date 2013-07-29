from unittest import TestCase, TestLoader, TextTestRunner
from ScrabbleWordRepresentation import ScrabbleWordRepresentation

__author__ = 'chaynes'


class TestScrabbleWordRepresentation(TestCase):
    def test_len_of_empty_is_zero(self):
        self.assertEqual(len(ScrabbleWordRepresentation("")), 0)

    def test_len_of_non_empty_is_non_zero(self):
        self.assertEqual(len(ScrabbleWordRepresentation("abc")), 3)


suite = TestLoader().loadTestsFromTestCase(TestScrabbleWordRepresentation)
TextTestRunner(verbosity=2).run(suite)