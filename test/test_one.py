import rakujunc as junc


def test_one_repr():
    assert repr(junc.one('hello', 'world')) == "one('hello', 'world')"


def test_one_str():
    assert str(junc.one('hello', 'world')) == "one('hello', 'world')"


def test_one_empty():
    assert not junc.one()


def test_one_True():
    assert junc.one(False, True, False)


def test_one_False():
    assert not junc.one(True, True, True)


def test_one_eq_one():
    assert junc.one(1,2) == junc.one(1,3)


def test_one_ne_one():
    assert junc.one(1,2) != junc.one(1,2)


def test_one_eq_any():
    assert junc.one(1,2) == junc.any(1,3)


def test_one_ne_any():
    assert junc.one(1,2) != junc.any(1,2)


def test_one_eq_all():
    assert junc.one(1,2) == junc.all(1,2)


def test_one_ne_all():
    assert junc.one(1,2) != junc.all(1,3)


def test_one_eq_none():
    assert junc.one(1,2) == junc.none(3)


def test_one_ne_none():
    assert junc.one(1,2) != junc.none(1,2)

