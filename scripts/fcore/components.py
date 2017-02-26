'''
This module collects all functions that have something to do with polygon object components.

'''
import maya.cmds as cmds
import util
import mathExtended as mx


def convertToVertices(componentList):
    '''
    :param list componentList:
    :returns: converts any given component-list to vertices
    :rtype: list
    '''
    vertices = cmds.polyListComponentConversion(componentList, tv=True)
    return cmds.ls(vertices, flatten=True)


def getTriangles(objList=None):
    '''
    This gets all Triangles from the given objList.

    :param list objList: List of objects you want the Triangles from.
                         If this is None the current selection will be used.
    :returns: a list of triangle faces
    :rtype: list of str
    '''
    if objList is None:
        objList = []

    tris = []  # @UnusedVariable
    with util.UserSelection():
        if objList:
            cmds.select(objList)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, polymeshFace=1)
        cmds.polySelectConstraint(mode=3, type=0x0008, size=1)
        cmds.polySelectConstraint(mode=0, size=0)
        tris = cmds.ls(selection=True, long=True)
    return tris


def getNGons(objList=None):
    '''
    This gets all N-Gons from the given objList.

    :param list objList: List of objects you want the N-Gons from.
                         If this is None the current User-selection will be used.
    :returns: a list of n-gons
    :rtype: list of str
    '''
    if objList is None:
        objList = []

    ngons = []  # @UnusedVariable
    with util.UserSelection():
        if objList:
            cmds.select(objList)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, polymeshFace=1)
        cmds.polySelectConstraint(mode=3, type=0x0008, size=3)
        cmds.polySelectConstraint(mode=0, size=0)
        ngons = cmds.ls(selection=True, long=True)
    return ngons


def getLaminaFaces(objList=None):
    '''
    This gets all lamina faces from the given objList.

    :param list objList: List of objects you want the lamina faces from.
                         If this is None the current selection will be used.
    :returns: a list of lamina faces
    :rtype: list of str
    '''
    if objList is None:
        objList = []

    lamina = []  # @UnusedVariable
    with util.UserSelection():
        if objList:
            cmds.select(objList)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, polymeshFace=1)
        cmds.polySelectConstraint(mode=3, type=0x0008, topology=2)
        cmds.polySelectConstraint(mode=0, topology=0)
        lamina = cmds.ls(selection=True, long=True)
    return lamina


def getNonManifoldVertices(objList=None):
    '''
    This gets all non-manifold vertecies from the given objList.

    :param list objList: List of objects you want the non-manifold vertecies from.
                         If this is None the current selection will be used.
    :returns: a list of non-manifold-vertecies
    :rtype: list of str
    '''
    if objList is None:
        objList = []

    nmv = []  # @UnusedVariable
    with util.UserSelection():
        if objList:
            cmds.select(objList)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, vertex=1)
        cmds.polySelectConstraint(mode=3, type=0x0001, nonmanifold=1)
        cmds.polySelectConstraint(mode=0, nonmanifold=0)
        nmv = cmds.ls(selection=True, long=True)
    return nmv


def isOnUvSeam(edge):
    '''
    :param str edge: The edge to check
    :returns: whether the given edge has more than 2 UV-Points associated with it. (Which means it lies on a seam.)
    :rtype: bool
    '''
    uvPoints = cmds.polyListComponentConversion(edge, fromEdge=True, toUV=True)
    flatUvPoints = cmds.ls(uvPoints, flatten=True)
    return len(flatUvPoints) > 2


def getSeamEdges(obj):
    '''
    :param str obj: the polygon Object to get the edges from
    :returns: all edges that lie on a uv-seam.
    :rtype: list
    '''
    edges = cmds.ls(obj + '.e[*]', flatten=True)
    return [edge for edge in edges if isOnUvSeam(edge)]


def getHardEdges(obj):
    '''
    :param str obj:
    :returns: all hard edges from the given mesh in a flat list
    :rtype: list of str
    '''
    return [obj + '.e[' + str(i) + ']'
            for i, edgeInfo in enumerate(cmds.polyInfo(obj + '.e[*]', ev=True))
            if edgeInfo.endswith('Hard\n')]


def getMidpoint(vertex_list):
    '''
    This function calculates the midpoint of a given vertex list.

    :param list vertex_list: The flat list of vertices.
    :return list midpoint: The midpoint in the format
                           [mid_x(float), mid_y(float), mid_z(float)].
    '''
    # The midpoint from an arbitrary number of vertices is the average of all their positions.

    positions = [cmds.pointPosition(vertex) for vertex in vertex_list]
    return mx.midpoint(positions)
