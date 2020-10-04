import rakujunc as junc


def test_one_repr():
    assert repr(junc.one('hello', 'world')) == "one('hello', 'world')"


def test_one_str():
    assert str(junc.one('hello', 'world')) == "one('hello', 'world')"


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

