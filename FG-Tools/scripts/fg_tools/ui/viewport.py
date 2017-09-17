"""
This module contains functions for making playblasts and screenshots from
modelpanels in Maya. Because of this GUI dependency this should not be loaded in batch mode.
"""
import os
import datetime

from pymel import core
import maya.cmds as cmds


class CaptureThumbnail(object):
    """
    This class can capture thumbnails from the Viewport and save them as MetaData for the current Maya scene.
    After that you can view the screenshot in the Content Browser.

    Usage::

        CaptureThumbnail()
    """

    def __init__(self):
        cmds.thumbnailCaptureComponent(capture=True,
                                       fileDialogCallback=('python("import fg_tools.ui.viewport as viewport;'
                                                           'viewport.CaptureThumbnail.save_capture()")'))

    @staticmethod
    def save_capture():
        cmds.thumbnailCaptureComponent(save=cmds.file(query=True, sceneName=True))


def get_model_panel():
    """
    This function will get (or otherwise guess) the currently active model-panel!
    :return: the panel or an empty string if no panel is visible
    :rtype: str
    """
    mod_pan = cmds.getPanel(type='modelPanel') or []
    foc_pan = cmds.getPanel(withFocus=True) or []
    vis_pan = cmds.getPanel(visiblePanels=True) or []

    vis_mod_pan = list(set(mod_pan).intersection(set(vis_pan)))

    if not vis_mod_pan:
        # no modelPanel visible
        return ''

    elif len(vis_mod_pan) == 1:
        # 1 modelPanel visible! -> we found a winner!
        return vis_mod_pan[0]

    elif len(vis_mod_pan) > 1:
        # more than 1 modelPanel visible! get the one with focus!
        vis_mod_foc_pan = [pnl for pnl in vis_mod_pan if foc_pan in pnl]
        if vis_mod_foc_pan:
            # more than 1 modelPanel visible and one has focus! -> we found a winner!
            return vis_mod_foc_pan[0]
        else:
            # more than 1 modelPanel visible and none has focus... just take the first one!
            return vis_mod_pan[0]


def create_playblast(mode='desktop'):
    """
    make a playblast from the current model panel

    :param mode: 'dialog': Save with Dialog
                 'project': Save to Project Directory
                 'desktop': Save to Desktop
    """

    p = get_model_panel()
    cam = cmds.modelEditor(p, query=True, camera=True)
    curr_file_name = cmds.file(query=True, sn=True, shn=True)
    nice_file_name = ('{0:%Y%m%d_%H%M%S}_{1:s}_{2:s}'
                      '').format(datetime.datetime.now(),
                                 curr_file_name.strip('.ma'),
                                 cam)

    save_dir = os.path.expanduser('~').replace('Documents', 'Desktop/') + nice_file_name + '.mov'
    if mode == 'project':
        project_dir = cmds.workspace(query=True, rd=True)
        save_dir = project_dir + '/images/' + nice_file_name + '.mov'
    elif mode == 'dialog':
        save_dir = cmds.fileDialog2(cap='Save Playblast',
                                    fileFilter=('MOV (*.mov);;'
                                                'JPEG-Sequence (*.jpg)'),
                                    startingDirectory=save_dir,
                                    fileMode=0,
                                    okCaption='Save',
                                    dialogStyle=2)[0]

    win = core.window(title='Playblast Panel', widthHeight=(1282, 722))
    core.paneLayout()
    me = core.modelEditor(displayAppearance='smoothShaded',
                          displayTextures=True,
                          twoSidedLighting=False,
                          allObjects=False,
                          nurbsSurfaces=True,
                          polymeshes=True,
                          grid=False,
                          headsUpDisplay=False,
                          selectionHiliteDisplay=False,
                          camera=cam)
    core.showWindow(win)
    core.modelEditor(me, edit=True, activeView=True)

    if save_dir is not None:
        if save_dir.endswith('mov'):
            core.playblast(percent=100,
                           quality=90,
                           startTime=core.playbackOptions(query=True, minTime=True),
                           endTime=core.playbackOptions(query=True, maxTime=True),
                           format='qt',
                           compression='H.264',
                           forceOverwrite=True,
                           filename=save_dir)
        else:
            core.playblast(percent=100,
                           quality=90,
                           startTime=core.playbackOptions(query=True, minTime=True),
                           endTime=core.playbackOptions(query=True, maxTime=True),
                           format='image',
                           compression='jpg',
                           forceOverwrite=True,
                           filename=save_dir)

    core.deleteUI(win, window=True)


def create_viewport_snapshot(image_file):
    """
    Creates a snapshot from the current Viewport and saves it to the specified path.

    :param str image_file: the full path for the image file.
    """
    image_dir = os.path.dirname(image_file)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    cmds.playblast(frame=core.currentTime(query=True),
                   format='image',
                   compression=image_file.split('.')[-1].lower(),
                   completeFilename=image_file,
                   percent=100)


def toggle_smooth_shaded(model_editor):
    if wireframe_is_active(model_editor):
        set_wireframe_on_shaded(model_editor, value=True)
        set_smooth_shaded(model_editor)
    elif wireframe_on_shaded_is_active(model_editor):
        set_wireframe(model_editor)


def toggle_wireframe(model_editor):
    if smooth_shaded_is_active(model_editor) and wireframe_on_shaded_is_active(model_editor):
        set_wireframe_on_shaded(model_editor, value=False)
    elif smooth_shaded_is_active(model_editor) and not wireframe_on_shaded_is_active(model_editor):
        set_wireframe_on_shaded(model_editor, value=True)


def set_wireframe(model_editor):
    cmds.modelEditor(model_editor, edit=True, displayAppearance='wireframe')


def set_smooth_shaded(model_editor):
    cmds.modelEditor(model_editor, edit=True, displayAppearance='smoothShaded')


def set_wireframe_on_shaded(model_editor, value=True):
    cmds.modelEditor(model_editor, edit=True, wireframeOnShaded=value)


def wireframe_is_active(model_editor):
    return cmds.modelEditor(model_editor, query=True, displayAppearance=True) == 'wireframe'


def smooth_shaded_is_active(model_editor):
    return cmds.modelEditor(model_editor, query=True, displayAppearance=True) == 'smoothShaded'


def wireframe_on_shaded_is_active(model_editor):
    return cmds.modelEditor(model_editor, query=True, wireframeOnShaded=True)
