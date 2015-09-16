# -*- coding: utf-8 -*-
from random import *
from os import system


HEADER = '\033[95m'
OKBLUE = '\033[31m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
"""
Created on Fri Sep 11 14:48:16 2015

@author: Dane
"""

def add_padd2(x):
    if x <10:
        return '0' + str(x)
    else:
        return ''  + str(x)
    
def add_padd(x):
    if x <10:
        return ' 0' + str(x)
    elif x <100:
        return ' '  + str(x)
    else:
        return str(100)
def print_board(board, players):
    for x in range(10):    
        print "_____ "*10
        s = x*10
        e = x*10+10
        board2 = []
        board2 += board[s:e]
        for y in range(2):
            b = (99 - players[y]+1)
            if b in range(s,e):
                a = b%10
                if y == 0:
                    board2[a] = "A/-"
                else:
                    if players[0] == players[1]:
                        board2[a] = board2[a][:-1] +"B"
                    else:
                        board2[a] = "-/B"
                    
        if x%2 == 0:
            
            print " " + " | ".join(board2)
        else:
            print " " + " | ".join(board2[::-1])

    print OKBLUE + "_____ "*10 + ENDC
    

def shuffle():
    return randint(1, 6)


def play(players, p_num, moves, board):
    if players[p_num] + moves > 100:
        return "Need 100 to win. No more"
    else:    
        players[p_num] += moves
        if players[p_num] == 100:
            return "Player " + str(p_num+1) + " rolled " + str(moves) + " to win."
        ttest = board[players[p_num]]
        if not ttest.isdigit():
            if ttest[0] == 'v' or ttest[0] == '^':
                players[p_num] = int(ttest[1:])
                if ttest[0] == 'v':
                    return "Player " + str(p_num+1) +" hit Snake to " + ttest[1:]
                else:
                    return "Player " + str(p_num+1) + " took ladder to " + ttest[1:]
            
        return "Player " + str(p_num+1) + " rolled " + str(moves)
    
def add_snakes_ladders(board):
    used = []
    for x in range(6):
        while(1):
            a = randint(10,99) 
            if a not in used:
                break
        while(1):
            b = randint(1, a-1)
            if b not in used:
                break
        while(1):
            c = randint(5, 90)
            if c not in used:
                break
        while(1):
            d = randint(c, 99)
            if d not in used:
                break
        used += [a,b,c,d]
        board[a-1] = 'v' + add_padd2(b)
        board[c-1] = '^' + add_padd2(d)
    return board
    
        

def game(board, players):
    count = 0
    move = 0
    z = ""
    add_snakes_ladders(board)
    while(max(players) < 100):    
        print_board(board[::-1], players)
        a =count%2
        print z
        for x in range(2):
            print "Player " + str( x+1) + " : " + str(players[x])
        y = raw_input("Player " + str(a +1) + ". Press Enter key.")
        move = shuffle()
        z =play(players, count%2, move, board)
        if max(players) == 100:
            break
        system('cls')
        count += 1
    system('cls')
    print_board(board[::-1], players)
    print z
    
    
board = [add_padd(x) for x in range(1,101)]
players = [1,1]

  
        