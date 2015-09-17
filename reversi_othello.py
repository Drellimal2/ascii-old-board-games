# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:22:25 2015

@author: Dane
"""
from os import system

BLACK = '\033[0;40m'
WHITE = '\033[1;47m'
T_WHITE = '\033[1;37m'
BLUE = '\033[1;46m'
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
    result = 0
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
                result += len(left)
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
                result += len(right)
            break
        
        elif int(board[r_pos][-7:-4]) == op_col:
            right += [r_pos]
            r_pos +=1
        else:
            break
    return result

def get_player(col):
    if col == 1:
        return WHITE + T_WHITE +" 1 " +ENDC
    else:
        return BLACK + " 0 " + ENDC

def check_diag(pos, col):
    result = 0
    t_edge = [x for x in range(8)]
    b_edge = [x for x in range(56,64)] 
    l_edge = [x for x in range(8,49,8)]
    r_edge = [x for x in range(15,56,8)]
    changed = []
    op_col = (col+1)%2

    npos = 0
    npos += pos
    npos -= 9
    if pos not in (t_edge +l_edge):
        while npos not in (t_edge + l_edge):
            if board[npos][-7] == "0":
                break
            elif int(board[npos][-7:-4]) == col:
                if changed == []:
                    break
                else:
                    change_color(pos, col)
                    for y in changed:
                        change_color(y, col)
                    result += len(changed)
                    changed = []

                break
            
            elif int(board[npos][-7:-4]) == op_col:
                changed += [npos]
                npos -=9
            else:
                break
    npos = 0
    npos += pos
    npos += 9
    if pos not in (b_edge +r_edge):
        while npos not in (b_edge + r_edge):
            if board[npos][-7] == "0":
                break
            elif int(board[npos][-7:-4]) == col:
                if changed == []:
                    break
                else:
                    change_color(pos, col)
                    for y in changed:
                        change_color(y, col)
                    result += len(changed)
                    changed = []
                break
            
            elif int(board[npos][-7:-4]) == op_col:
                changed += [npos]
                npos +=9
            else:
                break
    npos = 0
    npos += pos
    npos -= 7
    if pos not in (t_edge +r_edge):
        while npos not in (t_edge + r_edge):
            if board[npos][-7] == "0":
                break
            elif int(board[npos][-7:-4]) == col:
                if changed == []:
                    break
                else:
                    change_color(pos, col)
                    for y in changed:
                        change_color(y, col)
                    result += len(changed)
                    changed = []

                break
            
            elif int(board[npos][-7:-4]) == op_col:
                changed += [npos]
                npos -=7
            else:
                break
    npos = 0
    npos += pos
    npos += 7
    if pos not in (b_edge +l_edge):
        while npos not in (b_edge + l_edge):
            if board[npos][-7] == "0":
                break
            elif int(board[npos][-7:-4]) == col:
                if changed == []:
                    break
                else:
                    change_color(pos, col)
                    for y in changed:
                        change_color(y, col)
                    result += len(changed)
                    changed = []

                break
            
            elif int(board[npos][-7:-4]) == op_col:
                changed += [npos]
                npos +=7
            else:
                break
    return result
            
def check_verti(pos, col, s, e):
    result = 0
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
                result += len(top)
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
                result += len(bot)
            break
        
        if int(board[b_pos][-7:-4]) == op_col:
            bot += [b_pos]
            b_pos +=8
        else:
            break
    return result
            
def play(pos, player):
    a = check_hori(pos, player,pos- (pos%8),  pos- (pos%8)+8)
    b = check_verti(pos, player, pos%8, 56 + pos%8)
    c = check_diag(pos, player)
    
    return a+b+c 

    
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

players = [2,2]

def game(board):
    system('cls')
    print_board(board)
    player = 0
    for x in range(60):
        while(1):
            print players
            y = raw_input("|" +get_player(player) +"| select tile:")
            z = play(int(y), player)
            print z
            if z > 0:
                players[player] += z +1
                players[(player+1)%2] -= z
                break
            else:
                system('cls')
                print_board(board)
                print "Select Valid Position"
        
        player = (player+1)%2
        if players[player] == 0:
            player = (player+1)%2
            print "|" +get_player(player) +"| wins" 
        system('cls')
        
        print_board(board)
        print z
