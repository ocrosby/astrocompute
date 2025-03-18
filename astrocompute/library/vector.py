import math
from typing import Tuple, Union, overload

Vector2D = Tuple[float, float]
Vector3D = Tuple[float, float, float]
Vector = Union[Vector2D, Vector3D]


def dimension(v: Vector) -> int:
    return len(v)


def are_same_dimension(u: Vector, v: Vector) -> bool:
    return dimension(u) == dimension(v)


@overload
def add(u: Vector2D, v: Vector2D) -> Vector2D:
    pass


@overload
def add(u: Vector3D, v: Vector3D) -> Vector3D:
    pass


def add(u: Vector, v: Vector) -> Vector:
    return tuple(ua + va for ua, va in zip(u, v))  # type: ignore


@overload
def scalar_multiply(s: float, v: Vector2D) -> Vector2D:
    pass


@overload
def scalar_multiply(s: float, v: Vector3D) -> Vector3D:
    pass


def scalar_multiply(s: float, v: Vector) -> Vector:
    return tuple(s * vi for vi in v)  # type: ignore


@overload
def dot_product(u: Vector2D, v: Vector2D) -> float:
    pass


@overload
def dot_product(u: Vector3D, v: Vector3D) -> float:
    pass


def dot_product(u: Vector, v: Vector) -> float:
    return sum(ua * va for ua, va in zip(u, v))


@overload
def norm(v: Vector2D) -> float:
    pass


@overload
def norm(v: Vector3D) -> float:
    pass


def norm(v: Vector) -> float:
    return math.sqrt(sum(vi**2 for vi in v))


@overload
def normalize(v: Vector2D) -> Vector2D:
    pass


@overload
def normalize(v: Vector3D) -> Vector3D:
    pass


def normalize(v: Vector) -> Vector:
    n = norm(v)

    if n == 0.0:
        raise ValueError("Cannot normalize the zero vector")

    return tuple(vi / n for vi in v)  # type: ignore


@overload
def are_orthogonal(u: Vector2D, v: Vector2D) -> bool:
    pass


@overload
def are_orthogonal(u: Vector3D, v: Vector3D) -> bool:
    pass


def are_orthogonal(u: Vector, v: Vector) -> bool:
    return dot_product(u, v) == 0.0


@overload
def are_parallel(u: Vector2D, v: Vector2D) -> bool:
    pass


@overload
def are_parallel(u: Vector3D, v: Vector3D) -> bool:
    pass


def are_parallel(u: Vector, v: Vector) -> bool:
    if not are_same_dimension(u, v):
        raise ValueError("Vectors must be of the same dimension")

    u_dimension = dimension(u)

    if u_dimension not in (2, 3):
        raise ValueError(f"Unsupported dimension: {u_dimension}")

    if u_dimension == 2:
        # Handle 2D vectors
        return u[0] * v[1] == u[1] * v[0]

    # Handle 3D vectors
    return (
        u[0] * v[1] == u[1] * v[0]
        and u[0] * v[2] == u[2] * v[0]
        and u[1] * v[2] == u[2] * v[1]
    )
