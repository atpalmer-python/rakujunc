import p6junc as junc


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


def test_any_mul():
    target = junc.any(1,2,3) * 10
    assert target == 20
    assert target == 30
    assert target == 10


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
