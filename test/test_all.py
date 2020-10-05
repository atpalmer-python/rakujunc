import pytest
import rakujunc as junc


def test_all_mixed_int_bool():
    assert junc.all(1) == True
    assert junc.all(0) == False


def test_all_mixed_str_bool():
    with pytest.raises(NotImplementedError):
        assert junc.all('x') == True
    with pytest.raises(NotImplementedError):
        assert junc.all('') == False


def test_all_repr():
    assert repr(junc.all('hello', 'world')) == "all('hello', 'world')"


def test_all_str():
    assert str(junc.all('hello', 'world')) == "all('hello', 'world')"


def test_all_empty():
    assert junc.all()


def test_all_True():
    assert junc.all(True, True)


def test_all_False():
    assert not junc.all(True, True, False)


def test_all_eq_all():
    assert junc.all(1,1) == junc.all(1,1)


def test_all_ne_all():
    assert junc.all(1,1) != junc.all(1,2)


def test_all_eq_any():
    assert junc.all(1,2) == junc.any(1,2)


def test_all_ne_any():
    assert junc.all(1,2) != junc.any(1,3)


def test_all_eq_one():
    assert junc.all(1,2) == junc.one(1,2)


def test_all_ne_one():
    assert junc.all(1,2) != junc.one(1,3)


def test_all_eq_none():
    assert junc.all(1,3,5,7,9) == junc.none(2,4,6,8,10)


def test_all_eq_none():
    assert junc.all(1,3,5,7,9) != junc.none(1,2,3)

