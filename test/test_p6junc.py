import p6junc as junc


def test_any_FalseTrueFalse():
    assert bool(junc.any(False, True, False)) == True


def test_any_FalseFalse():
    assert bool(junc.any(False, False)) == False


def test_any_empty():
    assert bool(junc.any()) == False


def test_all_TrueTrue():
    assert bool(junc.all(True, True)) == True


def test_all_TrueTrueFalse():
    assert bool(junc.all(True, True, False)) == False


def test_all_empty():
    assert bool(junc.all()) == True
