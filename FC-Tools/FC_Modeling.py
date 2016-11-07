'''
'''

import datetime
import os

import pymel.core as pm
import maya.cmds as cmds


def make_playblast(mode="desktop"):
    """
    make a playblast from the current model panel
    :param mode: "dialog": Save with Dialog
                 "project": Save to Project Directory
                 "desktop": Save to Desktop
    """

    p = get_model_panel()
    cam_name = cmds.modelEditor(p, q=True, camera=True)
    curr_file_name = cmds.file(q=True, sn=True, shn=True)
    nice_file_name = ("{0:%Y%m%d_%H%M%S}_{1:s}_{2:s}"
                      "").format(datetime.datetime.now(),
                                 curr_file_name.strip(".ma"),
                                 cam_name)

    save_dir = os.path.expanduser("~").replace("Documents", "Desktop/") + nice_file_name + ".mov"
    if mode == "project":
        project_dir = cmds.workspace(q=True, rd=True)
        save_dir = project_dir + "/images/" + nice_file_name + ".mov"
    elif mode == "dialog":
        save_dir = cmds.fileDialog2(cap="Save Playblast",
                                    fileFilter=("MOV (*.mov);;"
                                                "JPEG-Sequence (*.jpg)"),
                                    startingDirectory=save_dir,
                                    fileMode=0,
                                    okCaption="Save",
                                    dialogStyle=2)[0]

    win = pm.window(title="Playblast Panel", widthHeight=(1282, 722))
    pm.paneLayout()
    me = pm.modelEditor(displayAppearance="smoothShaded",
                        displayTextures=True,
                        twoSidedLighting=False,
                        allObjects=False,
                        nurbsSurfaces=True,
                        polymeshes=True,
                        grid=False,
                        headsUpDisplay=False,
                        selectionHiliteDisplay=False,
                        camera=cam_name)
    pm.showWindow(win)
    pm.modelEditor(me, edit=True, activeView=True)

    if save_dir is not None:
        if save_dir.endswith("mov"):
            pm.playblast(percent=100,
                         quality=90,
                         startTime=pm.playbackOptions(q=True, minTime=True),
                         endTime=pm.playbackOptions(q=True, maxTime=True),
                         format="qt",
                         compression="H.264",
                         forceOverwrite=True,
                         filename=save_dir)
        else:
            pm.playblast(percent=100,
                         quality=90,
                         startTime=pm.playbackOptions(q=True, minTime=True),
                         endTime=pm.playbackOptions(q=True, maxTime=True),
                         format="image",
                         compression="jpg",
                         forceOverwrite=True,
                         filename=save_dir)

    pm.deleteUI(win, window=True)


def change_lock_node(lock=False, delete_node=False):
    sel = cmds.ls(selection=True, long=True)
    for node in sel:
        if cmds.lockNode(node, q=True, lock=True) != lock:
            cmds.lockNode(node, lock=lock)
            if not lock and delete_node:
                cmds.delete(node)


def freeze_transforms():
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


def toggle_xray():
    sel = cmds.ls(sl=True, ap=True, dag=True, type='surfaceShape')

    for obj in sel:
        xray_status = cmds.displaySurface(obj, q=True, xRay=True)
        cmds.displaySurface(obj, xRay=not(xray_status[0]))
