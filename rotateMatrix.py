#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:59:53 2018

@author: 1Air
"""
import numpy as np

def rotateMatrix(X):
    """
    rotates an NxN matrix 90 degrees clockwise
    input: matrix
    output: matrix
    """
    new_X = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            new_X[j][abs(i-3)] = X[i][j]
    return new_X.tolist()
            

# test
x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
y = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

result = rotateMatrix(x)
y == result