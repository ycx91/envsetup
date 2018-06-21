# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 02:18:57 2018

@author: Phoenix
"""

# Introducing meta-characters here for re: * , + , ? , {d:d}

import re_test_patterns as retp

'''When processing a repetition instruction, re will usually 
consume as much of the input as possible while matching the 
pattern. This so-called greedy behavior may result in fewer 
individual matches, or the matches may include more of the 
input text than intended. Greediness can be turned off by 
following the repetition instruction with ?.
'''
retp.test_patterns('abbaabbba',
                   [('ab*', 'a followed by zero or more b'),
                    ('ab+', 'a followed by one or more b'),
                    ('ab?', 'a followed by zero or one b'),
                    ('ab{3}', 'a followed by three b'),
                    ('ab{2,3}', 'a followed by two to three b'),
                    ('ab{2}?', 'a followed by two b and wildcard'),
                    ('ab', 'ab only')])

# Use ? at the end of the pattern to turn off greediness