"""
Short description of this module.
"""
import pymel.core


def createRuntimeCommand(commandName, command, annotation='', category='', commandLanguage='python', default=True):
    """
    Creates a custom command in Maya that can be accessed via Mel or Python at runtime.
    Be aware that you can not change an already created runtime command. You have to restart Maya and create it again.

    :param str commandName: The name of the command
    :param str command: The script you want to execute when the command is called.
    :param str annotation: (optional) A short description of what this command does.
    :param str category: (optional) You can place this command in a certain category so it's more logically sorted
                         in the hotkey editor. You can also have subcategories by inserting a "." between them
                         (i.e. "MainCategory.SubCategory")
    :param str commandLanguage: (optional) Can be "mel" or "python".
    :param str default: (optional) If this is True, Maya will not save this command in the preferences.
    """
    if not annotation:
        annotation = commandName

    if not pymel.core.runTimeCommand(commandName, exists=True):
        pymel.core.runTimeCommand(commandName,
                                  annotation=annotation,
                                  command=command,
                                  category=category,
                                  commandLanguage=commandLanguage,
                                  default=default)
    else:
        pymel.core.warning(('The runtime command "{0:s}" already exists and can not be overwritten. '
                            'To change an established runtime command you need to restart maya and create it again.'
                            '').format(commandName))
