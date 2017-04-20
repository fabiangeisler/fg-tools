'''

'''
import maya.api.OpenMaya as om
import commandPlugins.fcAverageComponentsCmd

maya_useNewAPI = True


def initializePlugin(plugin):
    commandPlugins.fcAverageComponentsCmd.initializePlugin(plugin=plugin)


def uninitializePlugin(plugin):
    commandPlugins.fcAverageComponentsCmd.uninitializePlugin(plugin=plugin)
