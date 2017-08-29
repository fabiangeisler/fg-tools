"""
This module is the entry point for the fc_tools library.
"""

import maya.cmds as cmds

import components as com
import file_system as fs
import math_extended as mx
import maya_runtime_command as mrc
import modeling as mdl
import pivot as piv

__fc_toolsInitialized = False


def initialize():
    """
    Initializes the fc_tools either from mayapy or regular maya.
    """
    global __fc_toolsInitialized

    cmds.loadPlugin('fcToolCommands.py')

    initializeRuntimeCommands()

    __fc_toolsInitialized = True


def createMenu():
    """
    Creates the Menu to access the FC-Tools from the GUI.

    :raises:
        :RuntimeError: When you call this in batch mode.
    """
    if cmds.about(batch=True):
        raise RuntimeError('The menu for FC Tools can not be created in batch-mode.')
    else:
        import ui.fc_menu as fm
        fm.FcMenu()


def initializeRuntimeCommands():
    """
    creates all runtimeCommands
    """
    main_category = 'FC-Tools'
    category = main_category + '.File'
    mrc.create_runtime_command(command_name='fcSmartOpen',
                               annotation='open a maya file and try to guess the project along the way',
                               command=('import fc_tools\n'
                                        'fc_tools.smartOpen()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcReloadScene',
                               annotation='Reload the currently open scene.',
                               command=('import fc_tools\n'
                                        'fc_tools.reloadScene()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSaveIncremental',
                               annotation='save the current maya file under a new version',
                               command=('import fc_tools\n'
                                        'fc_tools.saveIncremental()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSaveSnapshot',
                               annotation='create a snapshot of the viewport and save it in the render folder.',
                               command=('import fc_tools.ui\n'
                                        'fc_tools.ui.saveSnapshot()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcOpenSceneFolder',
                               annotation='open the current folder from this maya scene',
                               command=('import fc_tools\n'
                                        'fc_tools.openSceneFolder()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcOpenRenderFolder',
                               annotation='open the folder where images will be rendered to',
                               command=('import fc_tools\n'
                                        'fc_tools.openRenderFolder()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcOpenTextureFolder',
                               annotation='open the texture folder',
                               command=('import fc_tools\n'
                                        'fc_tools.openTextureFolder()'),
                               category=category)

    category = main_category + '.Selection'
    mrc.create_runtime_command(command_name='fcSelectTriangles',
                               annotation='select all triangles based on your current selection',
                               command=('import fc_tools\n'
                                        'fc_tools.selectTriangles()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSelectNGons',
                               annotation='select all n-gons based on your current selection',
                               command=('import fc_tools\n'
                                        'fc_tools.selectNGons()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSelectLaminaFaces',
                               annotation='select all lamina faces in your current selection',
                               command=('import fc_tools\n'
                                        'fc_tools.selectLaminaFaces()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSelectNonManifoldVertices',
                               annotation='select all non-manifold vertices in your current selection',
                               command=('import fc_tools\n'
                                        'fc_tools.selectNonManifoldVertices()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSelectUVSeams',
                               annotation='select all uv-seams in your current selection',
                               command=('import fc_tools\n'
                                        'fc_tools.selectUVSeams()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcSelectHardEdges',
                               annotation='select all hard edges in your current selection',
                               command=('import fc_tools\n'
                                        'fc_tools.selectHardEdges()'),
                               category=category)

    category = main_category + '.Modeling'
    mrc.create_runtime_command(command_name='fcSpherify',
                               annotation='Move all selected components to equal distance to each other.',
                               command=('import fc_tools\n'
                                        'fc_tools.spherify()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcMoveComponentsToXAxis',
                               annotation='Move all selected components so they\'re aligned on the x-axis.',
                               command=('import maya.cmds as cmds\n'
                                        'cmds.fcAverageComponents(axis="x")'),
                               category=category)

    mrc.create_runtime_command(command_name='fcMoveComponentsToYAxis',
                               annotation='Move all selected components so they\'re aligned on the y-axis.',
                               command=('import maya.cmds as cmds\n'
                                        'cmds.fcAverageComponents(axis="y")'),
                               category=category)

    mrc.create_runtime_command(command_name='fcMoveComponentsToZAxis',
                               annotation='Move all selected components so they\'re aligned on the z-axis.',
                               command=('import maya.cmds as cmds\n'
                                        'cmds.fcAverageComponents(axis="z")'),
                               category=category)

    mrc.create_runtime_command(command_name='fcAssignDefaultShaderToSelection',
                               annotation='Assign the Default Shader "lambert1" to all selected objects.',
                               command=('import fc_tools\n'
                                        'fc_tools.assignDefaultShaderToSelection()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcToggleXrayDisplayOfSelection',
                               annotation='Toggle X-Ray display in the viewport on all selected objects.',
                               command=('import fc_tools\n'
                                        'fc_tools.toggleXrayDisplayOfSelection()'),
                               category=category)

    category = main_category + '.Pivots'
    mrc.create_runtime_command(command_name='fcCopyPivot',
                               annotation='Copies the pivot of the selected object.',
                               command=('import fc_tools\n'
                                        'fc_tools.copyPivot()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcPastePivot',
                               annotation='Pastes the pivot to all selected objects.',
                               command=('import fc_tools\n'
                                        'fc_tools.pastePivot()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcPivotsToWorldCenter',
                               annotation='Moves the pivots of all selected objects to the world-center.',
                               command=('import fc_tools\n'
                                        'fc_tools.pivotsToWorldCenter()'),
                               category=category)

    mrc.create_runtime_command(command_name='fcPivotToSelection',
                               annotation='Moves the pivot to the middle of the selected components.',
                               command=('import fc_tools\n'
                                        'fc_tools.pivotToComponentSelection()'),
                               category=category)


def smartOpen():
    file_before = cmds.file(q=True, sn=True)
    cmds.OpenScene()
    file_after = cmds.file(q=True, sn=True)

    if file_before != file_after:
        try:
            workspace_dir = fs.get_workspace(file_after)
            cmds.workspace(workspace_dir, o=True)
            print 'The Project was set to: ' + workspace_dir,
        except OSError:
            cmds.warning('No Project-Directory found.')


def reloadScene():
    maya_file = cmds.file(q=True, sn=True)
    if maya_file:
        if 'Yes' == cmds.confirmDialog(title='Reload Scene',
                                       message=('Are you sure you want to '
                                                'reload the Scene?'),
                                       button=['Yes', 'No'],
                                       defaultButton='No',
                                       cancelButton='No',
                                       dismissString='No'):
            cmds.file(maya_file, open=True, force=True)
    else:
        cmds.warning('Your scene has not been saved yet!')


def saveIncremental():
    fs.incremental_save()


def openSceneFolder():
    maya_file = cmds.file(q=True, sn=True)
    if maya_file:
        fs.open_explorer(maya_file)
    else:
        cmds.warning('Your scene has not been saved yet!')


def openRenderFolder():
    render_folder = fs.get_render_folder()
    fs.open_explorer(render_folder)
    print 'Opened Folder: ' + render_folder


def openTextureFolder():
    tex_folder = fs.get_sourceimages_folder()
    fs.open_explorer(tex_folder)
    print 'Opened Folder: ' + tex_folder


def selectTriangles():
    tris = com.get_triangles()
    if tris:
        objects = list(set([tri.split('.')[0] for tri in tris]))
        cmds.select(tris)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshFace=True)
        print 'Selected {0:d} Triangles.\n'.format(len(tris)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not contain Triangles!\n',


def selectNGons():
    ngons = com.get_ngons()
    if ngons:
        objects = list(set([ngon.split('.')[0] for ngon in ngons]))
        cmds.select(ngons)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshFace=True)
        print 'Selected {0:d} N-Gons.\n'.format(len(ngons)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not contain N-Gons!\n',


def selectLaminaFaces():
    lamina = com.get_lamina_faces()
    if lamina:
        objects = list(set([l.split('.')[0] for l in lamina]))
        cmds.select(lamina)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshFace=True)
        print 'Selected {0:d} lamina faces.\n'.format(len(lamina)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not contain lamina faces!\n',


def selectNonManifoldVertices():
    nmv = com.get_non_manifold_vertices()
    if nmv:
        objects = list(set([vert.split('.')[0] for vert in nmv]))
        cmds.select(nmv)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, vertex=True)
        print 'Selected {0:d} non-manifold vertices'.format(len(nmv)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not contain non-manifold-vertices.',


def selectUVSeams():
    """
    select the UV Seams on all selected objects.
    """
    cmds.selectMode(object=True)

    seam_edges = []
    for obj in cmds.ls(selection=True):
        seam_edges += com.get_seam_edges(obj)
    if seam_edges:
        objects = list(set([edge.split('.')[0] for edge in seam_edges]))

        cmds.select(seam_edges)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshEdge=True)
        print 'Selected {0:d} seam edges.\n'.format(len(seam_edges)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not seam edges.\n',


def selectHardEdges():
    """
    select the hard edges on all selected objects.
    """
    cmds.selectMode(object=True)

    hard_edges = []
    for obj in cmds.ls(selection=True):
        hard_edges += com.get_hard_edges(obj)
    if hard_edges:
        objects = list(set([edge.split('.')[0] for edge in hard_edges]))

        cmds.select(hard_edges)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshEdge=True)
        print 'Selected {0:d} hard edges.\n'.format(len(hard_edges)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not hard edges.\n',


def spherify():
    """
    puts selected Components to average Distance to their Midpoint
    """
    vertices = com.convert_to_vertices(cmds.ls(selection=True))

    positions = [cmds.pointPosition(vertex) for vertex in vertices]
    midpoint = mx.midpoint(positions)

    distances = [mx.distance(midpoint, pos) for pos in positions]
    average_distance = mx.average(distances)

    new_positions = mx.spherify(positions, average_distance)

    for vertex, pos in zip(vertices, new_positions):
        cmds.move(pos[0], pos[1], pos[2], vertex, a=True)


def copyPivot():
    sel = cmds.ls(selection=True, o=True)
    piv.copy_pivot(sel[0])

    print 'Saved Pivot from: ' + sel[0],


def pastePivot():
    sel = cmds.ls(selection=True, o=True)
    for obj in sel:
        piv.paste_pivot(obj)
    cmds.selectMode(object=True)

    print 'Applied Pivot to:    ' + str(sel),


def pivotToComponentSelection():
    """
    puts the Pivot to the current component selection
    """
    sel = cmds.ls(selection=True, fl=True)
    piv.move_pivot_to_components(sel)
    cmds.selectMode(object=True)


def pivotsToWorldCenter():
    """
    Moves all pivots from the selected objects to the world center
    """
    sel = cmds.ls(selection=True)
    for obj in sel:
        piv.move_pivot_to_world_center(obj)


def assignDefaultShaderToSelection():
    cmds.sets(edit=True, forceElement='initialShadingGroup')


def toggleXrayDisplayOfSelection():
    """
    Toggles the XRay display in the viewport of the selected objects.
    """
    # this flag combination gives you all surface shapes below the selected surface shape
    sel = cmds.ls(selection=True, allPaths=True, dagObjects=True, type='surfaceShape')
    mdl.toggle_x_ray_display(objects=sel)


if not __fc_toolsInitialized:
    initialize()
