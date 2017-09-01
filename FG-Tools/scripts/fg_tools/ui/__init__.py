"""
"""
import datetime

import maya.cmds as cmds

import fg_tools.maya_runtime_command
import fg_tools.file_system as fs
import viewport
import fg_menu

__fg_toolsUIInitialized = False


def __initialize():
    """
    Initializes the parts of the FG-Tools that have dependencies to the Maya GUI.
    """
    global __fg_toolsUIInitialized

    if not __fg_toolsUIInitialized:
        if cmds.about(batch=True):
            raise RuntimeError('The UI parts of the FG-Tools can not be created in batch-mode.')
        else:
            initialize_runtime_commands()

            __fg_toolsUIInitialized = True
    else:
        cmds.warning('The UI parts of the FG-Tools are already initialized.')


def create_menu():
    """
    Creates the Menu to access the FG-Tools.
    """
    fg_menu.FgMenu()


def initialize_runtime_commands():
    """
    Creates all runtimeCommands that are depended to the Maya GUI.
    """
    main_category = 'FG-Tools'

    category = main_category + '.Display'
    fg_tools.maya_runtime_command.create_runtime_command(command_name='fgToggleSmoothShaded',
                                                         annotation=toggle_smooth_shaded.__doc__,
                                                         command=('import fg_tools.ui\n'
                                                                  'fg_tools.ui.toggle_smooth_shaded()'),
                                                         category=category)

    fg_tools.maya_runtime_command.create_runtime_command(command_name='fgToggleWireframe',
                                                         annotation=toggle_wireframe.__doc__,
                                                         command=('import fg_tools.ui\n'
                                                                  'fg_tools.ui.toggle_wireframe()'),
                                                         category=category)

    fg_tools.maya_runtime_command.create_runtime_command(command_name='fgSaveSnapshot',
                                                         annotation='Create a snapshot of the viewport and save it in '
                                                                    'the render folder.',
                                                         command=('import fg_tools.ui\n'
                                                                  'fg_tools.ui.save_snapshot()'),
                                                         category=category)


def save_snapshot(mode='project'):
    """
    save a snapshot from the current model panel.

    :param mode: 'dialog': Save Snapshot with Dialog
                 'project': Save to Project Directory
                 'desktop': Save to Desktop
    """
    p = viewport.get_model_panel()
    cam_name = cmds.modelEditor(p, query=True, camera=True).replace(':', '_')
    curr_file_name = cmds.file(query=True, sceneName=True, shortName=True)
    nice_file_name = '{0:%Y%m%d_%H%M%S}_{1:s}_{2:s}'.format(datetime.datetime.now(),
                                                            curr_file_name.strip('.ma'),
                                                            cam_name)

    desktop_folder = fs.get_desktop_folder()
    image_file = desktop_folder + nice_file_name + '.jpg'
    if mode == 'project':
        images_folder = fs.get_render_folder()
        image_file = images_folder + nice_file_name + '.jpg'
    elif mode == 'dialog':
        image_file = cmds.fileDialog2(cap='Save Screenshot',
                                      fileFilter='JPEG (*.jpg);;TIFF (*.tif)',
                                      startingDirectory=image_file,
                                      fileMode=0,
                                      okCaption='Save',
                                      dialogStyle=2)
        if image_file is not None:
            image_file = image_file[0]
        else:
            return
    print image_file
    viewport.create_viewport_snapshot(image_file)


def toggle_smooth_shaded():
    """
    Toggles smooth shading in the current viewport.
    """
    model_editor = viewport.get_model_panel()
    if model_editor:
        viewport.toggle_smooth_shaded(model_editor)


def toggle_wireframe():
    """
    Toggles wireframe in the current viewport.
    """
    model_editor = viewport.get_model_panel()
    if model_editor:
        viewport.toggle_wireframe(model_editor)


if not __fg_toolsUIInitialized:
    __initialize()
