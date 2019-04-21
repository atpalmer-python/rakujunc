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


def test_all_allTrue_allTrue():
    assert bool(junc.all(junc.all(True), junc.all(True))) == True


def test_all_allTrue_allFalse():
    assert bool(junc.all(junc.all(True), junc.all(False))) == False


def test_any_allTrue_allFalse():
    assert bool(junc.any(junc.all(True), junc.all(False))) == True


def test_any_allTrue_anyTrueFalse():
    assert bool(junc.any(junc.all(True), junc.any(True, False))) == True


def test_any_allTrueFalse_anyFalse():
    assert bool(junc.any(junc.all(True, False), junc.any(False))) == False


def test_one_TrueTrueFalse():
    assert bool(junc.one(True, True, False)) == False


def test_one_FalseTrueFalse():
    assert bool(junc.one(False, True, False)) == True


def test_one_FalseFalseFalse():
    assert bool(junc.one(False, False, False)) == False
