# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:28:51 2018

@author: Phoenix
"""

#Compiling Expressions

import re
import pprint as pp

regexes = [
        re.compile(p)
        for p in ['this','that']]
text = 'Does this text match the pattern?'
#print (f'TextA: {text!a}') #ascii
#print (f'Text1: {ascii(text)}')
#print (f'TextR: {text!r}') #repr
#print (f'Text2: {repr(text)}')
#print (f'TextS: {text!s}') #str
#print (f'Text3: {str(text)}')
#pp.pprint (f'TextP: {text!a}')

for regex in regexes:
    print (f'Seeking "{regex.pattern}" ->', end=' ')
    if regex.search(text):
        print ('match!')
    else:
        print ('no match!')
