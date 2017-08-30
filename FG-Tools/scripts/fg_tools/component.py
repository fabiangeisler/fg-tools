"""
This module collects all functions that have something to do with polygon object components.

"""
import maya.cmds as cmds
import util
import math_extended as mx


def convert_to_vertices(components):
    """
    :param list[str] components:
    :returns: converts any given component-list to vertices
    :rtype: list[str]
    """
    vertices = cmds.polyListComponentConversion(components, tv=True)
    return cmds.ls(vertices, flatten=True)


def get_triangles(objects=None):
    """
    This gets all Triangles from the given objList.

    :param list objects: List of objects you want the Triangles from.
                         If this is None the current selection will be used.
    :returns: a list of triangle faces
    :rtype: list of str
    """
    if objects is None:
        objects = []

    with util.UserSelection():
        if objects:
            cmds.select(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, polymeshFace=1)
        cmds.polySelectConstraint(mode=3, type=0x0008, size=1)
        cmds.polySelectConstraint(mode=0, size=0)
        tris = cmds.ls(selection=True, long=True)
    return tris


def get_ngons(objects=None):
    """
    This gets all N-Gons from the given objList.

    :param list objects: List of objects you want the N-Gons from.
                         If this is None the current User-selection will be used.
    :returns: a list of n-gons
    :rtype: list of str
    """
    if objects is None:
        objects = []

    with util.UserSelection():
        if objects:
            cmds.select(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, polymeshFace=1)
        cmds.polySelectConstraint(mode=3, type=0x0008, size=3)
        cmds.polySelectConstraint(mode=0, size=0)
        ngons = cmds.ls(selection=True, long=True)
    return ngons


def get_lamina_faces(objects=None):
    """
    This gets all lamina faces from the given objList.

    :param list objects: List of objects you want the lamina faces from.
                         If this is None the current selection will be used.
    :returns: a list of lamina faces
    :rtype: list of str
    """
    if objects is None:
        objects = []

    with util.UserSelection():
        if objects:
            cmds.select(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, polymeshFace=1)
        cmds.polySelectConstraint(mode=3, type=0x0008, topology=2)
        cmds.polySelectConstraint(mode=0, topology=0)
        lamina = cmds.ls(selection=True, long=True)
    return lamina


def get_non_manifold_vertices(objects=None):
    """
    This gets all non-manifold vertices from the given objList.

    :param list objects: List of objects you want the non-manifold vertices from.
                         If this is None the current selection will be used.
    :returns: a list of non-manifold-vertices
    :rtype: list of str
    """
    if objects is None:
        objects = []

    with util.UserSelection():
        if objects:
            cmds.select(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=0, vertex=1)
        cmds.polySelectConstraint(mode=3, type=0x0001, nonmanifold=1)
        cmds.polySelectConstraint(mode=0, nonmanifold=0)
        nmv = cmds.ls(selection=True, long=True)
    return nmv


def is_on_uv_seam(edge):
    """
    :param str edge: The edge to check
    :returns: whether the given edge has more than 2 UV-Points associated with it. (Which means it lies on a seam.)
    :rtype: bool
    """
    uv_points = cmds.polyListComponentConversion(edge, fromEdge=True, toUV=True)
    flat_uv_points = cmds.ls(uv_points, flatten=True)
    return len(flat_uv_points) > 2


def get_seam_edges(obj):
    """
    :param str obj: the polygon Object to get the edges from
    :returns: all edges that lie on a uv-seam.
    :rtype: list
    """
    edges = cmds.ls(obj + '.e[*]', flatten=True)
    return [edge for edge in edges if is_on_uv_seam(edge)]


def get_hard_edges(obj):
    """
    :param str obj:
    :returns: all hard edges from the given mesh in a flat list
    :rtype: list of str
    """
    return [obj + '.e[' + str(i) + ']'
            for i, edgeInfo in enumerate(cmds.polyInfo(obj + '.e[*]', ev=True))
            if edgeInfo.endswith('Hard\n')]


def get_midpoint(vertices):
    """
    This function calculates the midpoint of a given vertex list.

    :param list vertices: The flat list of vertices.
    :return list midpoint: The midpoint in the format
                           [mid_x(float), mid_y(float), mid_z(float)].
    """
    # The midpoint from an arbitrary number of vertices is the average of all their positions.

    positions = [cmds.pointPosition(vertex) for vertex in vertices]
    return mx.midpoint(positions)
