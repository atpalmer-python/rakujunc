

ANY = __builtins__['any']
ALL = __builtins__['all']


def ONE(iterable):
    itor = iter(iterable)
    return ANY(itor) and not ANY(itor)


def NONE(iterable):
    return ALL(not x for x in iterable)


def compose_inner(ljunc, rjunc, cmpname):
    return rjunc.__class__(*[ljunc.__class__(*[
            getattr(left, cmpname)(right) for left in ljunc
        ]) for right in rjunc])


def compose_outer(ljunc, rjunc, cmpname):
    return ljunc.__class__(*[rjunc.__class__(*[
            getattr(left, cmpname)(right) for right in rjunc
        ]) for left in ljunc])


def compose_single(junc, item, cmpname):
    return junc.__class__(*[
        getattr(left, cmpname)(item)
        for left in junc])


class Junction(object):
    def __init__(self, *items):
        self._items = items

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return self.__class__.__name__ + str(self._items)

    def _compose(self, other, cmpname):
        if isinstance(other, Junction):
            composer = self._get_composer(other)
            return composer(self, other, cmpname)
        return compose_single(self, other, cmpname)

    def __eq__(self, other):
        return self._compose(other, '__eq__')

    def __gt__(self, other):
        return self._compose(other, '__gt__')

    def __lt__(self, other):
        return self._compose(other, '__lt__')

    def __ge__(self, other):
        return self._compose(other, '__ge__')

    def __le__(self, other):
        return self._compose(other, '__le__')

    def __add__(self, other):
        return self._compose(other, '__add__')

    def __sub__(self, other):
        return self._compose(other, '__sub__')

    def __mul__(self, other):
        return self._compose(other, '__mul__')

    def __truediv__(self, other):
        return self._compose(other, '__truediv__')

    def __floordiv__(self, other):
        return self._compose(other, '__floordiv__')

    def __mod__(self, other):
        return self._compose(other, '__mod__')

    def __divmod__(self, other):
        return self._compose(other, '__divmod__')

    def __pos__(self):
        return self.__class__(*[i.__pos__() for i in self._items])

    def __neg__(self):
        return self.__class__(*[i.__neg__() for i in self._items])

    def __abs__(self):
        return self.__class__(*[i.__abs__() for i in self._items])

    def __round__(self):
        return self.__class__(*[round(i) for i in self._items])

    def __floor__(self):
        import math
        return self.__class__(*[math.floor(i) for i in self._items])

    def __ceil__(self):
        import math
        return self.__class__(*[math.ceil(i) for i in self._items])

    def __and__(self, other):
        return all(self, other)

    def __or__(self, other):
        return any(self, other)

    def __xor__(self, other):
        return one(self, other)


class any(Junction):
    def __bool__(self):
        return ANY(self)

    def _get_composer(self, other):
        if isinstance(other, one):
            return compose_outer
        return compose_inner


class all(Junction):
    def __bool__(self):
        return ALL(self)

    def _get_composer(self, other):
        return compose_outer


class one(Junction):
    def __bool__(self):
        return ONE(self)

    def _get_composer(self, other):
        if isinstance(other, any):
            return compose_outer
        return compose_inner


class none(Junction):
    def __bool__(self):
        return NONE(self)

    def _get_composer(self, other):
        return compose_outer
