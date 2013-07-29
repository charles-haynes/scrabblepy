__author__ = 'chaynes'

from array import array


class ScrabbleWordRepresentation():
    def __init__(self, array):
        self.ary = array

    @classmethod
    def fromString(cls, source):
        """
        create a ScrabbleWordRepresentation from a string

        :type source: str
        :param source: source string
        :rtype: ScrabbleWordRepresentation
        :return: the scrabble word representation for that string
        """
        ary = array('B', [0] * 26)
        for c in source:
            try:
                ary[ord(c) - ord('a')] += 1
            except IndexError:
                pass
        return cls(ary)

    def __sub__(self, other):
        ary = array('B', [0] * 26)
        for i in range(0, 25):
            ary[i] = self.ary[i] - other.ary[i] if self.ary[i] > other.ary[i] else 0
        return ScrabbleWordRepresentation(ary)

    def __eq__(self, other):
        return self.ary == other.ary

        # si = iter(self.iter)
        # s = si.next()
        # for o in other.iter:
        #     while s < o:
        #         yield s
        #         s = si.next()
        #     if s == o:
        #         s = si.next()
        # while True:
        #     yield s
        #     s = si.next()

    def __len__(self):
        return sum((x > 0) for x in self.ary)