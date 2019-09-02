#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment1_Part1
"""

class Book():
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        """Function that prints book info"""
        print(self.title + ", written by " + self.author)

"""Example objects of function display"""  
n = Book('John Steinbeck', 'Of Mice and Men')
m = Book('Harper Lee', 'To Kill a Mockingbird')

n.display()
m.display()
