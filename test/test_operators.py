import rakujunc as junc


def test_single_all_gt():
    assert junc.all(1,2,3) > 0


def test_single_any_eq():
    assert junc.any(1,2,3,3,3) == 3


def test_single_one_gt():
    assert junc.one(1,2,3) > 2


def test_single_nlt():
    assert not (7 < junc.any(1,2,3))


def test_all_add():
    target = junc.all(1,2,3) + 1
    assert target >= 1
    assert target <= 4


def test_all_sub():
    target = junc.all(1,2,3) - 1
    assert -1 < target < 3


def test_any_mul():
    target = junc.any(1,2,3) * 10
    assert target == 20
    assert target == 30
    assert target == 10


def test_any_truediv():
    target = junc.any(1,2,3) / 2
    assert target == 0.5
    assert target == 1
    assert target == 1.5


def test_any_floordiv():
    target = junc.any(5,6,7) // 2
    assert 1 != target
    assert 2 == target
    assert 3 == target
    assert 4 != target


def test_any_mod():
    target = junc.any(5,6,7) % 3
    assert target == junc.all(0,1,2)
    assert target == junc.none(-1,3)


def test_any_divmod():
    target = divmod(junc.any(5,6,7), 3)
    assert target != (1,1)
    assert target == (1,2)
    assert target == (2,0)
    assert target == (2,1)
    assert target != (2,2)


def test_any_pow():
    target = junc.any(1,2,3) ** 2
    assert target == 1
    assert target == 4
    assert target == 9
    assert target != 10


def test_any_lshift():
    target = junc.any(0x1,0x2,0x3) << 1
    assert target == 0x2
    assert target == 0x4
    assert target == 0x6
    assert target != 0x7


def test_any_rshift():
    target = junc.any(0x2,0x4,0x6) >> 1
    assert target == 0x1
    assert target == 0x2
    assert target == 0x3
    assert target != 0x4


def test_any_inverse():
    target = ~junc.any(1)
    assert target == -2
    assert target != 1


def test_any_and():
    assert junc.any(1,2,3) & 4 == junc.any(1, 4)


def test_any_or():
    assert junc.any(1,2,3) | 4 == junc.all(1, 4)


def test_any_xor():
    assert junc.all(True) ^ False


def test_any_neg():
    assert -junc.any(1,2,3) == -2


def test_any_pos():
    assert +junc.any(1,2,3) == +2


def test_any_abs():
    assert abs(junc.any(1,-2,3)) == +2


def test_any_round():
    target = round(junc.any(1.6,3.3,5.7))
    assert target != 1
    assert target == 2
    assert target == 3
    assert target != 4
    assert target != 5
    assert target == 6


def test_any_floor():
    import math
    target = math.floor(junc.any(1.6,3.3,5.7))
    assert target == 1
    assert target != 2
    assert target == 3
    assert target != 4
    assert target == 5
    assert target != 6


def test_any_ceil():
    import math
    target = math.ceil(junc.any(1.6,3.3,5.7))
    assert target != 1
    assert target == 2
    assert target != 3
    assert target == 4
    assert target != 5
    assert target == 6


def test_any_trunc():
    import math
    target = math.trunc(junc.any(1.6,3.3,5.7))
    assert target == 1
    assert target != 2
    assert target == 3
    assert target != 4
    assert target == 5
    assert target != 6


def test_transitivity_all_v_int():
    assert junc.all(42) == 42
    assert junc.all(42) != 0


def test_transitivity_int_v_all():
    assert 42 == junc.all(42)
    assert 0 != junc.all(42)

