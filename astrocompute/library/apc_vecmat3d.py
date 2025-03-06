from astrocompute.models.vec3d import Vec3D


def add(v1: Vec3D, v2: Vec3D) -> Vec3D:
    """
    Adds two 3 dimensional vectors.

    :param v1: First vector
    :param v2: Second vector
    :return: Sum of the two vectors
    """
    return v1 + v2


def scalar_multiply_vec3d(scalar: float, vec3: Vec3D) -> Vec3D:
    """
    Multiplies a 3 dimensional vector by a scalar.

    :param scalar: Scalar value
    :param vec3: 3 dimensional vector
    :return: Result of the scalar multiplication
    """
    return Vec3D(vec3.x * scalar, vec3.y * scalar, vec3.z * scalar)


def dot_product(v1: Vec3D, v2: Vec3D) -> float:
    """
    Calculates the dot product of two 3 dimensional vectors.

    :param v1: First vector
    :param v2: Second vector
    :return: Dot product of the two vectors
    """
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def cross_product(v1: Vec3D, v2: Vec3D) -> Vec3D:
    """
    Calculates the cross product of two 3 dimensional vectors.
    :param v1: First vector
    :param v2: Second vector
    :return: Cross product of the two vectors
    """
    return Vec3D(
        v1.y * v2.z - v1.z * v2.y,
        v1.z * v2.x - v1.x * v2.z,
        v1.x * v2.y - v1.y * v2.x,
    )


def norm(v: Vec3D) -> float:
    """
    Calculates the norm of a 3 dimensional vector.

    :param v: Vector
    :return: Norm of the vector
    """
    return (v.x**2 + v.y**2 + v.z**2) ** 0.5


def normalize(v: Vec3D) -> Vec3D:
    """
    Normalizes a 3 dimensional vector.
    This should return a unit vector in the same direction as the input vector.

    :param v: Vector
    :return: Normalized vector
    """
    n = norm(v)
    return Vec3D(v.x / n, v.y / n, v.z / n)
