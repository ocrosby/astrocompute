import pytest

from astrocompute.library.apc_math import frac, modulo, ddd, dms


@pytest.mark.parametrize(
    "input, expected",
    [(5.75, 0.75), (-5.75, -0.75), (0, 0), (1.0, 0.0), (-1.0, -0.0)],
)
def test_frac(input, expected):
    assert frac(input) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (5.75, 2, 1.75),
        (-5.75, 2, 0.25),
        (5.75, -2, -0.25),
        (-5.75, -2, -1.75),
        (0, 2, 0),
        (5.75, 1, 0.75),
        (5.75, 5.75, 0.0),
    ],
)
def test_modulo(x, y, expected):
    assert modulo(x, y) == expected


@pytest.mark.parametrize("x, y", [(5.75, 0)])
def test_modulo_zero_division(x, y):
    with pytest.raises(ZeroDivisionError):
        modulo(x, y)

@pytest.mark.parametrize(
    "d, m, s, expected",
    [
        (15, 30, 0.0, 15.50000),
        (-8, 9, 10.0, -8.15278),
        (0, 1, 0.0, 0.01667),
        (0,-5,0.0,-0.08334)
    ]
)
def test_ddd(d, m, s, expected):
    assert ddd(d, m, s) == pytest.approx(expected, abs=1e-5)

@pytest.mark.parametrize(
    "dd, expected",
    [
        (15.5, (15, 30, 0.0)),
        (-8.15278, (-8, 9, 10.0)),
        (0.01667, (0, 1, 0.0)),
        (-0.08334, (0, -5, 0.0)),
        (-0.00333, (0, 0, -12.0))
    ]
)
def test_dms(dd, expected):
    """
    This test case is used to test the dms function
    It takes a decimal degree and returns a tuple of degrees, minutes, and seconds
    :param dd:
    :param expected:
    :return:
    """
    result = dms(dd)
    assert result[0] == expected[0]
    assert result[1] == expected[1]
    assert result[2] == pytest.approx(expected[2], abs=1e-1)
