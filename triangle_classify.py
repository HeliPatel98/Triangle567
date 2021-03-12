# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""
import math

def classify_triangle(a_side, b_side, c_side):

    """Check that series of values form a triangle"""

    return_str = ""

    non_zero = (a_side <= 0 or b_side <= 0 or c_side <= 0)
    sides_compared = sides_comp(a_side,b_side,c_side)
    max_triangle = over_max(a_side, b_side, c_side)

    if non_zero or max_triangle or sides_compared:
        return_str += "Invalid Triangle"
    elif a_side == b_side and b_side == a_side and a_side == c_side:
        return_str += "Equilateral"
    elif math.isclose((a_side ** 2) + (b_side ** 2) , (c_side ** 2)):
        if scalene_triangle(a_side,b_side,c_side):
            return_str += "right and scalene"
        elif isoceles_triangle(a_side,b_side,c_side):
            return_str += "right and isoceles"
        else:
            return_str += "Right"
    elif scalene_triangle(a_side,b_side,c_side):
        return_str += "Scalene"
    else:
        return_str += "Isoceles"
    return return_str

def over_max(a_side,b_side,c_side):
    """Check if any side is greater than 200"""
    return (a_side > 200) or (b_side > 200) or (c_side > 200)

def sides_comp(a_side, b_side, c_side):
    """check if one side is greater than other two"""
    greater_a = (a_side > (b_side + c_side))
    greater_b = (b_side > (a_side + c_side))
    greater_c = (c_side > (a_side + b_side ))
    return greater_a or greater_b or greater_c

def scalene_triangle(a_side, b_side, c_side):
    """check if the triangle is scalene or not"""
    return (a_side != b_side) and (b_side != c_side ) and (a_side != c_side)

def isoceles_triangle(a_side, b_side, c_side):
    """check if the triangle is isoceles or not"""
    return (a_side == b_side) or (a_side == c_side) or (b_side == c_side)
