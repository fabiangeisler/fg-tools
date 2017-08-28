"""
"""

import maya.cmds as cmds

import fcTools.mayaRuntimeCommand as mrc
import fcTools.fileSystem as fs
import playblast as pb
import datetime

__FcToolsUIInitialized = False


def initialize():
    """
    Initializes the fcTools either from mayapy or regular maya.
    """
    global __FcToolsUIInitialized

    if cmds.about(batch=True):
        raise RuntimeError('The menu for FC Tools can not be created in batch-mode.')
    else:
        initializeRuntimeCommands()

        __FcToolsUIInitialized = True


def initializeRuntimeCommands():
    """
    creates all runtimeCommands
    """
    mainCategory = 'FC-Tools'
    # ==================================================================================================================
    # category = mainCategory + '.File'
    # mrc.createRuntimeCommand(commandName='fcSmartOpen',
    #                          annotation='open a maya file and try to guess the project along the way',
    #                          command=('import fcTools\n'
    #                                   'fcTools.smartOpen()'),
    #                          category=category)
    # ==================================================================================================================

    category = mainCategory + '.Display'
    mrc.createRuntimeCommand(commandName='fcToggleSmoothShaded',
                             annotation='Toggles smooth shading in the current viewport.',
                             command=('import fcTools.ui\n'
                                      'fcTools.ui.toggleSmoothShaded()'),
                             category=category)

    mrc.createRuntimeCommand(commandName='fcToggleWireframe',
                             annotation='Toggles wireframe in the current viewport.',
                             command=('import fcTools.ui\n'
                                      'fcTools.ui.toggleWireframe()'),
                             category=category)


def saveSnapshot(mode='project'):
    """
    save a snapshot from the current model panel.

    :param mode: 'dialog': Save Snapshot with Dialog
                 'project': Save to Project Directory
                 'desktop': Save to Desktop
    """
    p = pb.getModelPanel()
    cam_name = cmds.modelEditor(p, query=True, camera=True).replace(':', '_')
    curr_file_name = cmds.file(query=True, sceneName=True, shortName=True)
    nice_file_name = '{0:%Y%m%d_%H%M%S}_{1:s}_{2:s}'.format(datetime.datetime.now(),
                                                            curr_file_name.strip('.ma'),
                                                            cam_name)

    desktopFolder = fs.getDesktopFolder()
    imageFile = desktopFolder + nice_file_name + '.jpg'
    if mode == 'project':
        imagesFolder = fs.getRenderFolder()
        imageFile = imagesFolder + nice_file_name + '.jpg'
    elif mode == 'dialog':
        imageFile = cmds.fileDialog2(cap='Save Screengrab',
                                     fileFilter='JPEG (*.jpg);;TIFF (*.tif)',
                                     startingDirectory=imageFile,
                                     fileMode=0,
                                     okCaption='Save',
                                     dialogStyle=2)
        if imageFile is not None:
            imageFile = imageFile[0]
        else:
            return
    print imageFile
    pb.createViewportSnapshot(imageFile)


def toggleSmoothShaded():
    mdlEditor = pb.getModelPanel()
    if mdlEditor:
        pb.toggleSmoothShaded(mdlEditor)


def toggleWireframe():
    mdlEditor = pb.getModelPanel()
    if mdlEditor:
        pb.toggleWireframe(mdlEditor)

if not __FcToolsUIInitialized:
    initialize()
