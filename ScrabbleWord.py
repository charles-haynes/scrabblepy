__author__ = 'chaynes'


class ScrabbleWord():
    def __init__(self, iterable):
        self.iterable = iterable

    @classmethod
    def FromWord(cls, word):
        return cls(sorted(word))

    def contains(self, other):
        return not any(other._sub(self))

    def _sub(self, other):
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

