"""
This module is the entry point for the fg_tools library.
"""

import maya.cmds as cmds

import component
import file_system
import math_extended
import maya_runtime_command
import modeling
import pivot

__fg_toolsInitialized = False


def __initialize():
    """
    Initializes the fg_tools either from mayapy or regular maya. This will be called automatically once you import this
    package. It will __initialize all runtime commands that are accessible in "normal"- and in "batch"-mode.
    """
    global __fg_toolsInitialized

    if not __fg_toolsInitialized:

        cmds.loadPlugin('fg_tools_commands.py')

        initialize_runtime_commands()

        __fg_toolsInitialized = True
    else:
        cmds.warning('FG-Tools are already initialized')


def initialize_runtime_commands():
    """
    Creates all runtimeCommands that are accessible in "normal"- and in "batch"-mode.
    """
    main_category = 'FG-Tools'
    category = main_category + '.File'
    maya_runtime_command.create_runtime_command(command_name='fgSmartOpen',
                                                annotation='Open a maya file and tries to find and set the '
                                                           'appropriate project.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.smart_open()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgReloadScene',
                                                annotation='Reload the currently open scene.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.reload_scene()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgSaveIncremental',
                                                annotation='save the current maya file under a new version',
                                                command=('import fg_tools\n'
                                                         'fg_tools.save_incremental()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgOpenSceneFolder',
                                                annotation='open the current folder from this maya scene',
                                                command=('import fg_tools\n'
                                                         'fg_tools.open_scene_folder()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgOpenRenderFolder',
                                                annotation='open the folder where images will be rendered to',
                                                command=('import fg_tools\n'
                                                         'fg_tools.open_render_folder()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgOpenTextureFolder',
                                                annotation='open the texture folder',
                                                command=('import fg_tools\n'
                                                         'fg_tools.open_texture_folder()'),
                                                category=category)

    category = main_category + '.Selection'
    maya_runtime_command.create_runtime_command(command_name='fgSelectTriangles',
                                                annotation='select all triangles based on your current selection',
                                                command=('import fg_tools\n'
                                                         'fg_tools.select_triangles()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgSelectNGons',
                                                annotation='select all n-gons based on your current selection',
                                                command=('import fg_tools\n'
                                                         'fg_tools.select_n_gons()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgSelectLaminaFaces',
                                                annotation='select all lamina faces in your current selection',
                                                command=('import fg_tools\n'
                                                         'fg_tools.select_lamina_faces()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgSelectNonManifoldVertices',
                                                annotation='select all non-manifold vertices in your current selection',
                                                command=('import fg_tools\n'
                                                         'fg_tools.select_non_manifold_vertices()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgSelectUVSeams',
                                                annotation='select all uv-seams in your current selection',
                                                command=('import fg_tools\n'
                                                         'fg_tools.select_uv_seams()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgSelectHardEdges',
                                                annotation='select all hard edges in your current selection',
                                                command=('import fg_tools\n'
                                                         'fg_tools.select_hard_edges()'),
                                                category=category)

    category = main_category + '.Modeling'
    maya_runtime_command.create_runtime_command(command_name='fgSpherify',
                                                annotation='Move all selected components to equal distance to each '
                                                           'other.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.spherify()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgMoveComponentsToXAxis',
                                                annotation='Move all selected components so they\'re aligned on the '
                                                           'x-axis.',
                                                command=('import maya.cmds as cmds\n'
                                                         'cmds.fgAverageComponents(axis="x")'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgMoveComponentsToYAxis',
                                                annotation='Move all selected components so they\'re aligned on the '
                                                           'y-axis.',
                                                command=('import maya.cmds as cmds\n'
                                                         'cmds.fgAverageComponents(axis="y")'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgMoveComponentsToZAxis',
                                                annotation='Move all selected components so they\'re aligned on the '
                                                           'z-axis.',
                                                command=('import maya.cmds as cmds\n'
                                                         'cmds.fgAverageComponents(axis="z")'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgAssignDefaultShaderToSelection',
                                                annotation='Assign the Default Shader "lambert1" to all selected '
                                                           'objects.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.assign_default_shader_to_selection()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgToggleXRayDisplayOfSelection',
                                                annotation='Toggle X-Ray display in the viewport on all selected '
                                                           'objects.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.toggle_x_ray_display_of_selection()'),
                                                category=category)

    category = main_category + '.Pivots'
    maya_runtime_command.create_runtime_command(command_name='fgCopyPivot',
                                                annotation='Copies the pivot of the selected object.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.copy_pivot()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgPastePivot',
                                                annotation='Pastes the pivot to all selected objects.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.paste_pivot()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgPivotsToWorldCenter',
                                                annotation='Moves the pivots of all selected objects to the '
                                                           'world-center.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.pivots_to_world_center()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgPivotToSelection',
                                                annotation='Moves the pivot to the middle of the selected components.',
                                                command=('import fg_tools\n'
                                                         'fg_tools.pivot_to_component_selection()'),
                                                category=category)

    maya_runtime_command.create_runtime_command(command_name='fgPivotToBottom',
                                                annotation='Moves the pivot to the center of the combined bounding '
                                                           'box. Except the y-axis which will be at the bottom of the '
                                                           'bounding box',
                                                command=('import fg_tools\n'
                                                         'fg_tools.pivot_to_bottom()'),
                                                category=category)


def smart_open():
    file_before = cmds.file(q=True, sn=True)
    cmds.OpenScene()
    file_after = cmds.file(q=True, sn=True)

    if file_before != file_after:
        try:
            workspace_dir = file_system.get_workspace(file_after)
            cmds.workspace(workspace_dir, o=True)
            print 'The Project was set to: ' + workspace_dir,
        except OSError:
            cmds.warning('No Project-Directory found.')


def reload_scene():
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


def save_incremental():
    file_system.incremental_save()


def open_scene_folder():
    maya_file = cmds.file(q=True, sn=True)
    if maya_file:
        file_system.open_explorer(maya_file)
    else:
        cmds.warning('Your scene has not been saved yet!')


def open_render_folder():
    render_folder = file_system.get_render_folder()
    file_system.open_explorer(render_folder)
    print 'Opened Folder: ' + render_folder


def open_texture_folder():
    tex_folder = file_system.get_sourceimages_folder()
    file_system.open_explorer(tex_folder)
    print 'Opened Folder: ' + tex_folder


def select_triangles():
    tris = component.get_triangles()
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


def select_n_gons():
    ngons = component.get_ngons()
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


def select_lamina_faces():
    lamina = component.get_lamina_faces()
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


def select_non_manifold_vertices():
    nmv = component.get_non_manifold_vertices()
    if nmv:
        objects = list(set([vertex.split('.')[0] for vertex in nmv]))
        cmds.select(nmv)
        cmds.hilite(objects)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, vertex=True)
        print 'Selected {0:d} non-manifold vertices'.format(len(nmv)),
    else:
        cmds.selectMode(object=True)
        print 'Selection does not contain non-manifold-vertices.',


def select_uv_seams():
    """
    Select the UV seams on all selected objects.
    """
    cmds.selectMode(object=True)

    seam_edges = []
    for obj in cmds.ls(selection=True):
        seam_edges += component.get_seam_edges(obj)
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


def select_hard_edges():
    """
    Select the hard edges on all selected objects.
    """
    cmds.selectMode(object=True)

    hard_edges = []
    for obj in cmds.ls(selection=True):
        hard_edges += component.get_hard_edges(obj)
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
    Puts selected components to average distance to their midpoint.
    """
    vertices = component.convert_to_vertices(cmds.ls(selection=True))

    positions = [cmds.pointPosition(vertex) for vertex in vertices]
    midpoint = math_extended.midpoint(positions)

    distances = [math_extended.distance(midpoint, position) for position in positions]
    average_distance = math_extended.average(distances)

    new_positions = math_extended.spherify(positions, average_distance)

    for vertex, position in zip(vertices, new_positions):
        cmds.move(position[0], position[1], position[2], vertex, absolut=True)


def copy_pivot():
    """
    Save the pivot the currently selected pivot to apply it later with "paste_pivot".
    """
    sel = cmds.ls(selection=True, o=True)
    pivot.copy_pivot(sel[0])

    print 'Saved Pivot from: ' + sel[0],


def paste_pivot():
    """
    Paste the pivot information that previously has bin saved via "copy_pivot" onto all selected objects.
    """
    sel = cmds.ls(selection=True, o=True)
    for obj in sel:
        pivot.paste_pivot(obj)
    cmds.selectMode(object=True)

    print 'Applied Pivot to:    ' + str(sel),


def pivot_to_component_selection():
    """
    puts the pivot to the current component selection.
    """
    sel = cmds.ls(selection=True, fl=True)
    pivot.move_pivot_to_components(sel)
    cmds.selectMode(object=True)


def pivots_to_world_center():
    """
    Moves all pivots from the selected objects to the world center.
    """
    sel = cmds.ls(selection=True)
    for obj in sel:
        pivot.move_pivot_to_world_center(obj)


def pivot_to_bottom():
    """
    Moves all pivots from the selected objects to the center of their bounding box, except the y-axis will be on the
    bottom of the bounding box.
    """
    sel = cmds.ls(selection=True)
    pivot.pivot_to_bottom(sel)


def assign_default_shader_to_selection():
    """
    Assigns the default "lambert1" shader to the current selection.
    """
    cmds.sets(edit=True, forceElement='initialShadingGroup')


def toggle_x_ray_display_of_selection():
    """
    Toggles the XRay display in the viewport of the selected objects.
    """
    # this flag combination gives you all surface shapes below the selected surface shape
    sel = cmds.ls(selection=True, allPaths=True, dagObjects=True, type='surfaceShape')
    modeling.toggle_x_ray_display(objects=sel)


if not __fg_toolsInitialized:
    __initialize()
