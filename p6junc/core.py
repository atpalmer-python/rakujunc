from collections import OrderedDict


def _one(iterable):
    count = 0
    for item in iterable:
        if item:
            count += 1
        if count > 1:
            return False
    return count == 1


def find_precedence(a, b):
    for cls in (_Any, _One, _All):
        if isinstance(a, cls):
            return (a, b)
        if isinstance(b, cls):
            return (b, a)
    assert False, 'Should not arrive here'


class _Junction(object):
    def __init__(self, *, to_bool, items):
        self._bool = to_bool
        self._items = items

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return self._bool.__name__ + str(self._items)

    def __bool__(self):
        return self._bool(self)

    def __eq__(self, other):
        inner, outer = find_precedence(self, other)
        return outer._bool(inner._bool(a.__eq__(b) for a in inner) for b in outer)

    def __gt__(self, other):
        inner, outer = find_precedence(self, other)
        return outer._bool(inner._bool(a.__gt__(b) for a in inner) for b in outer)


class _Any(_Junction):
    pass


class _All(_Junction):
    pass


class _One(_Junction):
    pass


def any(*items):
    return _Any(items=items, to_bool=__builtins__['any'])


def all(*items):
    return _All(items=items, to_bool=__builtins__['all'])


def one(*items):
    return _One(items=items, to_bool=_one)
