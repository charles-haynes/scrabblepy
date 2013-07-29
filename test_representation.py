from unittest import TestCase
from scrabble import representation

__author__ = 'chaynes'


class TestRepresentation(TestCase):
    
    def test_representation_unordered(self):
        self.assertEqual(representation("spot"), representation("stop"))    

    def test_representation_keeps_repetition(self):
        self.assertNotEquals(representation("stops"), representation("stop"))
        
    def test_representation_difference(self):
        self.assertEquals(representation("stops")-representation("stop"), representation("s"))

    # def test_representation_intersection(self):
    #     self.assertEqual(representation("stops")&representation("stop"), representation("stop"))
