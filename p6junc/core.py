from collections import OrderedDict


def find_precedence(a, b):
    for cls in (any, one, all):
        if isinstance(a, cls):
            return (a, b)
        if isinstance(b, cls):
            return (b, a)
    assert False, 'Should not arrive here'


class _Junction(object):
    def __init__(self, *items):
        self._items = items

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return self.bool.__name__ + str(self._items)

    def __bool__(self):
        return self.bool(self)

    def __eq__(self, other):
        inner, outer = find_precedence(self, other)
        return outer.bool(inner.bool(a.__eq__(b) for a in inner) for b in outer)

    def __gt__(self, other):
        inner, outer = find_precedence(self, other)
        return outer.bool(inner.bool(a.__gt__(b) for a in inner) for b in outer)


class any(_Junction):
    bool = __builtins__['any']


class all(_Junction):
    bool = __builtins__['all']


class one(_Junction):
    @staticmethod
    def bool(iterable):
        count = 0
        for item in iterable:
            if item:
                count += 1
            if count > 1:
                return False
        return count == 1
