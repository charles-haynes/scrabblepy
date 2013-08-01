__author__ = 'chaynes'
from ScrabbleWord import ScrabbleWord


class ScrabbleRack(ScrabbleWord):
    def __init__(self, iterable, blanks):
        ScrabbleWord.__init__(self, iterable)
        self.blanks = blanks

    @classmethod
    def RackFromWord(cls, word, blanks):
        return cls(sorted(word), blanks)

    def contains(self, other):
        blanks = self.blanks
        for _ in other._sub(self):
            blanks -= 1
            if blanks < 0:
                return False
        return True
