# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:33:56 2018

@author: Phoenix
"""

import re

def test_patterns(text, patterns):
    '''Given source text and a list of patterns, look for
    matches for each pattern within the text and print 
    them to stdout.
    '''
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print (f"'{pattern}' ({desc})\n")
        print (f"  '{text}'")
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_bslash = text[:s].count('\\')
            prefix = '.' * (s + n_bslash)
            print (f"  {prefix}'{substr}'")
        print ()
    return

# Edit the pattern ab given here to see the change, each . 
# is a count of the number of chars leading up to the pattern
if __name__ == "__main__":
    test_patterns('abbaaabbbbaaaaa', 
                  [('ab', "'a' followed by 'b'")])
