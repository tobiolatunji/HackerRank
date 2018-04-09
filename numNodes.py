#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:56:30 2018

@author: 1Air
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def numNodes(root):
    if not root:
        return 0
    return numNodes(root.left) + numNodes(root.right) + 1


# test case
three = Node(3)
five = Node(5)
one = Node(1)
four = Node(4)
two = Node(2)
six = Node(6)
zero = Node(0)
min1 = Node(-1)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)

three.left = two
three.right = five
two.left = one
five.left = four
five.right = six
one.left = zero
zero.left = min1


result = numNodes(three)
print (result)