"""
This module collects functions that are handy for modeling.
"""
import maya.cmds as cmds
import components as com


def move_components_to_axis(components, axis='x'):
    """
    puts selected Components to the average of the specified axis
    """
    vertices = com.convert_to_vertices(components)
    aver = com.get_midpoint(vertices)

    if axis == 'x':
        cmds.move(aver[0], components, x=True)
    elif axis == 'y':
        cmds.move(aver[1], components, y=True)
    else:
        cmds.move(aver[2], components, z=True)


def freeze_transforms():
    """
    Tries to freeze the transforms of the current selection.
    """
    try:
        cmds.makeIdentity(apply=True, translate=True)
    except Exception as fail:
        print fail

    try:
        cmds.makeIdentity(apply=True, rotate=True)
    except Exception as fail:
        print fail

    try:
        cmds.makeIdentity(apply=True, scale=True)
    except Exception as fail:
        print fail


def toggle_x_ray_display(objects):
    """
    Toggles the X-Ray display in the viewport of the given objects.
    :param list objects:
    """
    if objects:
        x_ray_status = not cmds.displaySurface(objects[0], query=True, xRay=True)[0]
        for obj in objects:
            cmds.displaySurface(obj, xRay=x_ray_status)
