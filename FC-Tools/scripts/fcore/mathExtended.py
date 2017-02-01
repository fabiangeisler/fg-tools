'''
some extend math functionality
'''
import math


def spherify(positions, radius):
    '''
    puts selected Components to average Distance to their Midpoint
    '''
    resultPositions = []

    midpoint = averageVector(positions)
    distances = [distance(midpoint, pos) for pos in positions]

    midX, midY, midZ = midpoint
    for pos, dist in zip(positions, distances):
        if dist == 0:
            factor = 1
        else:
            factor = radius / dist
        x = (pos[0] - midX) * factor + midX
        y = (pos[1] - midY) * factor + midY
        z = (pos[2] - midZ) * factor + midZ
        resultPositions.append([x, y, z])
    return resultPositions


def distance(pointA, pointB):
    '''
    :param list pointA:
    :param list pointB:
    :returns: the distance in 3D space of to given points
    :rtype: list
    '''
    return math.sqrt((pointA[0] - pointB[0]) ** 2 +
                     (pointA[1] - pointB[1]) ** 2 +
                     (pointA[2] - pointB[2]) ** 2)


def average(numberList):
    '''
    :param list numberList: a list of numbers
    :returns: the average of the given number sequence. an empty list returns 0.
    :rtype: float
    '''
    return float(sum(numberList)) / max(len(numberList), 1)


def averageVector(vectorList):
    '''
    :param list vectorList: The list of vectors in the format [[x, y, z], [...]].
    :returns: The average Vector from the given list of vectors. An empty vectorList returns [0.0, 0.0, 0.0]
    :rtype: list
    '''
    result = [0.0, 0.0, 0.0]

    if len(vectorList) < 1:
        return result

    allX, allY, allZ = zip(*vectorList)
    result[0] = average(allX)
    result[1] = average(allY)
    result[2] = average(allZ)

    return result
