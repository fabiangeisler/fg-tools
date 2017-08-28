"""
Functions for controlling pivots on objects.
"""
import maya.cmds as cmds
import components as com


gROTATEPIVOT = [0.0, 0.0, 0.0]
gSCALEPIVOT = [0.0, 0.0, 0.0]


def pivotToComponents(components):
    """
    puts the Pivot to the current component selection
    """
    vertices = com.convertToVertices(components)
    shape = vertices[0].split('.')[0]
    transform = cmds.listRelatives(shape, parent=True)[0]

    midX, midY, midZ = com.getMidpoint(vertices)

    cmds.move(midX, midY, midZ, transform + '.scalePivot')
    cmds.move(midX, midY, midZ, transform + '.rotatePivot')


def pivotToWorldCenter(obj):
    cmds.move(0, 0, 0, obj + '.scalePivot')
    cmds.move(0, 0, 0, obj + '.rotatePivot')


def copyPivot(obj):
    global gROTATEPIVOT
    global gSCALEPIVOT

    gROTATEPIVOT = cmds.xform(obj, query=True, worldSpace=True, rotatePivot=True)
    gSCALEPIVOT = cmds.xform(obj, query=True, worldSpace=True, scalePivot=True)


def pastePivot(obj):
    cmds.xform(obj, worldSpace=True, rotatePivot=gROTATEPIVOT)
    cmds.xform(obj, worldSpace=True, scalePivot=gSCALEPIVOT)
