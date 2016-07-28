'''
Created on 12.06.2016

:author: Fabian
'''
import os
import sys
import maya.cmds as cmds


def initialize():

    os.environ["FC_SCRIPTS"] = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    os.environ["FC_ICONS"] = os.path.dirname(os.environ["FC_SCRIPTS"]) + "/icons/"

    import fcore.fcmds as fcmds
    fcmds.initFcModelingTools()

    if cmds.about(batch=True):
        print "Scipping initizalisation of UI"
    else:
        import fcore.fcontroller as fctl
        fctl.initializeRuntimeCommands()
        import fcore.ui.fcMenu as fm
        fm.FcMenu()


def reloadPyModules(scriptPath):
    '''
    :param str scriptPath: The full path to the script directory.
    This reloads all currently loaded python modules that are located inside the given scriptPath.
    This is mainly meant to be a developer tool so no "reload()" functions have to be placed in the actual code.
    '''
    scriptPath = scriptPath.replace("\\", "/")

    reloadModules = {}
    for modName, mod in sys.modules.iteritems():
        if mod is not None:
            modPath = getattr(mod, '__file__', "")
            if modPath:
                modPath = modPath.replace("\\", "/")
                if scriptPath in modPath:
                    reloadModules[modName] = mod

    # sort module names by depth - so the deepest modules get reloaded first
    reloadOrder = sorted(reloadModules.keys(),
                         reverse=True,
                         key=lambda name: len(name.split(".")))

    percent = 100.0 / max(len(reloadModules), 1)

    for i, modName in enumerate(reloadOrder):
        try:
            reload(reloadModules[modName])
        except Exception as error:
            print "ERROR:" + str(error)
        print "{0:3.0f}% loaded: reloading {1:s}".format(percent * (i + 1), modName)
    print "Reloaded {0:d} Modules.".format(len(reloadModules)),
