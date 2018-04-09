#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:15:48 2018

@author: 1Air
"""

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def insert(self,val):
        if self.left is None:
            self.left = Node(val)
        elif self.right is None:
            self.right = Node(val)
        else:
            self.insert(self.left.left, val)


def balancedTree(lst):
    """
    create a binary tree from list with minimum height
    """
    if not lst:
        return
    mid = len(lst)//2
    root = Node(lst[mid])
    root.left = balancedTree(lst[:mid])
    root.right = balancedTree(lst[mid+1:])
    return root

lst = [-1,0,1,2,3,4,5,6]
result = balancedTree(lst)
print (result)

result.right.left.val

   

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




