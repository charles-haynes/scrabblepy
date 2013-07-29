from unittest import TestCase
from scrabble import convert, representation

__author__ = 'chaynes'


class TestConvert(TestCase):
    def test_convert(self):
        word_iterable = ["spot\n", "pots\r", "stop\n\r", "tops", "stops\r\n", "spots", "pot"]
        word_list = {representation("spot"): ["spot", "pots", "stop", "tops"],
                     representation("stops"): ["stops", "spots"],
                     representation("pot"): ["pot"]}
        self.assertEqual(convert(word_iterable), word_list)