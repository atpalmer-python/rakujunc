import rakujunc as junc


def test_none_repr():
    assert repr(junc.none('hello', 'world')) == "none('hello', 'world')"


def test_none_str():
    assert str(junc.none('hello', 'world')) == "none('hello', 'world')"


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


## none v. one

def test_none_eq_one():
    assert junc.none(1,2) == junc.one(3,4,5)


def test_none_ne_one():
    assert junc.none(1,2) != junc.one(1,3)

