# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:35:48 2019

@author: Joana
"""

def move_ball(board):
    pos = []
    fin = []
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == "E" or board[i][k] == "N" or board[i][k] == "W" or board[i][k] == "S":
                pos = (i, k)
                break
        if pos == (i, k):
            break
    direc = board[i][k]
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == "X":
                fin = (i, k)
                break
        if fin == (i, k):
            break
    res = [pos]
    while pos != fin:
        print(pos)
        (y, x) = pos
        if board[y][x] != "\\" and board[y][x] != "/" and direc == "W":
            x = x - 1
            pos = (y, x)
            res.append(pos)
            continue
        elif board[y][x] == "\\" and direc == "W":
            y = y - 1
            pos = (y, x)
            direc = "N"
            res.append(pos)
            continue
        elif board[y][x] == "/" and direc == "W":
            y = y + 1
            pos = (y, x)
            direc = "S"
            res.append(pos)
            continue

        if board[y][x] != "\\" and board[y][x] != "/" and direc == "E":
            x = x + 1
            pos = (y, x)
            res.append(pos)
            continue
        elif board[y][x] == "\\" and direc == "E":
            y = y + 1
            pos = (y, x)
            direc = "S"
            res.append(pos)
            continue
        elif board[y][x] == "/" and direc == "E":
            y = y - 1
            pos = (y, x)
            direc = "N"
            res.append(pos)
            continue
        if board[y][x] != "\\" and board[y][x] != "/" and direc == "S":
            y = y + 1
            pos = (y, x)
            res.append(pos)
            continue
        elif board[y][x] == "\\" and direc == "S":
            x = x + 1
            pos = (y, x)
            direc = "E"
            res.append(pos)
            continue
        elif board[y][x] == "/" and direc == "S":
            x = x - 1
            pos = (y, x)
            direc = "W"
            res.append(pos)
            continue

        if board[y][x] != "\\" and board[y][x] != "/" and direc == "N":
            y = y - 1
            pos = (y, x)
            res.append(pos)
            continue
        elif board[y][x] == "\\" and direc == "N":
            x = x - 1
            pos = (y, x)
            direc = "W"
            res.append(pos)
            continue
        elif board[y][x] == "/" and direc == "N":
            x = x + 1
            pos = (y, x)
            direc = "E"
            res.append(pos)
            continue

    return res