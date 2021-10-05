# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:53:04 2019

@author: Joana
"""

import datetime

x = datetime.datetime.now()
h = x.hour
min = x.minute

h = 8 + h
min = 30 + min

if min > 60:
    min = min - 60
    h = h + 1
elif min == 60:
    min = 0
    h = h + 1
else:
    min = min

if h > 24:
    h = h - 24
elif h == 24:
    h = 0
else:
    h = h

print(str(h).zfill(2) + ":" + str(min).zfill(2))