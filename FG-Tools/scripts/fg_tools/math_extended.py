"""
some extended math functionality
"""
import math


def spherify(points, radius):
    """
    :param list[list[float]] points:
    :param float radius:
    :returns: The points with average distance to their midpoint.
    :rtype: list[list[float]]
    """
    result_positions = []

    mid = midpoint(points)
    distances = [distance(mid, pos) for pos in points]

    mid_x, mid_y, mid_z = mid
    for pos, dist in zip(points, distances):
        if dist == 0:
            factor = 1
        else:
            factor = radius / dist
        x = (pos[0] - mid_x) * factor + mid_x
        y = (pos[1] - mid_y) * factor + mid_y
        z = (pos[2] - mid_z) * factor + mid_z
        result_positions.append([x, y, z])
    return result_positions


def distance(a, b):
    """
    :param list[float] a:
    :param list[float] b:
    :returns: the distance in 3D space of to given points
    :rtype: float
    """
    return math.sqrt((a[0] - b[0]) ** 2 +
                     (a[1] - b[1]) ** 2 +
                     (a[2] - b[2]) ** 2)


def average(numbers):
    """
    :param list[float] numbers: a list of numbers
    :returns: the average of the given number sequence. an empty list returns 0.
    :rtype: float
    """
    return float(sum(numbers)) / max(len(numbers), 1)


def midpoint(vectors):
    """
    :param list[list[float]] vectors: The list of vectors in the format [[x, y, z], [...]].
    :returns: The average Vector from the given list of vectors. An empty vectorList returns [0.0, 0.0, 0.0]
    :rtype: list
    """
    result = [0.0, 0.0, 0.0]

    if not vectors:
        return result

    all_x, all_y, all_z = zip(*vectors)
    result[0] = average(all_x)
    result[1] = average(all_y)
    result[2] = average(all_z)

    return result
