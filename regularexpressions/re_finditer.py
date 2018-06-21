# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:09:05 2018

@author: Phoenix
"""

# Multiple Matches

import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

matchdict = {}
count = 0
matchlist = []
# Find multiple occurrences of pattern in text and other key info
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    count += 1
    matchdict[text[s:e] + str(count)] = f'{s}:{e}'
    matchlist.append([count, text[s:e], s, e])
    print (f'Found {text[s:e]} at {s}:{e}')
print (matchdict)
print (matchlist)
    