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


def test_mixed_int_bool():
    assert junc.all(1) == True
    assert junc.all(0) == False


def test_mixed_str_bool():
    with pytest.raises(NotImplementedError):
        assert junc.all('x') == True
    with pytest.raises(NotImplementedError):
        assert junc.all('') == False

