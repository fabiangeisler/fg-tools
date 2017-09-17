"""
Functions for file system manipulation.
"""
import os
import subprocess
import maya.cmds as cmds
import re


def get_workspace(file_path):
    """
    takes the given file path and walks up the structure and tries to find the workspace.mel.
    and returns it when it finds it.

    :param str file_path:
    :rtype: str
    """
    parent_folder = os.path.dirname(file_path)
    while not os.path.exists(parent_folder + '/workspace.mel'):
        next_folder = os.path.dirname(parent_folder)
        if next_folder == parent_folder:
            raise OSError('Could not find workspace.mel')
        else:
            parent_folder = next_folder
    return parent_folder


def open_explorer(path):
    """
    opens the windows explorer with the given file selected.

    :param str path: File or folder path to open.
    """
    if os.path.isfile(path):
        subprocess.Popen(r'Explorer /select,{0:s}'.format(path.replace('/', '\\')))
    else:
        os.startfile(path)


def get_render_folder():
    """
    :returns: the current folder where images will be rendered.
    :rtype: str
    """
    return cmds.workspace(expandName=cmds.workspace(fileRuleEntry='images')) + '/'


def get_sourceimages_folder():
    """
    :returns: the current textures folder.
    :rtype: str
    """
    return cmds.workspace(expandName=cmds.workspace(fileRuleEntry='sourceImages')) + '/'


def get_desktop_folder():
    """
    :returns: The absolute path to the desktop.
    :rtype: str
    """
    return os.path.expanduser('~').replace('Documents', 'Desktop') + '/'


def incremental_save():
    """
    This function finds the last number in the currently open filename, increments it by 1 and saves the file under this
    new name.
    """
    curr_filename = cmds.file(q=True, sn=True)
    match = re.finditer(r'\d+', curr_filename)

    if match:
        last_number = [m for m in match][-1]

        new_number_int = int(last_number.group(0)) + 1
        new_number_str = str(new_number_int).zfill(len(last_number.group(0)))

        increment_filename = curr_filename[:last_number.start(0)] + new_number_str + curr_filename[last_number.end(0):]

        cmds.file(rename=increment_filename)

        if curr_filename.endswith('mb'):
            file_type = 'mayaBinary'
        else:
            file_type = 'mayaAscii'
        cmds.file(save=True, type=file_type)
        print 'File saved: ' + increment_filename + '\n',
    else:
        cmds.warning('Filename has no Numbers in it!')
