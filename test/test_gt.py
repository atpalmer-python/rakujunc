import p6junc as junc


def test_all_gt_all():
    assert junc.all(1,2,3) > junc.all(-1,-2,-3)


def test_all_gt_any():
    assert junc.all(1,2,3) > junc.any(-1,4,5)


def test_any_gt_all():
    assert junc.any(-1,-2,4) > junc.all(1,2,3)


def test_all_lt_any():
    assert junc.all(1,2,3) < junc.any(-1,-2,4)
