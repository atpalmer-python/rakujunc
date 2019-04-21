import p6junc as junc


def test_any123_ne_any345():
    assert (junc.any(1,2,3) != junc.any(3,4,5)) == False


def test_all1_ne_all12():
    assert (junc.all(1) != junc.all(1,2)) == True


def test_any12_ne_all12():
    assert (junc.any(1,2) != junc.all(1,2)) == False


def test_all12_ne_any12():
    assert (junc.all(1,2) != junc.any(1,2)) == False
