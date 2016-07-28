'''
Created on 12.06.2016

@author: Fabian
'''
import pymel.core as pm


class FcMenu():

    def __init__(self):

        fcMenuName = "fcMenu"
        if pm.menu(fcMenuName, query=True, exists=True):
            pm.deleteUI(fcMenuName, menu=True)

        with pm.menu(fcMenuName, tearOff=True, parent=pm.MelGlobals()['gMainWindow'], label="FC Tools"):
            pm.menuItem(dividerLabel='File', divider=True)
            pm.menuItem(label='Smart Open',  # image='fileOpen.png',
                        sourceType="mel",
                        command=('int $mods = `getModifiers`;\n'
                                 'if ($mods % 2) { // Shift\n'
                                 '    fcReloadScene;\n'
                                 '} else {\n'
                                 '    fcSmartOpen;\n'
                                 '}'),
                        annotation=("Open File and set Project if possible.\n"
                                    "Shift: Reload the current Scene."),
                        imageOverlayLabel="Open")
            pm.menuItem(label='Save Incremental',  # image='save.png',
                        sourceType="mel",
                        command="fcSaveIncremental;",
                        annotation="Incremental Save")
            pm.menuItem(label='Save Snapshot',  # image='save.png',
                        sourceType="mel",
                        command="fcSaveSnapshot;",
                        annotation="Save a snapshot from the viewport in your current render folder.")

            with pm.subMenuItem(tearOff=True, label="Open Explorer"):
                pm.menuItem(label='Open Scene Folder',  # image='openScript.png',
                            sourceType="mel",
                            command="fcOpenSceneFolder;",
                            annotation="Open Scene Folder")
                pm.menuItem(label='Open Render Folder',  # image='openScript.png',
                            sourceType="mel",
                            command="fcOpenRenderFolder;",
                            annotation="Open Render Folder")
                pm.menuItem(label='Open Texture Folder',  # image='openScript.png',
                            sourceType="mel",
                            command="fcOpenTextureFolder;",
                            annotation="Open Texture Folder")

            pm.menuItem(dividerLabel='Select', divider=True)
            pm.menuItem(label="Select Triangles",
                        command="fcSelectTriangles;",
                        imageOverlayLabel="Tris",
                        sourceType="mel",
                        echoCommand=True,
                        annotation='Select Triangles from all polygon objects you selected.')
            pm.menuItem(label="Select N-Gons",
                        imageOverlayLabel="N-Gons",
                        command="fcSelectNGons;",
                        sourceType="mel",
                        echoCommand=True,
                        annotation='Select N-Gons from all polygon objects you selected.')
            pm.menuItem(label="Select Lamina Faces",
                        imageOverlayLabel="Lamina",
                        command="fcSelectLaminaFaces;",
                        sourceType="mel",
                        echoCommand=True,
                        annotation='Select lamina faces from all polygon objects you selected.')
            pm.menuItem(label="Select Non-Manifold Vertices",
                        imageOverlayLabel="NonMani",
                        command="fcSelectNonManifoldVertices;",
                        sourceType="mel",
                        echoCommand=True,
                        annotation='Select Non-Manifold Vertices from all polygon objects you selected.')
            pm.menuItem(label="Select UV-Seams",
                        imageOverlayLabel="UVSeam",
                        command="fcSelectUVSeams;",
                        sourceType="mel",
                        echoCommand=True,
                        annotation='Select UV-Seams in polygon objects you selected.')

            pm.menuItem(dividerLabel='Modeling', divider=True)
            pm.menuItem(label="Spherify",
                        command="fcSpherify;",
                        imageOverlayLabel="spherify",
                        sourceType="mel",
                        echoCommand=True,
                        annotation='Move all selected components to equal distance.')
            pm.menuItem(label="Move Components to X-Axis",
                        command="fcMoveComponentsToXAxis;",
                        imageOverlayLabel="mcX",
                        sourceType="mel",
                        echoCommand=True,
                        annotation="Move all selected components so they're aligned on the x-axis.")
            pm.menuItem(label="Move Components to Y-Axis",
                        command="fcMoveComponentsToYAxis;",
                        imageOverlayLabel="mcX",
                        sourceType="mel",
                        echoCommand=True,
                        annotation="Move all selected components so they're aligned on the y-axis.")
            pm.menuItem(label="Move Components to Z-Axis",
                        command="fcMoveComponentsToZAxis;",
                        imageOverlayLabel="mcX",
                        sourceType="mel",
                        echoCommand=True,
                        annotation="Move all selected components so they're aligned on the z-axis.")
            pm.menuItem(label="Copy Pivot",
                        command="fcCopyPivot;",
                        imageOverlayLabel="copyP",
                        sourceType="mel",
                        echoCommand=True,
                        annotation="Copies the pivot of the selected object.")
            pm.menuItem(label="Paste Pivot",
                        command="fcPastePivot;",
                        imageOverlayLabel="pasteP",
                        sourceType="mel",
                        echoCommand=True,
                        annotation="Pastes the pivot to all selected objects.")
"""

                    pm.symbolButton('PlayBlastSBtn', image='CameraDown.png',
                                    command=self.playblast_sbtn_cmd,
                                    annotation=("Make a Playblast.\n"
                                                "Ctrl: Make a Playblast and save to your Desktop.\n"
                                                "Shift: Make a Playblast and save to your Project directory."))


                    pm.symbolButton('NodeEditorSBtn',
                                    image='nodeGrapherUnlocked.png',
                                    command=self.unlock_node_sbtn_cmd,
                                    annotation=("unlock selected Nodes\n"
                                                "Shift: lock selected Nodes.\n"
                                                "Ctrl: unlock and delete selected Nodes"))

                    pm.symbolButton('DefaultMaterialSBtn',
                                    image='FC_Modeling/lambertshd.png',
                                    command=self.default_material_sbtn_cmd,
                                    annotation="Assign Default Shader.")
                    pm.symbolButton('FreezeTransformsSBtn',
                                    image='FC_Modeling/freezetrans.png',
                                    command=self.freeze_transforms_sbtn_cmd,
                                    annotation="Freeze Transforms.")

                    pm.symbolButton('MdlCheckSBtn',
                                    image='polyCheck.png',
                                    command=self.mdl_check_sbtn_cmd,
                                    annotation="Check and fix various Modeling Problems.")

                    pm.symbolButton('CenterPivotSBtn',
                                    image='FC_Modeling/centerpivot.png',
                                    command=self.center_pivot_sbtn_cmd,
                                    annotation="Center Pivot")
                    pm.symbolButton('PivotToWorldCenterSBtn',
                                    image='FC_Modeling/centerpivotworld.png',
                                    command=self.pivot_to_world_center_sbtn_cmd,
                                    annotation="Center Pivot to World")
                    pm.symbolButton('PivotToSelectionSBtn',
                                    image='FC_Modeling/aligntoworld.png',
                                    command=self.pivot_to_selection_sbtn_cmd,
                                    annotation="Center Pivot to Selection")
                    pm.symbolCheckBox('SaveAndPastePivotSCB',
                                      onImage='FC_Modeling/pastePivot.png',
                                      offImage='FC_Modeling/copyPivot.png',
                                      offCommand=self.save_and_paste_pivot_scboff_cmd,
                                      onCommand=self.save_and_paste_pivot_scbon_cmd,
                                      annotation="Copy and Paste a Pivot")

                    pm.symbolButton('XRayObjectSBtn',
                                    image='FC_Modeling/togglexray.png',
                                    command=self.xray_object_sbtn_cmd,
                                    annotation="Toggle Xray for selected Object")


    def snapshot_sbtn_cmd(self, value):
        mods = cmds.getModifiers()
        if (mods & 1) > 0:  # Shift
            save_snapshot("project")
        elif (mods & 4) > 0:  # Ctrl
            save_snapshot("desktop")
        else:
            save_snapshot("dialog")

    def playblast_sbtn_cmd(self, value):
        mods = cmds.getModifiers()
        if (mods & 1) > 0:  # Shift
            make_playblast("project")  # Save to Project Directory
        elif (mods & 4) > 0:  # Ctrl
            make_playblast("desktop")  # save to Desktop
        else:
            make_playblast("dialog")  # save with Dialog


    def unlock_node_sbtn_cmd(self, value):
        mods = cmds.getModifiers()
        if (mods & 1) > 0:  # Shift
            change_lock_node(lock=True, delete_node=False)
        elif (mods & 4) > 0:  # Ctrl
            change_lock_node(lock=False, delete_node=True)
        else:
            change_lock_node(lock=False, delete_node=False)

    def default_material_sbtn_cmd(self, value):
        cmds.sets(e=True, forceElement="initialShadingGroup")

    def freeze_transforms_sbtn_cmd(self, value):
        freeze_transforms()

    def mdl_check_sbtn_cmd(self, value):
        mdl = FCc.Checker.ModelingCheck()
        mdl.check_and_fix_ui()

    def center_pivot_sbtn_cmd(self, value):
        mel.eval('CenterPivot')

    def pivot_to_world_center_sbtn_cmd(self, value):
        pivot_to_world_center()

    def pivot_to_selection_sbtn_cmd(self, value):
        pivot_to_selection()

    def save_and_paste_pivot_scbon_cmd(self, value):
        save_pivot_location()

    def save_and_paste_pivot_scboff_cmd(self, value):
        paste_pivot_location()

    def xray_object_sbtn_cmd(self, value):
        toggle_xray()

"""
