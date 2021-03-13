# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest


from triangle_classify import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInput1(self):
        self.assertEqual(classify_triangle(0,1,2), 'NotATriangle')

    def testInput2(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'NotATriangle')

    def testInput3(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def testInput4(self):
        self.assertEqual(classify_triangle(2,3,2), 'Isosceles')

    def testInput5(self):
        self.assertEqual(classify_triangle(0, 0, 200), 'NotATriangle')

    def testInput6(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def testInput7(self):
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')

    def testInput8(self):
        self.assertEqual(classify_triangle(6, 6, 6), 'Equilateral')

    def testInput9(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

