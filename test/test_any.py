import rakujunc as junc


def test_any_repr():
    assert repr(junc.any('hello', 'world')) == "any('hello', 'world')"


def test_any_str():
    assert str(junc.any('hello', 'world')) == "any('hello', 'world')"


def test_any_empty():
    assert not junc.any()


def test_any_True():
    assert junc.any(False, True, False)


def test_any_False():
    assert not junc.any(False, False)


def test_any_eq_any():
    assert junc.any(1,2) == junc.any(2,4)


def test_any_ne_any():
    assert junc.any(1,2) != junc.any(3,4)


def test_any_eq_all():
    assert junc.any(1,2) == junc.all(1,2)


def test_any_ne_all():
    assert junc.any(1,2) != junc.all(1,3)


def test_any_eq_one():
    assert junc.any(1,2) == junc.one(1,3)


def test_any_ne_one():
    assert junc.any(1,2) != junc.one(3,4)


def test_any_eq_none():
    assert junc.any(1,2) == junc.none(3,4)


def test_any_ne_none():
    assert junc.any(1,2) != junc.none(1,3)

