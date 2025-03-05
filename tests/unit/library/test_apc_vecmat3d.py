import pytest
from astrocompute.library.apc_vecmat3d import Vec3D

@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        (Vec3D(1, 2, 3), Vec3D(4, 5, 6), Vec3D(5, 7, 9)),
        (Vec3D(-1, -2, -3), Vec3D(1, 2, 3), Vec3D(0, 0, 0)),
        (Vec3D(0, 0, 0), Vec3D(0, 0, 0), Vec3D(0, 0, 0)),
    ]
)
def test_vec3d_add(v1, v2, expected):
    assert v1 + v2 == expected

@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        (Vec3D(1, 2, 3), Vec3D(4, 5, 6), Vec3D(-3, -3, -3)),
        (Vec3D(-1, -2, -3), Vec3D(1, 2, 3), Vec3D(-2, -4, -6)),
        (Vec3D(0, 0, 0), Vec3D(0, 0, 0), Vec3D(0, 0, 0)),
    ]
)
def test_vec3d_sub(v1, v2, expected):
    assert v1 - v2 == expected

@pytest.mark.parametrize(
    "v, scalar, expected",
    [
        (Vec3D(1, 2, 3), 2, Vec3D(2, 4, 6)),
        (Vec3D(-1, -2, -3), -1, Vec3D(1, 2, 3)),
        (Vec3D(0, 0, 0), 5, Vec3D(0, 0, 0)),
    ]
)
def test_vec3d_mul(v, scalar, expected):
    assert v * scalar == expected

@pytest.mark.parametrize(
    "v, scalar, expected",
    [
        (Vec3D(2, 4, 6), 2, Vec3D(1, 2, 3)),
        (Vec3D(-1, -2, -3), -1, Vec3D(1, 2, 3)),
        (Vec3D(0, 0, 0), 5, Vec3D(0, 0, 0)),
    ]
)
def test_vec3d_truediv(v, scalar, expected):
    assert v / scalar == expected

def test_vec3d_truediv_zero_division():
    with pytest.raises(ZeroDivisionError):
        Vec3D(1, 2, 3) / 0

@pytest.mark.parametrize(
    "v, expected",
    [
        (Vec3D(1, 2, 2), 3),
        (Vec3D(0, 0, 0), 0),
        (Vec3D(-1, -2, -2), 3),
    ]
)
def test_vec3d_norm(v, expected):
    assert v.norm() == pytest.approx(expected)

@pytest.mark.parametrize(
    "v, expected",
    [
        (Vec3D(1, 2, 2), Vec3D(1/3, 2/3, 2/3)),
        (Vec3D(0, 0, 0), Vec3D(0, 0, 0)),
        (Vec3D(-1, -2, -2), Vec3D(-1/3, -2/3, -2/3)),
    ]
)
def test_vec3d_normalize(v, expected):
    if v.norm() == 0:
        with pytest.raises(ZeroDivisionError):
            v.normalize()
    else:
        assert v.normalize() == expected

def test_vec3d_str():
    v = Vec3D(1, 2, 3)
    assert str(v) == "(1, 2, 3)"