"""
The main entry point plugin which collects and initializes all other custom commands.
"""
import maya.api.OpenMaya as om

import command_plugins.fgAverageComponents_cmd

maya_useNewAPI = True


# noinspection PyPep8Naming
def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin, vendor='Fabian Geisler', version='v0.1.0', apiVersion='Any')
    command_plugins.fgAverageComponents_cmd.attach_command(mfn_plugin=pluginFn)


# noinspection PyPep8Naming
def uninitializePlugin(plugin):
    command_plugins.fgAverageComponents_cmd.uninitializePlugin(plugin=plugin)
