

ANY = __builtins__['any']
ALL = __builtins__['all']


def ONE(iterable):
    itor = iter(iterable)
    return ANY(itor) and not ANY(itor)


def NONE(iterable):
    return ALL(not x for x in iterable)


def compare_inner(ljunc, rjunc, cmpname):
    return rjunc.__class__(*[ljunc.__class__(*[
            getattr(left, cmpname)(right) for left in ljunc
        ]) for right in rjunc])


def compare_outer(ljunc, rjunc, cmpname):
    return ljunc.__class__(*[rjunc.__class__(*[
            getattr(left, cmpname)(right) for right in rjunc
        ]) for left in ljunc])


class _Junction(object):
    def __init__(self, *items):
        self._items = items

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return self.__class__.__name__ + str(self._items)

    def _compare(self, other, cmpname):
        if isinstance(other, str) or not hasattr(other, '__iter__'):
            other = [other]
        comparer = self._get_comparer(other)
        return comparer(self, other, cmpname)

    def __eq__(self, other):
        return self._compare(other, '__eq__')

    def __gt__(self, other):
        return self._compare(other, '__gt__')


class any(_Junction):
    def __bool__(self):
        return ANY(self)

    def _get_comparer(self, other):
        if isinstance(other, one):
            return compare_outer
        return compare_inner


class all(_Junction):
    def __bool__(self):
        return ALL(self)

    def _get_comparer(self, other):
        return compare_outer


class one(_Junction):
    def __bool__(self):
        return ONE(self)

    def _get_comparer(self, other):
        if isinstance(other, any):
            return compare_outer
        return compare_inner


class none(_Junction):
    def __bool__(self):
        return NONE(self)

    def _get_comparer(self, other):
        return compare_outer
