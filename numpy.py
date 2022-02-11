#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 00:27:41 2021

@author: cenkakdeniz
"""
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array.shape)

a = array.reshape(3,5)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.size)
#%%numpy basic aps
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

print(a*b)

print(a.dot(b.T))
#%%
array = np.array([1,2,3,4,5,6,7])
print(array[::-1])
array1 = ([1,2,3],[4,5,6])
#%%
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
#flatten
a= array.ravel()
array2 = a.reshape(3,3)
#%% convert and copy
lst = [1,2,3,4]
array = np.array([5,6,7,8])

listToArray = np.array(lst)
arrayToList = list(array)

print(type(listToArray))
print(type(arrayToList))