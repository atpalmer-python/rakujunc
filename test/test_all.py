import rakujunc as junc


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
