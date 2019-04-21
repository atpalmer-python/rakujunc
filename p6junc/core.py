from collections import OrderedDict


BOOL_CONVERTERS_BY_PRECEDENCE = OrderedDict([
    ('any', __builtins__['any']),
    ('all', __builtins__['all']),
])


def find_precedence(a, b):
    for func in BOOL_CONVERTERS_BY_PRECEDENCE.values():
        if a._bool is func:
            return (a, b)
        if b._bool is func:
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


def any(*items):
    return _Junction(items=items, to_bool=BOOL_CONVERTERS_BY_PRECEDENCE['any'])


def all(*items):
    return _Junction(items=items, to_bool=BOOL_CONVERTERS_BY_PRECEDENCE['all'])
