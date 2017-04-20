'''

'''
import maya.api.OpenMaya as om
from commandPlugins.fcAverageComponentsCmd import FcAverageComponentsCmd

maya_useNewAPI = True


def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.registerCommand(FcAverageComponentsCmd.cmdName,
                             FcAverageComponentsCmd.creator,
                             FcAverageComponentsCmd.createSyntax)


def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.deregisterCommand(FcAverageComponentsCmd.cmdName)
