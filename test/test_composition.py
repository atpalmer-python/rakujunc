import rakujunc as junc


def test_comp_any_allTrue_allFalse():
    assert junc.any(junc.all(True), junc.all(False))


def test_comp_any_allTrue_anyTrueFalse():
    assert junc.any(junc.all(True), junc.any(True, False))


def test_comp_any_allTrueFalse_anyFalse():
    assert not junc.any(junc.all(True, False), junc.any(False))


def test_comp_all_allTrue_allTrue():
    assert junc.all(junc.all(True), junc.all(True))


def test_comp_all_allTrue_allFalse():
    assert not junc.all(junc.all(True), junc.all(False))

