import rakujunc as junc


def test_transitivity_all_v_int():
    assert junc.all(42) == 42
    assert junc.all(42) != 0


def test_transitivity_int_v_all():
    assert 42 == junc.all(42)
    assert 0 != junc.all(42)

