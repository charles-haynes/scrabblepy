__author__ = 'chaynes'

class ScrabbleWordRepresentation():
    def __init__(self, iterable):
        self.iterable = sorted(iterable)

    def __sub__(self, other):
        return ScrabbleWordRepresentation(self.sub(other))

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

    def __len__(self):
        return sum(1 for _ in self.iterable)

    def __eq__(self, other):
        return self.iterable == other.iterable

    def __hash__(self):
        try:
            return self._hash
        except AttributeError:
            self._hash = hash(tuple(self.iterable))
            return self._hash
