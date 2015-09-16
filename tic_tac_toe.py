# -*- coding: utf-8 -*-
import os 

"""
Created on Thu Sep 10 11:02:41 2015

@author: Dane
"""

def print_board(vals):
    count = 0     
    for x in vals:
        print " " + " | ".join(x) + " "
        if count <2:
            print "___ ___ ___"
            count +=1

def make_play(pos, player, board):
    x = (pos-1)%3
    y = (pos-1)/3 
    if board[y][x] == '-':    
        if player == 0:
            val = 'X'
        else:
            val = 'O'
        
        board[y][x] = val
        
        if check_win(board, player, x, y):
            return 2

        return 1
    else:
        print "Cannot make specified move"
        return 0

def check_cols(board, x):
    val = board[0][x]
    for y in board:
        if y[x] != val:
            return False
    return True
    
def check_row(board, y):
    val = board[y][0]
    for x in board[y]:
        if x != val:
            return False
    return True

def check_diag(board, x, y):
    if x ==  y and x == 1:
        one = True 
        two = True
        val1 = board[0][0]
        val2 = board[0][2]
        x1= 2
        y1=0
        for i in range(3):
            if board[x1-i][y1+i] != val2 and two:
                two = False
            if board[i][i] != val1 and one:
                one = False
        return one and two
    if x == y:
                
        val = board[0][0]
        for i in range(3):
            if board[i][i] != val:
                return False
        else:
            return True
    else:
        val = board[0][2]
        x1= 2
        y1=0
        for i in range(3):
            if board[x1-i][y1+i] != val:
                return False
        else:
            return True
            
        
def check_win(board, player, x, y):
    diags = [(0,0),(2,0),(1,1), (0,2), (2,2)]
    diag = False
    if (x,y) in diags:
        diag = check_diag(board,x,y)
    if diag or check_cols(board,x) or check_row(board, y):
        os.system('cls')
        print_board(board)
        print "Player " + str(player+1) + " wins!!"
        return True
    else:
        return False
        
def game():
    places = [[str(x*3 + y +1) for y in range(3)] for x in range(3)]
    print " "
    option = raw_input("Press N for new game \nPress I for instructions\nChoice:")
    if option.upper() == 'N':
        x = 0
        board = [['-' for y in range(3)] for x in range(3)]
        while(x <= 10):
            print_board(board)
            player = x%2
            play = raw_input("Player " + str(player+1)  +":")
            os.system('cls')

            valid = make_play(int(play), player, board)
            x += valid
            if valid == 2:
                break
            
    elif option.upper() == 'I':
        print_board(places)
        print "\nPlayers take turns placing X or O tryig to get 3 in a row."
        print "\nWhen promted select appropriate square corresponding to board above.\n\n"
        game()
    else:
        os.system('cls')
        print "\nPlease select a valid option.\n"
        game()
    if valid != 2:
        print "Draw!!!"
    if (raw_input("Do you want to play again? [Y/N]")).upper() == 'Y':
        os.system('cls')
        game()
game()
    


