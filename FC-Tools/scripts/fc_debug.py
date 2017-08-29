"""
Functions for debugging purposes.
"""
import sys


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
