# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:42:01 2019

@author: Joana
"""

def number_of_collisions(objects):
    count = 0
    for e in objects:
        i = objects.index(e)
        x1 = set(range(e["x1"],e["x2"]+1))
        y1 = set(range(e["y1"],e["y2"]+1))
        for f  in objects:
            if objects.index(f) > i:
                x2 = set(range(f["x1"],f["x2"]+1))
                y2 = set(range(f["y1"],f["y2"]+1))
                if list(x1 & x2) != [] and list(y1 & y2) != []:
                    count += 1

    return count

print(number_of_collisions([{'x1': 11, 'y1': 192, 'x2': 59, 'y2': 280}, {'x1': 546, 'y1': 564, 'x2': 629, 'y2': 580}, {'x1': 368, 'y1': 418, 'x2': 455, 'y2': 432}, {'x1': 479, 'y1': 506, 'x2': 577, 'y2': 521}, {'x1': 113, 'y1': 315, 'x2': 156, 'y2': 415}, {'x1': 513, 'y1': 40, 'x2': 537, 'y2': 119}, {'x1': 521, 'y1': 488, 'x2': 549, 'y2': 522}, {'x1': 72, 'y1': 295, 'x2': 122, 'y2': 343}, {'x1': 87, 'y1': 160, 'x2': 135, 'y2': 213}, {'x1': 495, 'y1': 304, 'x2': 524, 'y2': 339}]))        
