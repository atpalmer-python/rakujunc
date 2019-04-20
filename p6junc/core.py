

class _Junction(object):
    def __init__(self, *, to_bool, items):
        self._bool = to_bool
        self._items = items

    def __bool__(self):
        return self._bool(self._items)


def any(*items):
    return _Junction(items=items, to_bool=__builtins__['any'])


def all(*items):
    return _Junction(items=items, to_bool=__builtins__['all'])
