import rakujunc as junc


def test_none_repr():
    assert repr(junc.none('hello', 'world')) == "none('hello', 'world')"


def test_none_str():
    assert str(junc.none('hello', 'world')) == "none('hello', 'world')"


def test_none_eq_none():
    assert junc.none(1,2) == junc.none(1,2)


def test_none_ne_none():
    assert junc.none(1,2) != junc.none(3,4)


def test_none_eq_any():
    assert junc.none(1,2) == junc.any(3,4)


def test_none_ne_any():
    assert junc.none(1,2) != junc.any(1,2)


def test_none_eq_all():
    assert junc.none(1,2) == junc.all(3,4)


def test_none_ne_all():
    assert junc.none(1) != junc.all(1)


def test_none_eq_one():
    assert junc.none(1,2) == junc.one(3,4,5)


def test_none_ne_one():
    assert junc.none(1,2) != junc.one(1,3)

