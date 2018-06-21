# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:10:22 2018

@author: Phoenix
"""

#Finding Pattern Location

import re

pattern = 'this'
text = 'Does thi text match this pattern?'

match = re.search(pattern, text) #only for the first pattern found
s = match.start() #gives the starting position of the matched text
e = match.end() #gives the ending position of the matched text
print (f'Started at {s}')
print (f'Ended at {e}')
print (f'Pattern is: {match.re.pattern}')
print (f'String is: {match.string}')
print (f'Found "{match.re.pattern}"\nin "{match.string} from {s} to {e} ("{text[s:e]}")')

