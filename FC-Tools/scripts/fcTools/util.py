"""
little utility functions for this and that.
"""
import maya.cmds as cmds


def removePlugin(pluginName):
    """
    This tries to unload the given plugin from maya by deleting all its registered nodes first
    and the unload the plugin. There is still no guarantee that this will work.

    :param str pluginName: The name of the plugin
    """
    if cmds.pluginInfo(pluginName, q=True, loaded=True):
        cmds.pluginInfo(pluginName, e=True, autoload=False)

        nodeTypes = cmds.pluginInfo(pluginName, query=True, dependNode=True)

        for nodetype in nodeTypes:
            nodes = cmds.ls(type=nodetype)
            for node in nodes:
                cmds.lockNode(node, lock=False)
                print node
                cmds.delete(node)
        cmds.flushUndo()
        try:
            cmds.unloadPlugin(pluginName)
        except Exception as err:
            print err


def getUpstreamNodes(node):
    """
    :param str node:
    :returns: all upstream nodes of the given node
    :rtype: list
    """
    def getInputs(obj):
        inputs = cmds.listConnections(obj, source=True, destination=False)
        if inputs is not None:
            return set(inputs)
        return set()

    def getRecursiveInputs(obj, parentResults=None):
        if parentResults is None:
            parentResults = set()
        results = getInputs(obj)
        if results:
            results.add(obj)
            relevantResults = results - parentResults
            for inputNode in relevantResults:
                results = results.union(getRecursiveInputs(inputNode, results))
        return results

    resultNodes = getRecursiveInputs(node)
    resultNodes.discard(node)
    return list(resultNodes)


def attrChangedBetween(attr, start, end):
    """
    Takes the given attribute and checks if it changes between
    the given time range. This is helpful to check whether an object is animated regardless if its parented, constrained
    or has animationcurves.

    :param str attr: The attribute you want to check i.e. "persp.translateX"
    :param int start: The start frame for the check.
    :param int end: The end frame for the check.
    :returns: Whether the attribute changed.
    :rType: boolean
    """
    tmp = cmds.getAttr(attr, time=start)
    for frame in range(start + 1, end + 1):
        tmp2 = cmds.getAttr(attr, time=frame)
        if tmp != tmp2:
            return True
    return False


class UserSelection(object):
    """
    A context-manager to preserve the current selection of the user.

    ..Example::

        with UserSelection() as us:
            # in this code block you can select whatever you want.
            cmds.select(cmds.ls())
            # if you still have the need to know what the user selected you can query that.
            print us
        # here the last user selection is restored
    """

    @staticmethod
    def _getSelectMode():
        if cmds.selectMode(q=True, object=True):
            return "object"
        elif cmds.selectMode(q=True, component=True):
            return "component"
        elif cmds.selectMode(q=True, root=True):
            return "root"
        elif cmds.selectMode(q=True, leaf=True):
            return "leaf"
        elif cmds.selectMode(q=True, template=True):
            return "template"
        elif cmds.selectMode(q=True, hierarchical=True):
            return "hierarchical"
        elif cmds.selectMode(q=True, preset=True):
            return "preset"

    @staticmethod
    def _setSelectMode(mode):
        if mode == "object":
            cmds.selectMode(object=True)
        elif mode == "component":
            cmds.selectMode(component=True)
        elif mode == "root":
            cmds.selectMode(root=True)
        elif mode == "leaf":
            cmds.selectMode(leaf=True)
        elif mode == "template":
            cmds.selectMode(template=True)
        elif mode == "hierarchical":
            cmds.selectMode(hierarchical=True)
        elif mode == "preset":
            cmds.selectMode(preset=True)

    def __init__(self):
        self._userSelection = []
        self._selectMode = ""

    def __enter__(self):
        self._selectMode = self._getSelectMode()
        self._userSelection = cmds.ls(selection=True, long=True)
        return self._userSelection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._setSelectMode(self._selectMode)
        cmds.select(clear=True)
        # since the user could have changed some names in the code block of the with statement we will check
        # whether every stored item exist before selecting it again.
        exSel = [obj for obj in self._userSelection if cmds.objExists(obj)]
        if exSel:
            cmds.select(exSel)
        return False
