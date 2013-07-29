from unittest import TestCase, TestLoader, TextTestRunner
import score

__author__ = 'chaynes'


class TestScore(TestCase):
    def test_score(self):
        self.assertEqual(score.score("abcdefghijklmnopqrstuvwxyz"), 137)

    def test_parenthesized_blank(self):
        self.assertEqual(score.score("a(a)a"), 2)

    def test_capitalized_blank(self):
        self.assertEqual(score.score("aAa"), 2)

    def test_mixed_blanks(self):
        self.assertEqual(score.score("aAa(a)a"), 3)

    def test_multiple_blanks(self):
        self.assertEqual(score.score("AAa(aa)a(a)(a)aA(a)a(a)AaA(a)Aa(a)A(a)"), 56)

    def test_bingo(self):
        self.assertEqual(score.score("aaaAaaa"), 56)

    def test_non_bingo_with_blanks(self):
        self.assertEqual(score.score("a(a)aaaa"), 5)


suite = TestLoader().loadTestsFromTestCase(TestScore)
TextTestRunner(verbosity=2).run(suite)