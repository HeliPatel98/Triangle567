# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math


from triangle_classify import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInput1(self):
        self.assertEqual(classify_triangle(0, 1, 2), 'Invalid Triangle')

    def testInput2(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'Invalid Triangle')

    def testInput3(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def testInput4(self):
        self.assertEqual(classify_triangle(2, 3, 3), 'Isoceles')

    def testInput5(self):
        self.assertEqual(classify_triangle(0, 0, 200), 'Invalid Triangle')

    def testInput6(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'right and scalene')

    def testInput7(self):
        self.assertEqual(classify_triangle(5, 7, 5), 'Isoceles')

    def testInput8(self):
        self.assertEqual(classify_triangle(6, 6, 6), 'Equilateral')

    def testInput9(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isoceles')

    def testInput10(self):
        self.assertEqual(classify_triangle(15, 20, 25), 'right and scalene')

    def testInput11(self):
        self.assertEqual(classify_triangle(7, 7, 7 * math.sqrt(2)), 'right and isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

