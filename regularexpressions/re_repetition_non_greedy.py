# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:13:05 2018

@author: Phoenix
"""

import re_test_patterns as rtp

rtp.test_patterns(
        'abbaabba',
        [('ab*?', '1'),
         ('ab+?', '2'),
         ('ab??', '3'),
         ('ab{3}?', '4'),
         ('ab{2,3}?', '5')])