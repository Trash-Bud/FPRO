# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:36:46 2019
x1x
0o2 
xoo
@author: Joana
"""
def tic_tac_toe(board, player):
    h = []
    count = 0
    board = board.split("\n")
    diagonals = [[("A1", board[0][0]),("B2", board[1][1]),("C3", board[2][2])],[("A3", board[0][2]),("B2", board[1][1]),("C1", board[2][0])]]
    dic = {0:"A",1:"B",2:"C"}
    for i in board:
        if i.count(player) == 2 and " " in i:
            n = i.index(" ") + 1
            l = dic[board.index(i)]
            return l + str(n)
    for i in range(len(board)):
        for e in board:
            h.append(e[i]) 
            h.append(dic[board.index(e)] + str(i + 1))
        if h.count(player) == 2 and " " in h:
            return h[h.index(" ") + 1]
        else: 
            h = []
            continue
    for d in diagonals:
        for f in range(3):
            if d[f][1] == player:
                count += 1
            elif d[f][1] == " ":
                r = d[f][0]
        if count == 2:
            return r
        else:
            count = 0
            