# Fabian Czichelski's Personal Script Arsenal

This is a collection of some handy (modeling-) tools in maya. If you run the code
you will get a small extra menu with all available commands. All of these commands
are also available as runtimeCommands so you can assign hot-keys to it.

If you want to use these tools you must first clone this repository to your local
harddrive. After that you have to open Maya and ether execute this script in the
scripteditor.

```python
import sys
fcToolPath = "X:/PATH/TO/FC-Tools/scripts"

if fcToolPath not in sys.path:
    sys.path.append(fcToolPath)

import fcTools
fcTools.initialize()
```
I recommend to but this in a shelf button or in the userSetup.py.
Also note that this is save to execute in batchmode.

Supported Platforms: **Windows**

Supported Maya Versions: **2015, 2016, 2017**

Author: [**Fabian Czichelski**](http://hub.morroimages.com/display/~f.czichelski)

Use at you own risk! Awesomeness not guaranteed (but likely ;) )!
