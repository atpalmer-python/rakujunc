import p6junc as junc


# any


def test_any_FalseTrueFalse():
    assert bool(junc.any(False, True, False)) == True


def test_any_FalseFalse():
    assert bool(junc.any(False, False)) == False


def test_any_empty():
    assert bool(junc.any()) == False


def test_any_allTrue_allFalse():
    assert bool(junc.any(junc.all(True), junc.all(False))) == True


def test_any_allTrue_anyTrueFalse():
    assert bool(junc.any(junc.all(True), junc.any(True, False))) == True


def test_any_allTrueFalse_anyFalse():
    assert bool(junc.any(junc.all(True, False), junc.any(False))) == False


def test_any123_eq_any345():
    assert junc.any(1,2,3) == junc.any(3,4,5)


def test_all1_eq_all12():
    assert (junc.all(1) == junc.all(1,2)) == False


def test_any12_eq_all12():
    assert junc.any(1,2) == junc.all(1,2)


def test_any_gt_all():
    assert junc.any(-1,-2,4) > junc.all(1,2,3)


def test_any123_ne_any345():
    assert (junc.any(1,2,3) != junc.any(3,4,5)) == False


def test_any12_ne_all12():
    assert (junc.any(1,2) != junc.all(1,2)) == False


# all


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


def test_all12_eq_any12():
    assert junc.all(1,2) == junc.any(1,2)


def test_all_gt_all():
    assert junc.all(1,2,3) > junc.all(-1,-2,-3)


def test_all_gt_any():
    assert junc.all(1,2,3) > junc.any(-1,4,5)


def test_all_lt_any():
    assert junc.all(1,2,3) < junc.any(-1,-2,4)


def test_all1_ne_all12():
    assert (junc.all(1) != junc.all(1,2)) == True


def test_all12_ne_any12():
    assert (junc.all(1,2) != junc.any(1,2)) == False


# one


def test_one_TrueTrueFalse():
    assert bool(junc.one(True, True, False)) == False


def test_one_FalseTrueFalse():
    assert bool(junc.one(False, True, False)) == True


def test_one_FalseFalseFalse():
    assert bool(junc.one(False, False, False)) == False


def test_one12_eq_one12():
    assert (junc.one(1,2) == junc.one(1,2)) == False


def test_one12_eq_any12():
    assert (junc.one(1,2) == junc.any(1,2)) == False


def test_one12_eq_all12():
    assert junc.one(1,2) == junc.all(1,2)
