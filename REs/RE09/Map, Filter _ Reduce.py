# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:20:19 2019

@author: Joana
"""
import functools
def reduce_map_filter(args):
    if type(args[2]) is tuple:
        if args[0] == "map":
            return list(map(args[1],reduce_map_filter(args[2])))
        elif args[0] == "filter":
            return list(filter(args[1],reduce_map_filter(args[2])))
        else:
            return functools.reduce(args[1],reduce_map_filter(args[2])) 
    if type(args[2]) is not tuple:
        if args[0] == "map":
            return list(map(args[1],args[2]))
        elif args[0] == "filter":
            return list(filter(args[1],args[2]))
        else:
            return functools.reduce(args[1],args[2])
