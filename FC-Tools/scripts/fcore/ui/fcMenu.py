'''
This module Contains the Main class for creating the Menu of the fcTools.
'''
import pymel.core as pm


class FcMenu():

    def __init__(self):

        fcMenuName = 'fcMenu'
        if pm.menu(fcMenuName, query=True, exists=True):
            pm.deleteUI(fcMenuName, menu=True)

        with pm.menu(fcMenuName, tearOff=True, parent=pm.MelGlobals()['gMainWindow'], label='FC Tools'):
            pm.menuItem(dividerLabel='File', divider=True)
            pm.menuItem(label='Smart Open',  # image='fileOpen.png',
                        sourceType='mel',
                        command=('int $mods = `getModifiers`;\n'
                                 'if ($mods % 2) { // Shift\n'
                                 '    fcReloadScene;\n'
                                 '} else {\n'
                                 '    fcSmartOpen;\n'
                                 '}'),
                        annotation=('Open File and set Project if possible.\n'
                                    'Shift: Reload the current Scene.'),
                        imageOverlayLabel='Open')
            pm.menuItem(label='Save Incremental',
                        sourceType='mel',
                        command='fcSaveIncremental;',
                        annotation='Incremental Save')
            pm.menuItem(label='Save Snapshot',
                        sourceType='mel',
                        command='fcSaveSnapshot;',
                        annotation='Save a snapshot from the viewport in your current render folder.')

            with pm.subMenuItem(tearOff=True, label='Open Explorer'):
                pm.menuItem(label='Open Scene Folder',
                            sourceType='mel',
                            command='fcOpenSceneFolder;',
                            annotation='Open Scene Folder')
                pm.menuItem(label='Open Render Folder',
                            sourceType='mel',
                            command='fcOpenRenderFolder;',
                            annotation='Open Render Folder')
                pm.menuItem(label='Open Texture Folder',
                            sourceType='mel',
                            command='fcOpenTextureFolder;',
                            annotation='Open Texture Folder')

            pm.menuItem(dividerLabel='Select', divider=True)
            pm.menuItem(label='Select Triangles',
                        command='fcSelectTriangles;',
                        imageOverlayLabel='Tris',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select Triangles from all polygon objects you selected.')
            pm.menuItem(label='Select N-Gons',
                        imageOverlayLabel='N-Gons',
                        command='fcSelectNGons;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select N-Gons from all polygon objects you selected.')
            pm.menuItem(label='Select Lamina Faces',
                        imageOverlayLabel='Lamina',
                        command='fcSelectLaminaFaces;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select lamina faces from all polygon objects you selected.')
            pm.menuItem(label='Select Non-Manifold Vertices',
                        imageOverlayLabel='NonMani',
                        command='fcSelectNonManifoldVertices;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select Non-Manifold Vertices from all polygon objects you selected.')
            pm.menuItem(label='Select UV-Seams',
                        imageOverlayLabel='UVSeam',
                        command='fcSelectUVSeams;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select UV-Seams in polygon objects you selected.')
            pm.menuItem(label='Select Hard Edges',
                        imageOverlayLabel='HardE',
                        command='fcSelectHardEdges;',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Select hard edges in polygon objects you selected.')

            pm.menuItem(dividerLabel='Modeling', divider=True)
            pm.menuItem(label='Spherify',
                        command='fcSpherify;',
                        imageOverlayLabel='spherify',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components to equal distance.')
            pm.menuItem(label='Move Components to X-Axis',
                        command='fcMoveComponentsToXAxis;',
                        imageOverlayLabel='mcX',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components so they are aligned on the x-axis.')
            pm.menuItem(label='Move Components to Y-Axis',
                        command='fcMoveComponentsToYAxis;',
                        imageOverlayLabel='mcX',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components so they are aligned on the y-axis.')
            pm.menuItem(label='Move Components to Z-Axis',
                        command='fcMoveComponentsToZAxis;',
                        imageOverlayLabel='mcX',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Move all selected components so they are aligned on the z-axis.')
            pm.menuItem(label='Assign Default Shader',
                        command='fcAssignDefaultShaderToSelection;',
                        imageOverlayLabel='lam1',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Assign the Default Shader "lambert1" to all selected objects.')
            pm.menuItem(label='Toggle X-Ray',
                        command='fcToggleXrayDisplayOfSelection;',
                        imageOverlayLabel='XRay',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Toggle X-Ray display in the viewport on all selected objects.')

            pm.menuItem(dividerLabel='Pivots', divider=True)
            pm.menuItem(label='Copy Pivot',
                        command='fcCopyPivot;',
                        imageOverlayLabel='copyP',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Copies the pivot of the selected object.')
            pm.menuItem(label='Paste Pivot',
                        command='fcPastePivot;',
                        imageOverlayLabel='pasteP',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Pastes the pivot to all selected objects.')
            pm.menuItem(label='Pivots to WorldCenter',
                        command='fcPivotsToWorldCenter;',
                        imageOverlayLabel='worldP',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Moves the pivots of all selected objects to the world-center.')
            pm.menuItem(label='Pivot to Selection',
                        command='fcPivotToSelection;',
                        imageOverlayLabel='selP',
                        sourceType='mel',
                        echoCommand=True,
                        annotation='Moves the pivot to the middle of the selected components.')
