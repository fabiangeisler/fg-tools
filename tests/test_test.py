'''
'''
import unittest

import start
start.initializeMayaPy()

import maya.cmds as cmds


class Test(unittest.TestCase):

    def testBasic(self):
        print cmds.polySphere()
        self.assertEqual(1, 1, "Much Problem")
