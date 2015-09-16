# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:22:25 2015

@author: Dane
"""
from os import system

BLACK = '\033[0;40m'
WHITE = '\033[1;47m'
T_WHITE = '\033[1;37m'
BLUE = '\033[1;44m'
GREEN = '\033[1;42m'
ENDC = '\033[0m'


def add_padd(x):
    if x <10:
        return '00' + str(x) 
    else:
        return '0'  + str(x) 

def change_color(pos, col):
    if col == 1:
        COLOR = WHITE
        TEXT = T_WHITE + ' 1 '
    else:
        COLOR = BLACK
        TEXT = ' 0 '
    board[pos] = COLOR + TEXT + ENDC
    b_h[pos] = COLOR + "___" + ENDC

board = [(BLUE +add_padd(x) +ENDC) for x in range(64)]
b_h = [(BLUE +"___"+ENDC) for x in range(64)]
change_color(27, 1)
change_color(28,0)
change_color(35, 0)
change_color(36,1)


def check_hori(pos, col, s, e):
    left  = []
    right = []
    l_pos = 0
    r_pos = 0
    r_pos += pos + 1
    l_pos += pos -1
    
    op_col = (col+1)%2
    while l_pos >= s:
        if board[l_pos][-7] == "0":
            break
        elif int(board[l_pos][-7:-4]) == col:
            if left == []:
                print "Failed Left"
            else:
                change_color(pos, col)
                for y in left:
                    change_color(y, col)
            break
        
        elif int(board[l_pos][-7:-4]) == op_col:
            left += [l_pos]
            l_pos -=1
        else:
            break
    while r_pos <= e:
        if board[r_pos][-7] == "0":
            break
        elif int(board[r_pos][-7:-4]) == col:
            if right == []:
                print "Failed Right"
            else:
                change_color(pos, col)
                for y in right:
                    change_color(y, col)
            break
        
        elif int(board[r_pos][-7:-4]) == op_col:
            right += [r_pos]
            r_pos +=1
        else:
            break
    return 5
    
def check_verti(pos, col, s, e):
    top  = []
    bot = []
    t_pos = 0
    b_pos = 0
    t_pos += pos - 8
    b_pos += pos + 8
    
    op_col = (col+1)%2
    while t_pos >= s:
        if board[t_pos][-7] == "0":
            break
        if int(board[t_pos][-7:-4]) == col:
            if top == []:
                print "Failed Left"
            else:
                change_color(pos, col)
                for y in top:
                    change_color(y, col)
            break
        
        elif int(board[t_pos][-7:-4]) == op_col:
            top += [t_pos]
            t_pos -= 8
        else:
            break            
            
    while b_pos <= e:
        if board[b_pos][-7] == "0":
            break
        if int(board[b_pos][-7:-4]) == col:
            if bot == []:
                print "Failed Right"
            else:
                change_color(pos, col)
                for y in bot:
                    change_color(y, col)
            break
        
        if int(board[b_pos][-7:-4]) == op_col:
            bot += [b_pos]
            b_pos +=8
        else:
            break
    return 5
            
def play(pos, player):
    check_hori(pos, player,pos- (pos%8),  pos- (pos%8)+8)
    check_verti(pos, player, pos%8, 56 + pos%8)
    

    
nums_board = [add_padd(x) for x in range(64)]

def print_board(board):

    for x in range(8):    
        # print (B_L_GREEN + "_____"+ ENDC + " ") *10
        s = x*8
        e = x*8+8
        board2 = []
        board4 = []

        board4 += b_h[s:e]
        board2 += board[s:e]
        print   (BLUE+"|"+ENDC).join(board2) 
        print   (BLUE+"|"+ENDC).join(board4)

def game(board):
    system('cls')
    print_board(board)
    player = 0
    for x in range(60):
        y = raw_input("Player " + str(player+1) +"select tile:")
        play(int(y), player)
        player = (player+1)%2
        system('cls')
        print_board(board)