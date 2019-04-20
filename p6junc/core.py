

class _Junction(object):
    def __init__(self, *, to_bool, items):
        self._bool = to_bool
        self._items = items

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return self._bool.__name__ + str(self._items)

    def __bool__(self):
        return self._bool(self._items)

    def __eq__(self, other):
        return self._bool(other._bool(a.__eq__(b) for b in other) for a in self)


def any(*items):
    return _Junction(items=items, to_bool=__builtins__['any'])


def all(*items):
    return _Junction(items=items, to_bool=__builtins__['all'])
