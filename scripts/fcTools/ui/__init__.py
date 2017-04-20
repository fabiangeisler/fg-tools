'''
'''
import os

import maya.cmds as cmds

import fcTools.mayaRuntimeCommands as mrc

__FcToolsUIInitialized = False


def initialize():
    '''
    Initializes the fcTools either from mayapy or regular maya.
    '''
    if cmds.about(batch=True):
        raise RuntimeError('The menu for FC Tools can not be created in batch-mode.')
    else:
        scriptsDir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
        os.environ['XBMLANGPATH'] += ';' + os.path.dirname(scriptsDir) + '/icons'

        initializeRuntimeCommands()

        __FcToolsUIInitialized = True


def initializeRuntimeCommands():
    '''
    creates all runtimeCommands
    '''
    category = 'FC-Tools'
    subcategory = 'File'
    mrc.createRuntimeCommand(commandName='fcSmartOpen',
                             annotation='open a maya file and try to guess the project along the way',
                             command=('import fcTools\n'
                                      'fcTools.smartOpen()'),
                             category=category,
                             subcategory=subcategory)


if not __FcToolsUIInitialized:
    initialize()
