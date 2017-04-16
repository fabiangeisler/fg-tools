'''
Functions for debugging purposes.
'''
import sys


def reloadPyModules(scriptPath):
    '''
    This reloads all currently loaded python modules that are located inside the given scriptPath.
    This is mainly meant to be a developer tool so no "reload()" functions have to be placed in the actual code.

    :param str scriptPath: The full path to the script directory.
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

    for i, modName in enumerate(reloadOrder, 1):
        try:
            reload(reloadModules[modName])
        except Exception as error:
            print "ERROR:" + str(error)
        print "{0:3.0f}% loaded: reloading {1:s}".format(percent * i, modName)
    print "Reloaded {0:d} Modules.\n".format(len(reloadModules)),
