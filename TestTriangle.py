# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInput1(self):
        self.assertEqual(classifyTriangle(13,12,5),'Right')

    def testInput2(self):
        self.assertEqual(classifyTriangle(5,3,4), 'InvalidInput')

    def testInput3(self):
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral')

    def testInput4(self):
        self.assertEqual(classifyTriangle(3,3,2), 'Isoceles')

    def testInput5(self):
        self.assertEqual(classifyTriangle(0,0,200), 'InvalidInput')

    def testInput6(self):
        self.assertEqual(classifyTriangle(3,4,5), 'Right')

    def testInput7(self):
        self.assertEqual(classifyTriangle(5,7,5), 'Isoceles')

    def testInput8(self):
        self.assertEqual(classifyTriangle(6,6,6), 'Equilateral')

    def testInput9(self):
        self.assertEqual(classifyTriangle(2,2,3), 'Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

