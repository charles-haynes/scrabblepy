__author__ = 'chaynes'


class ScrabbleWord():
    def __init__(self, iterable, blanks=0):
        self.iterable = iterable
        self.blanks = blanks

    @classmethod
    def FromWord(cls, word, blanks=0):
        return cls(sorted(word), blanks)

    def contains(self, other):
        blanks = self.blanks
        for _ in other.sub(self):
            blanks -= 1
            if blanks < 0:
                return False
        return True

    def __sub__(self, other):
        return ScrabbleWord(self.sub(other))

    def sub(self, other):
        si = iter(self.iterable)
        s = si.next()
        for o in other.iterable:
            while s < o:
                yield s
                s = si.next()
            if s == o:
                s = si.next()
        while True:
            yield s
            s = si.next()

    def __eq__(self, other):
        return all(x == y for (x, y) in zip(self.iterable, other.iterable))

