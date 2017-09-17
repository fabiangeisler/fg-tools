"""
Functions for debugging purposes.
"""
import os
from pprint import pprint
import sys

import maya.cmds as cmds


def reload_python_modules(script_path):
    """
    This reloads all currently loaded python modules that are located inside the given scriptPath.
    This is mainly meant to be a developer tool so no "reload()" functions have to be placed in the actual code.

    :param str script_path: The full path to the script directory.
    """
    script_path = script_path.replace("\\", "/")

    reload_modules = {}
    for modName, mod in sys.modules.iteritems():
        if mod is not None:
            mod_path = getattr(mod, '__file__', "")
            if mod_path:
                mod_path = mod_path.replace("\\", "/")
                if script_path in mod_path:
                    reload_modules[modName] = mod

    # sort module names by depth - so the deepest modules get reloaded first
    reload_order = sorted(reload_modules.keys(),
                          reverse=True,
                          key=lambda name: len(name.split(".")))

    percent = 100.0 / max(len(reload_modules), 1)

    for i, modName in enumerate(reload_order, 1):
        try:
            reload(reload_modules[modName])
        except Exception as error:
            print "ERROR:" + str(error)
        print "{0:3.0f}% loaded: reloading {1:s}".format(percent * i, modName)
    print "Reloaded {0:d} Modules.\n".format(len(reload_modules)),


def maya_module_info():
    """
    Prints out information about the currently loaded Maya modules.
    """
    mods = {}
    for mod in cmds.moduleInfo(listModules=True):

        beauty_environ = {}
        for key, value in dict(os.environ).iteritems():
            if ';' in value:
                value = value.split(';')
            paths = [path for path in value if path.startswith(cmds.moduleInfo(path=True, moduleName=mod))]
            if paths:
                beauty_environ[key] = paths

        file_content = []
        with open(cmds.moduleInfo(definition=True, moduleName=mod), 'r') as f:
            for line in f:
                file_content.append(line.replace('\r\n', ''))

        mods[mod] = {"modFile": cmds.moduleInfo(definition=True, moduleName=mod),
                     "modFileContent": file_content,
                     "path": cmds.moduleInfo(path=True, moduleName=mod),
                     "version": cmds.moduleInfo(version=True, moduleName=mod),
                     "environment": beauty_environ}
    pprint(mods)


def maya_environment_info():
    """
    Prints easily readable information about the currently loaded environment in Maya.
    """
    beauty_environ = {}
    for key, value in dict(os.environ).iteritems():
        if ';' in value:
            value = value.split(';')
        beauty_environ[key] = value
    print('{:*^100}'.format(' os.environ '))
    pprint(beauty_environ, indent=4)
    print('{:*^100}'.format(' sys.path '))
    pprint(sys.path)
