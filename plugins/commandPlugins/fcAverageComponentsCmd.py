"""

"""

import maya.api.OpenMaya as om
import fcore.modeling as mdl

maya_useNewAPI = True


class FcAverageComponentsCmd(om.MPxCommand):

    cmdName = 'fcAverageComponents'

    axisFlag = '-ax'
    axisFlagLong = '-axis'

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def creator():
        return FcAverageComponentsCmd()

    @staticmethod
    def createSyntax():
        syntax = om.MSyntax()
        syntax.setObjectType(om.MSyntax.kSelectionList)
        syntax.useSelectionAsDefault(True)
        syntax.addFlag(FcAverageComponentsCmd.axisFlag,
                       FcAverageComponentsCmd.axisFlagLong,
                       om.MSyntax.kString)
        return syntax

    def doIt(self, args):
        try:
            argdb = om.MArgDatabase(self.syntax(), args)
        except RuntimeError:
            om.MGlobal.displayError(('Error while parsing arguments:'
                                     '    If passing in list of nodes, also check that node names exist in scene.'))
            raise

        selList = argdb.getObjectList()

        if argdb.isFlagSet(FcAverageComponentsCmd.axisFlag):
            axis = argdb.flagArgumentString(FcAverageComponentsCmd.axisFlag, 0)
        else:
            axis = 'x'

        mdl.moveComponentsToAxis(selList.getSelectionStrings(), axis=axis)


def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.registerCommand(FcAverageComponentsCmd.cmdName,
                             FcAverageComponentsCmd.creator,
                             FcAverageComponentsCmd.createSyntax)


def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.deregisterCommand(FcAverageComponentsCmd.cmdName)
