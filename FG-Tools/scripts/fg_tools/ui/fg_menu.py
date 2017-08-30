"""
This module Contains the Main class for creating the Menu of the FG-Tools.
"""
import pymel.core as pm


class FgMenu(object):

    def __init__(self):

        fg_menu_name = 'fg_menu'
        if pm.menu(fg_menu_name, query=True, exists=True):
            pm.deleteUI(fg_menu_name, menu=True)

        with pm.menu(fg_menu_name, tearOff=True, parent=pm.MelGlobals()['gMainWindow'], label='FG-Tools'):
            pm.menuItem(dividerLabel='File', divider=True)
            pm.menuItem(label='Smart Open',
                        image='fileOpen.png',
                        sourceType='mel',
                        command=('int $mods = `getModifiers`;\n'
                                 'if ($mods % 2) { // Shift\n'
                                 '    fgReloadScene;\n'
                                 '} else {\n'
                                 '    fgSmartOpen;\n'
                                 '}'),
                        annotation=('Open File and set Project if possible.\n'
                                    'Shift: Reload the current Scene.'))
            pm.menuItem(label='Save Incremental',
                        sourceType='mel',
                        command='fgSaveIncremental;',
                        annotation='Incremental Save')
            pm.menuItem(label='Save Snapshot',
                        sourceType='mel',
                        command='fgSaveSnapshot;',
                        annotation='Save a snapshot from the viewport in your current render folder.')

            with pm.subMenuItem(tearOff=True, label='Open Explorer'):
                pm.menuItem(label='Open Scene Folder',
                            sourceType='mel',
                            command='fgOpenSceneFolder;',
                            annotation='Open Scene Folder')
                pm.menuItem(label='Open Render Folder',
                            sourceType='mel',
                            command='fgOpenRenderFolder;',
                            annotation='Open Render Folder')
                pm.menuItem(label='Open Texture Folder',
                            sourceType='mel',
                            command='fgOpenTextureFolder;',
                            annotation='Open Texture Folder')

            pm.menuItem(dividerLabel='Select', divider=True)
            pm.menuItem(label='Select Triangles',
                        command='fgSelectTriangles;',
                        image='fg_triangles.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select Triangles from all polygon objects you selected.')
            pm.menuItem(label='Select N-Gons',
                        image='fg_ngons.png',
                        command='fgSelectNGons;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select N-Gons from all polygon objects you selected.')
            pm.menuItem(label='Select Lamina Faces',
                        imageOverlayLabel='Lamina',
                        command='fgSelectLaminaFaces;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select lamina faces from all polygon objects you selected.')
            pm.menuItem(label='Select Non-Manifold Vertices',
                        imageOverlayLabel='NonMani',
                        command='fgSelectNonManifoldVertices;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select Non-Manifold Vertices from all polygon objects you selected.')
            pm.menuItem(label='Select UV-Seams',
                        imageOverlayLabel='UVSeam',
                        command='fgSelectUVSeams;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select UV-Seams in polygon objects you selected.')
            pm.menuItem(label='Select Hard Edges',
                        imageOverlayLabel='HardE',
                        command='fgSelectHardEdges;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select hard edges in polygon objects you selected.')

            pm.menuItem(dividerLabel='Modeling', divider=True)
            pm.menuItem(label='Spherify',
                        command='fgSpherify;',
                        image='fg_spherify.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components to equal distance.')
            pm.menuItem(label='Move Components to X-Axis',
                        command='fgAverageComponents -axis "x";',
                        image='fg_average_selection_x.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components so they are aligned on the x-axis.')
            pm.menuItem(label='Move Components to Y-Axis',
                        command='fgAverageComponents -axis "y";',
                        image='fg_average_selection_y.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components so they are aligned on the y-axis.')
            pm.menuItem(label='Move Components to Z-Axis',
                        command='fgAverageComponents -axis "z";',
                        image='fg_average_selection_z.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components so they are aligned on the z-axis.')
            pm.menuItem(label='Assign Default Shader',
                        command='fgAssignDefaultShaderToSelection;',
                        image='fg_lambert1.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Assign the Default Shader "lambert1" to all selected objects.')
            pm.menuItem(label='Toggle X-Ray',
                        command='fgToggleXrayDisplayOfSelection;',
                        image='fg_x_ray.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Toggle X-Ray display in the viewport on all selected objects.')

            pm.menuItem(dividerLabel='Pivots', divider=True)
            pm.menuItem(label='Copy Pivot',
                        command='fgCopyPivot;',
                        image='fg_copy_pivot.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Copies the pivot of the selected object.')
            pm.menuItem(label='Paste Pivot',
                        command='fgPastePivot;',
                        image='fg_paste_pivot.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Pastes the pivot to all selected objects.')
            pm.menuItem(label='Pivots to WorldCenter',
                        command='fgPivotsToWorldCenter;',
                        image='fg_center_pivot_world.png',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Moves the pivots of all selected objects to the world-center.')
            pm.menuItem(label='Pivot to Selection',
                        command='fgPivotToSelection;',
                        imageOverlayLabel='selP',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Moves the pivot to the middle of the selected components.')
            pm.menuItem(label='Pivot to Bottom',
                        command='fgPivotToBottom;',
                        imageOverlayLabel='Pbot',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Moves the pivot to the center of the combined bounding box. Except the y-axis '
                                   'which will be at the bottom of the bounding box')
