'''
Created on 12.06.2016

:author: Fabian
'''
import unittest
import start
import maya.cmds as cmds


class Test(unittest.TestCase):

    def testBasic(self):
        print cmds.polySphere()
        self.assertEqual(1, 1, "Much Problem")
