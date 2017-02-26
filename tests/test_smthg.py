'''
Created on 14.06.2016

:author: Fabian
'''
import unittest

import start
start.initializeMayaPy()

import maya.cmds as cmds


class TestNumberTwo(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMet1(self):
        print cmds.polySphere()
        self.assertEqual(1, 2, "msg")

if __name__ == '__main__':
    unittest.main()