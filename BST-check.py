#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:34:38 2018

@author: 1Air
"""

class BinaryNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
           

def inOrderTraversal(root, tree):
    if not root:
        return tree
    
    inOrderTraversal(root.left, tree)
    tree.append(root.data)
    inOrderTraversal(root.right, tree)
    return tree

def inOrderTraversaly(root):
    tree = []
    if not root:
        return tree
    tree.extend(inOrderTraversaly(root.left))
    tree.append(root.data)
    tree.extend(inOrderTraversaly(root.right))
    return tree

def inOrderTraversalx(root):
    if not root:
        return []
    tree = list()
    tree.extend(inOrderTraversalx(root.left))
    tree.append(root.data)
    tree.extend(inOrderTraversalx(root.right))
    return tree


three = BinaryNode(3)
five = BinaryNode(5)
one = BinaryNode(1)
four = BinaryNode(4)
two = BinaryNode(2)
six = BinaryNode(6)


three.left = two
three.right = five
two.left = one
five.left = four
five.right = six

tree = []
result = inOrderTraversaly(three)
print (result)