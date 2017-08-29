"""
Functions for controlling pivots on objects.
"""
import maya.cmds as cmds
import components as com


ROTATE_PIVOT = [0.0, 0.0, 0.0]
SCALE_PIVOT = [0.0, 0.0, 0.0]


def move_pivot_to_components(components):
    """
    puts the Pivot to the current component selection

    :param list[str] components: A list of components.
    """
    vertices = com.convert_to_vertices(components)
    shape = vertices[0].split('.')[0]
    transform = cmds.listRelatives(shape, parent=True)[0]

    mid_x, mid_y, mid_z = com.get_midpoint(vertices)

    cmds.move(mid_x, mid_y, mid_z, transform + '.scalePivot')
    cmds.move(mid_x, mid_y, mid_z, transform + '.rotatePivot')


def move_pivot_to_world_center(obj):
    """
    Moves the pivot if the given object to the world center

    :param str obj:
    """
    cmds.move(0, 0, 0, obj + '.scalePivot')
    cmds.move(0, 0, 0, obj + '.rotatePivot')


def copy_pivot(obj):
    """
    Saves the pivot location from the given object temporally to apply it later via paste_pivot()

    :param str obj:
    """
    global ROTATE_PIVOT
    global SCALE_PIVOT

    ROTATE_PIVOT = cmds.xform(obj, query=True, worldSpace=True, rotatePivot=True)
    SCALE_PIVOT = cmds.xform(obj, query=True, worldSpace=True, scalePivot=True)


def paste_pivot(obj):
    """
    Applies he previously saved pivot to the given object.

    :param str obj:
    """
    cmds.xform(obj, worldSpace=True, rotatePivot=ROTATE_PIVOT)
    cmds.xform(obj, worldSpace=True, scalePivot=SCALE_PIVOT)
