# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:06:11 2018

@author: Phoenix
"""

# Multiple Matches

import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

# Finding number of instances of pattern in text
for match in re.findall(pattern, text):
    print (f'Found {repr(match)}')
    