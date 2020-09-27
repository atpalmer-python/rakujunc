

class _Junction(object):
    def __init__(self, *items):
        self._items = items

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return self.__class__.__name__ + str(self._items)

    def __bool__(self):
        return self.__class__.bool(self)

    def _compare(self, other, cmpname):
        if isinstance(other, str) or not hasattr(other, '__iter__'):
            other = [other]
        inner, outer = self._precedence(other)
        swap = inner is not self
        outer_list = []
        for o in outer:
            inner_list = []
            for i in inner:
                left, right = (o, i) if swap else (i, o)
                result = getattr(left, cmpname)(right)
                inner_list.append(result)
            outer_list.append(inner.__class__(*inner_list))
        return outer.__class__(*outer_list)

    def __eq__(self, other):
        return self._compare(other, '__eq__')

    def __gt__(self, other):
        return self._compare(other, '__gt__')


class any(_Junction):
    bool = __builtins__['any']

    def _precedence(self, other):
        if isinstance(other, one):
            return (other, self)
        return (self, other)


class all(_Junction):
    bool = __builtins__['all']

    def _precedence(self, other):
        return (other, self)


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

    def _precedence(self, other):
        if isinstance(other, any):
            return (other, self)
        return (self, other)
