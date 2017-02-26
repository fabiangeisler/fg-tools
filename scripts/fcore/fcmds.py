'''
This module contains all core functions that can be safely run during batchmode.
'''
import maya.mel as mel


def initFcModelingTools():
    '''
    This initializes all basic settings for the pipeline.
    '''
    # unload some nasty plugins
    # for plugin in ["Mayatomr", "Turtle", "ngSkin", "VectorRender"]:
    #     utils.removePlugin(plugin)

    # this prevents maya from writing and loading panel configuration into scene files.
    # corresponding optionVar -> 'useSaveScenePanelConfig'
    mel.eval("$gUseSaveScenePanelConfig = false;")
    # corresponding optionVar -> 'useScenePanelConfig'
    mel.eval("$gUseScenePanelConfig = false;")
