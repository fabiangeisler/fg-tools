'''
Created on 20.06.2016

:author: Fabian
'''
import maya.cmds as cmds
import components as com


def moveComponentsToAxis(components, axis="x"):
    """
    puts selected Components to the average of the specified axis
    """
    vertices = com.convertToVertices(components)
    aver = com.getMidpoint(vertices)

    if axis == "x":
        cmds.move(aver[0], components, x=True)
    elif axis == "y":
        cmds.move(aver[1], components, y=True)
    else:
        cmds.move(aver[2], components, z=True)
