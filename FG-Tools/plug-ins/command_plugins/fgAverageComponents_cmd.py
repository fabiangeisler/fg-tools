"""

"""

import maya.api.OpenMaya as om
import fg_tools.modeling as mdl

maya_useNewAPI = True


# noinspection PyPep8Naming
class FgAverageComponents_cmd(om.MPxCommand):

    cmdName = 'fgAverageComponents'

    axisFlag = '-ax'
    axisFlagLong = '-axis'

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def creator():
        return FgAverageComponents_cmd()

    @staticmethod
    def createSyntax():
        syntax = om.MSyntax()
        syntax.setObjectType(om.MSyntax.kSelectionList)
        syntax.useSelectionAsDefault(True)
        syntax.addFlag(FgAverageComponents_cmd.axisFlag,
                       FgAverageComponents_cmd.axisFlagLong,
                       om.MSyntax.kString)
        return syntax

    def doIt(self, args):
        try:
            arguments = om.MArgDatabase(self.syntax(), args)
        except RuntimeError:
            om.MGlobal.displayError(('Error while parsing arguments:'
                                     '    If passing in list of nodes, also check that node names exist in scene.'))
            raise

        selection = arguments.getObjectList()

        if arguments.isFlagSet(FgAverageComponents_cmd.axisFlag):
            axis = arguments.flagArgumentString(FgAverageComponents_cmd.axisFlag, 0)
        else:
            axis = 'x'

        mdl.move_components_to_axis(selection.getSelectionStrings(), axis=axis)


# noinspection PyPep8Naming
def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.registerCommand(FgAverageComponents_cmd.cmdName,
                             FgAverageComponents_cmd.creator,
                             FgAverageComponents_cmd.createSyntax)


# noinspection PyPep8Naming
def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.deregisterCommand(FgAverageComponents_cmd.cmdName)
