# -*- coding: utf-8 -*-
"""
Write a script that given an hour and minutes by user input, prints at what time the alarm clock will ring, knowing that the current hour is hour and the current minutes are minutes. The clock goes off after 6 hour and 51 minutes.
"""

import math
h = int(input())
min = int(input())


h = h + 6
min = min + 51
h_overflow = int(h / 24)
h_n_overflow = 1 - h_overflow
min_overflow = int(min / 60)
min_n_overflow = 1 - min_overflow
min_f = min_overflow * (min - 60) + min_n_overflow * min
h_f = (h_overflow * (h - 24) + h_n_overflow * h) + min_overflow * 1
print(str(h_f).zfill(2) + ":" + str(min_f).zfill(2))
