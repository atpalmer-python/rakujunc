import p6junc as junc


def test_any123_eq_any345():
    assert junc.any(1,2,3) == junc.any(3,4,5)


def test_all1_eq_all12():
    assert (junc.all(1) == junc.all(1,2)) == False


def test_any12_eq_all12():
    assert junc.any(1,2) == junc.all(1,2)


def test_all12_eq_any12():
    assert junc.all(1,2) == junc.any(1,2)
