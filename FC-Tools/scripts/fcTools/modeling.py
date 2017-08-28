"""
This module collects functions that are handy for modeling.
"""
import maya.cmds as cmds
import components as com


def moveComponentsToAxis(components, axis='x'):
    """
    puts selected Components to the average of the specified axis
    """
    vertices = com.convertToVertices(components)
    aver = com.getMidpoint(vertices)

    if axis == 'x':
        cmds.move(aver[0], components, x=True)
    elif axis == 'y':
        cmds.move(aver[1], components, y=True)
    else:
        cmds.move(aver[2], components, z=True)


def freezeTransforms():
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


def toggleXRayDisplay(objects):
    """
    Toggles the XRay display in the viewport of the given objects.
    :param list objects:
    """
    if objects:
        xrayStatus = not cmds.displaySurface(objects[0], query=True, xRay=True)[0]
        for obj in objects:
            cmds.displaySurface(obj, xRay=xrayStatus)
