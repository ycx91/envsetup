# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:04:07 2018

@author: stamfordyao
"""

import re

file = r"C:\Users\stamfordyao\Desktop\html20180921.txt"

with open(file, "r+") as f:
    output = []
    lines = f.readlines()
    for line in lines:
        if re.match(r'^\s*$', line):
            continue
        if "\"" in line:
            zy = line.index("\"")
#            print (zy)
            line = line[:zy]
#            print (line)
            output.append(line)
        else:
            if line.strip('\n') != '':
                print (line)
                output.append(line)
    f.seek(0)
    f.truncate()
    for line in output:
        f.write(f'{line}\n')