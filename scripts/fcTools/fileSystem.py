'''
Functions for file system manipulation.
'''
import os
import subprocess
import maya.cmds as cmds
import re


def findWorkspace(filePath):
    '''
    takes the given file path and walks up the structure and tries to find the workspace.mel.
    and returns it when it finds it.

    :param str filePath:
    :rtype: str
    '''
    dirname = os.path.dirname(filePath)
    while not os.path.exists(dirname + '/workspace.mel'):
        newDirname = os.path.dirname(dirname)
        if newDirname == dirname:
            raise OSError('Could not find workspace.mel')
        else:
            dirname = newDirname
    return dirname


def openExplorer(path):
    '''
    opens the windows explorer with the given file selected.
    :param str path:
    '''
    if os.path.isfile(path):
        subprocess.Popen(r'Explorer /select,{0:s}'.format(path.replace('/', '\\')))
    else:
        os.startfile(path)


def getRenderFolder():
    '''
    :returns: the current folder where images will be rendered.
    :rtype: str
    '''
    return cmds.workspace(expandName=cmds.workspace(fileRuleEntry='images')) + '/'


def getSourceimagesFolder():
    '''
    :returns: the current textures folder.
    :rtype: str
    '''
    return cmds.workspace(expandName=cmds.workspace(fileRuleEntry='sourceImages')) + '/'


def getDesktopFolder():
    return os.path.expanduser('~').replace('Documents', 'Desktop') + '/'


def incremental_save():

    curr_filename = cmds.file(q=True, sn=True)
    match = re.finditer(r'\d+', curr_filename)

    if match:
        pos_of_numbers = [m for m in match]
        last_number = pos_of_numbers[-1]

        inc_number_int = int(last_number.group(0)) + 1
        new_number_str = str(inc_number_int).zfill(len(last_number.group(0)))

        increment_filename = curr_filename[:last_number.start(0)] + new_number_str + curr_filename[last_number.end(0):]

        cmds.file(rename=increment_filename)

        if curr_filename.endswith('mb'):
            filetype = 'mayaBinary'
        else:
            filetype = 'mayaAscii'
        cmds.file(save=True, type=filetype)
        print 'File saved: ' + increment_filename,
    else:
        cmds.warning('Filename has no Numbers in it!')
