'''
Created on 14.06.2016

:author: Fabian
'''
import os
import sys

import maya.cmds as cmds
import atexit

def uninitializeMayaPy():
    print 'uninitialize Mayapy'
    maya.standalone.uninitialize()

MAYASTANDALONE_INITALIZED = False

if not hasattr(cmds, "about") and not MAYASTANDALONE_INITALIZED:
    import maya.standalone
    maya.standalone.initialize(name='python')

    # Make sure all paths in PYTHONPATH are also in sys.path
    # When a maya module is loaded, the scripts folder is added to PYTHONPATH, but it doesn't seem
    # to be added to sys.path. So we are unable to import any of the python files that are in the
    # module/scripts folder. To workaround this, we simply add the paths to sys ourselves.
    realsyspath = [os.path.realpath(p) for p in sys.path]
    pythonpath = os.environ.get('PYTHONPATH', '')
    for p in pythonpath.split(os.pathsep):
        p = os.path.realpath(p)  # Make sure symbolic links are resolved
        if p not in realsyspath:
            sys.path.insert(0, p)

    # pymel is imported since its doing a lot of stuff automatically,
    # like sourcing the usersetup.mel and other stuff.
    import pymel.core  # @UnusedImport
    MAYASTANDALONE_INITALIZED = True

    atexit.register(uninitializeMayaPy)

else:
    print "Scipping initizalisation"
