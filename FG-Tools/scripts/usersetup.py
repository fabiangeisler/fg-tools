"""
The main entry point for the FG-Tools.
"""
import maya.cmds as cmds


def initialize_fg_tools():
    """
    Initializes all components of the FG-Tools once Maya is started.
    Creates the Menu for the FG-Tools.
    In batch mode, only the parts that have no GUI dependency will be initialized.
    """
    if cmds.about(batch=True):
        import fg_tools
        print 'Skipped Menu creation of FG-Tools'
    else:
        import fg_tools.ui
        fg_tools.ui.create_menu()
    print 'FG-Tools initialized'

cmds.evalDeferred(initialize_fg_tools)
