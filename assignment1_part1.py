#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment1_Part1
"""

def listDivide(numbers, divide=2):
    """Function that returns the number of elements divisible by divide which is 2 by default """

    even = 0
    for number in numbers:
        if number % divide == 0:
            even += 1
    return even


class ListDivideException(Exception):
    pass

def testListDivide():
    """Test examples of listDivide function"""
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
    except:
        raise ListDivideException

testListDivide()
