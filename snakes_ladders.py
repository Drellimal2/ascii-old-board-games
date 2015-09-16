# -*- coding: utf-8 -*-
from random import *
from os import system


BLACK = '\033[0;30m'
SNAKES = '\033[1;43m'
F_WHITE = '\033[37m'
B_T_GREEN = '\033[1;42m'
B_L_GREEN = '\033[42m'
WINNING = '\033[1;45m\033[1;37m'
LADDERS = '\033[1;46m'
P1 = '\033[1;41m' + F_WHITE
P2 = '\033[1;44m' + F_WHITE


ENDC = '\033[0m'

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
        return B_L_GREEN + F_WHITE + '  0' + str(x) + ' ' + ENDC
    elif x <100:
        return B_L_GREEN + F_WHITE+'  '  + str(x) + ' ' + ENDC
    else:
        return WINNING + ' '+ str(100)+ ' ' + ENDC


def print_board(board, players):
    print (B_T_GREEN + "_____"+ ENDC + " ") *10

    for x in range(10):    
        # print (B_L_GREEN + "_____"+ ENDC + " ") *10
        s = x*10
        e = x*10+10
        board2 = []
        board4 = []
        b_h = bottom_halves[::-1]
        board4 += b_h[s:e]
        board2 += board[s:e]
        for y in range(2):
            b = (99 - players[y]+1)
            if b in range(s,e):
                a = b%10
                if y == 0:
                    board2[a] = P1 +" A" + "   " + ENDC
                    board4[a] = P1 + "_____"+ ENDC + " "
                else:
                    if players[0] == players[1]:
                        board2[a] = board2[a][:-6] + ENDC + P2 +"B "+ENDC
                        board4[a] = board4[a][:-7] + ENDC + P2 +"__"+ENDC + " "
                    else:
                        board2[a] =  P2 + "   " +  "B " + ENDC
                        board4[a] = P2 + "_____"+ ENDC + " "
                    
        if x%2 == 0:
            print   "|".join(board2)
            print   "".join(board4)

        else:
            print  "|".join(board2[::-1])
            print   "".join(board4[::-1])


    

def shuffle():
    return randint(1, 6)


def play(players, p_num, moves, board):
    if players[p_num] + moves > 100:
        return "Need 100 to win. No more"
    else:    
        players[p_num] += moves
        if players[p_num] == 100:
            return "Player " + str(p_num+1) + " rolled " + str(moves) + " to win."
        ttest = board[players[p_num]-1]
        if not ttest.isdigit():
            if ttest[7:9] == ' v' or ttest[7:9] == ' ^':
                players[p_num] = int(ttest[-7:-5])
                if ttest[7:9] == ' v':
                    return "Player " + str(p_num+1) + " rolled " + str(moves) +  " and hit Snake to " + ttest[-7:-5]
                else:
                    return "Player " + str(p_num+1) + " rolled " + str(moves) +  " and took ladder to " + ttest[-7:-5]
            
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
        board[a-1] = SNAKES +' v' + add_padd2(b) + ' ' + ENDC
        bottom_halves[a-1] = SNAKES + "_____"+ ENDC + " "
        board[c-1] = LADDERS + ' ^' + add_padd2(d) + ' ' + ENDC
        bottom_halves[c-1] = LADDERS + "_____"+ ENDC + " "        
    return board
    
        

def game(board, players):
    system('cls')
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
bottom_halves = [(B_L_GREEN + "_____"+ ENDC + " ") for x in range(100)]
bottom_halves[99] = WINNING + "_____"+ ENDC + " "
players = [1,1]

  
        