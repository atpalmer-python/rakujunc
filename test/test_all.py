import pytest
import rakujunc as junc


def test_int():
    assert junc.all(42) == 42
    assert junc.all(42) != 0


def test_float():
    assert junc.all(4.2) == 4.2
    assert junc.all(4.2) != 0.0


def test_str():
    assert junc.all('hello') == 'hello'
    assert junc.all('hello') != 'world'


def test_bool():
    assert junc.all(False) == False
    assert junc.all(False) != True


def test_None():
    assert junc.all(None) == None
    with pytest.raises(NotImplementedError):
        junc.all(None) == 'something'


def test_tuple():
    assert junc.all((1,'a')) == (1,'a')
    assert junc.all((1,'a')) != ('a',1)


def test_list():
    assert junc.all([1,'a']) == [1,'a']
    assert junc.all([1,'a']) != ['a',1]


def test_dict():
    assert junc.all({'a': 1}) == {'a': 1}
    assert junc.all({'a': 1}) != {1: 'a'}


def test_set():
    assert junc.all({'a'}) == {'a'}
    assert junc.all({'a'}) != {'b'}


def test_class():
    class Fake(object):
        def __init__(self, value):
            self.value = value
        def __eq__(self, other):
            return self.value == other.value
    x1 = Fake('a')
    x2 = Fake('a')
    x3 = Fake('b')
    assert junc.all(x1) == x2
    assert junc.all(x2) != x3


# transitivity


def test_transitivity_all_v_int():
    assert junc.all(42) == 42
    assert junc.all(42) != 0


def test_transitivity_int_v_all():
    assert 42 == junc.all(42)
    assert 0 != junc.all(42)



# composition


def test_comp_any_allTrue_allFalse():
    assert bool(junc.any(junc.all(True), junc.all(False))) == True


def test_comp_any_allTrue_anyTrueFalse():
    assert bool(junc.any(junc.all(True), junc.any(True, False))) == True


def test_comp_any_allTrueFalse_anyFalse():
    assert bool(junc.any(junc.all(True, False), junc.any(False))) == False


def test_comp_all_allTrue_allTrue():
    assert bool(junc.all(junc.all(True), junc.all(True))) == True


def test_comp_all_allTrue_allFalse():
    assert bool(junc.all(junc.all(True), junc.all(False))) == False


# junc vs. single


def test_single_all_gt():
    assert junc.all(1,2,3) > 0


def test_single_any_eq():
    assert junc.any(1,2,3,3,3) == 3


def test_single_one_gt():
    assert junc.one(1,2,3) > 2


def test_single_nlt():
    assert not (7 < junc.any(1,2,3))


def test_all_add():
    target = junc.all(1,2,3) + 1
    assert target >= 1
    assert target <= 4


def test_all_sub():
    target = junc.all(1,2,3) - 1
    assert -1 < target < 3


def test_any_mul():
    target = junc.any(1,2,3) * 10
    assert target == 20
    assert target == 30
    assert target == 10


def test_any_truediv():
    target = junc.any(1,2,3) / 2
    assert target == 0.5
    assert target == 1
    assert target == 1.5


def test_any_floordiv():
    target = junc.any(5,6,7) // 2
    assert 1 != target
    assert 2 == target
    assert 3 == target
    assert 4 != target


def test_any_mod():
    target = junc.any(5,6,7) % 3
    assert target == junc.all(0,1,2)
    assert target == junc.none(-1,3)


def test_any_divmod():
    target = divmod(junc.any(5,6,7), 3)
    assert target != (1,1)
    assert target == (1,2)
    assert target == (2,0)
    assert target == (2,1)
    assert target != (2,2)


def test_any_pow():
    target = junc.any(1,2,3) ** 2
    assert target == 1
    assert target == 4
    assert target == 9
    assert target != 10


def test_any_lshift():
    target = junc.any(0x1,0x2,0x3) << 1
    assert target == 0x2
    assert target == 0x4
    assert target == 0x6
    assert target != 0x7


def test_any_rshift():
    target = junc.any(0x2,0x4,0x6) >> 1
    assert target == 0x1
    assert target == 0x2
    assert target == 0x3
    assert target != 0x4


def test_any_inverse():
    target = ~junc.any(1)
    assert target == -2
    assert target != 1


def test_any_and():
    assert junc.any(1,2,3) & 4 == junc.any(1, 4)


def test_any_or():
    assert junc.any(1,2,3) | 4 == junc.all(1, 4)


def test_any_xor():
    assert junc.all(True) ^ False


def test_any_neg():
    assert -junc.any(1,2,3) == -2


def test_any_pos():
    assert +junc.any(1,2,3) == +2


def test_any_abs():
    assert abs(junc.any(1,-2,3)) == +2


def test_any_round():
    target = round(junc.any(1.6,3.3,5.7))
    assert target != 1
    assert target == 2
    assert target == 3
    assert target != 4
    assert target != 5
    assert target == 6


def test_any_floor():
    import math
    target = math.floor(junc.any(1.6,3.3,5.7))
    assert target == 1
    assert target != 2
    assert target == 3
    assert target != 4
    assert target == 5
    assert target != 6


def test_any_ceil():
    import math
    target = math.ceil(junc.any(1.6,3.3,5.7))
    assert target != 1
    assert target == 2
    assert target != 3
    assert target == 4
    assert target != 5
    assert target == 6


def test_any_trunc():
    import math
    target = math.trunc(junc.any(1.6,3.3,5.7))
    assert target == 1
    assert target != 2
    assert target == 3
    assert target != 4
    assert target == 5
    assert target != 6


# any


def test_any_FalseTrueFalse():
    assert junc.any(False, True, False)


def test_any_FalseFalse():
    assert not junc.any(False, False)


def test_any_empty():
    assert not junc.any()


## any v. any

def test_any123_eq_any345():
    assert junc.any(1,2,3) == junc.any(3,4,5)


def test_any123_ne_any345():
    assert not (junc.any(1,2,3) != junc.any(3,4,5))


## any v. all

def test_any12_eq_all12():
    assert junc.any(1,2) == junc.all(1,2)


def test_any12_ne_all12():
    assert not (junc.any(1,2) != junc.all(1,2))


def test_any_gt_all():
    assert junc.any(-1,-2,4) > junc.all(1,2,3)


## any v. none

def test_any_ne_none():
    assert junc.any(1,2) != junc.none(1,2)


def test_any_gt_none():
    assert junc.any(1,2,10) > junc.none(11,12,13)


# all


def test_all_TrueTrue():
    assert junc.all(True, True)


def test_all_TrueTrueFalse():
    assert not junc.all(True, True, False)


def test_all_empty():
    assert junc.all()


## all v. all

def test_all1_ne_all12():
    assert junc.all(1) != junc.all(1,2)


def test_all_gt_all():
    assert junc.all(1,2,3) > junc.all(-1,-2,-3)


## all v. any

def test_all12_eq_any12():
    assert junc.all(1,2) == junc.any(1,2)


def test_all_gt_any():
    assert junc.all(1,2,3) > junc.any(-1,4,5)


def test_all_lt_any():
    assert junc.all(1,2,3) < junc.any(-1,-2,4)


def test_all12_ne_any12():
    assert not (junc.all(1,2) != junc.any(1,2))


## all v. none

def test_all_eq_none():
    assert junc.all(1,3,5,7,9) == junc.none(2,4,6,8,10)


def test_all_lt_none():
    assert junc.all(11,12,13) < junc.none(9,8,7)


# one


def test_one_TrueTrueFalse():
    assert not junc.one(True, True, False)


def test_one_FalseTrueFalse():
    assert bool(junc.one(False, True, False)) == True


def test_one_FalseFalseFalse():
    assert bool(junc.one(False, False, False)) == False


## one v. one

def test_one12_ne_one12():
    assert junc.one(1,2) != junc.one(1,2)


## one v. any

def test_one12_ne_any12():
    assert junc.one(1,2) != junc.any(1,2)


## one v. all

def test_one12_eq_all12():
    assert junc.one(1,2) == junc.all(1,2)


## one v. none

def test_one_eq_none():
    assert junc.one(1,2) != junc.none(1,2)


def test_one_gt_none():
    assert junc.one(1,2) > junc.none(5,6,7)


# none


## none v. none

def test_none_gt_none():
    junc.none(1, 2) > junc.all(5, 6)


## none v. any

def test_none_eq_any():
    junc.none(1,2) == junc.any(5,6)


def test_none_gt_any():
    junc.none(1,2) > junc.any(5,6)


## none v. all

def test_none_gt_all():
    junc.none(1,2) > junc.all(5,6)


def test_none_gt_one():
    junc.none(1,2) > junc.all(5,6)
