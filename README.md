# FC Tools

This is a collection of some handy (modeling-) tools in Maya.
After installation you will get a small extra menu ("FC Tools") where you can find all available commands.
You can assign hot-keys to them if you want to.

## Installation
* Clone this repository to your local harddrive.
* Open Maya and execute this script in the scripteditor:

  ```python
  import sys
  fcToolPath = "X:/PATH/TO/FC-Tools/scripts"

  if fcToolPath not in sys.path:
      sys.path.append(fcToolPath)

  import fc_tools
  fc_tools.createMenu()
  ```
* Thats's it! :)

I recommend to put this in a shelf button or in the userSetup.py.
Also note that this is save to execute in batch-mode. The UI creation simply be skipped in that case.

Supported Platforms: **Windows**

Supported Maya Versions: **2015, 2016, 2017**

Author: [**Fabian Czichelski**](http://hub.morroimages.com/display/~f.czichelski)

Use at you own risk! Awesomeness not guaranteed (but likely ;) )!
