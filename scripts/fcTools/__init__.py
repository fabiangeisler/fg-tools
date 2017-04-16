'''
This module is the entry point for the fcTools library.
'''
import os
import maya.cmds as cmds
import fcontroller as fctl
import fcmds

__FcToolsInitialized = False


def initialize():
    '''
    Initializes the fcTools either from mayapy or regular maya.
    '''
    fcmds.initFcModelingTools()

    scriptsDir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
    os.environ['MAYA_PLUG_IN_PATH'] += ';' + os.path.dirname(scriptsDir) + '/plugins'
    cmds.loadPlugin('fcToolCommands.py')

    fctl.initializeRuntimeCommands()

    __FcToolsInitialized = True


def createMenu():
    if cmds.about(batch=True):
        raise RuntimeError('The menu for FC Tools can not be created in batch-mode.')
    else:
        scriptsDir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
        os.environ['XBMLANGPATH'] += ';' + os.path.dirname(scriptsDir) + '/icons'

        import ui.fcMenu as fm
        fm.FcMenu()


if not __FcToolsInitialized:
    initialize()
