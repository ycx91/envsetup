# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:40:53 2018

@author: Phoenix
"""

a = 0.1
b = 0.2
'''swap the values of objects a and b without using another variable name'''
a = a + b
b = a - b
a = a - b

print (a + b)