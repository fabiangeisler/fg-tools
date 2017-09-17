# FG-Tools

This is a collection of some handy (modeling-) tools in Maya.
After installation you will get a small extra menu ("FG-Tools") where you can find all available commands.
You can assign hot-keys to them if you want to.

## Installation
* Clone this repository to your local hard-drive.
* Open Maya and execute this script in the script-editor:

  ```python
  import fg_tools
  fg_tools.create_menu()
  ```
* That's it! :)

I recommend to put this in a shelf button or in the userSetup.py.
Also note that this is save to execute in batch-mode. The UI creation simply be skipped in that case.

Supported Platforms: **Windows**

Supported Maya Versions: **2015, 2016, 2017**

Author: [**Fabian Czichelski**](http://hub.morroimages.com/display/~f.czichelski)

Use at you own risk! Awesomeness not guaranteed (but likely ;) )!
