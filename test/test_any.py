import rakujunc as junc


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

