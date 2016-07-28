'''
Created on 20.06.2016

:author: Fabian
'''
from pymel import core
from maya import cmds


def getModelPanel():
    """
    This function will get (or otherwise guess) the currently active model-panel!
    :return: the panel or an empty string if no panel is visible
    :rtype: str
    """
    mod_pan = cmds.getPanel(type='modelPanel')
    if mod_pan is None:
        mod_pan = []
    foc_pan = cmds.getPanel(withFocus=True)
    if foc_pan is None:
        foc_pan = []
    vis_pan = cmds.getPanel(visiblePanels=True)
    if vis_pan is None:
        vis_pan = []

    vis_mod_pan = list(set(mod_pan).intersection(set(vis_pan)))

    if len(vis_mod_pan) == 0:
        # no modelPanel visible
        return ""

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


def createViewportSnapshot(imageFile):
    '''
    creates a snapshot from the current Viewport and saves it to the specified path
    :param str imageFile: the full path for the image file.
    '''
    cmds.playblast(frame=core.currentTime(q=True),
                   format="image",
                   compression=imageFile.split(".")[-1].lower(),
                   completeFilename=imageFile,
                   percent=100)


def saveRenderViewImage(imageFile):

    editor = 'renderView'

    # if no image is in the render view this returns -1
    if cmds.renderWindowEditor(editor, q=True, nbImages=True) > -1:
        print "yeah"

    cmds.renderWindowEditor(editor, e=True, writeImage=imageFile)
