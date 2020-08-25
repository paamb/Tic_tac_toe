import numpy as np
import math
board = [['_','_','_'],['_','_','_'],['_','_','_']]
rewards = [1,0,-1]
move_counter = 0

def print_board(board):
        for i in range (len(board)):
            if i != 0:
                print("\n","- - - - -")
            for j in range (len(board)):
                if j != 0:
                    print(" | ", end="")
                print(board[i][j], end="")

def make_a_move(row, col, player, move_counter, board):
    print("hallqa")
    row = int(row)
    col = int(col)
    if board[row][col] == '_':
        board[row][col] = player
        move_counter += 1
    else:
        print("Feltet er tatt velg et annet")
    return board, move_counter

def game_end(board, player):
    #Checking horisontals
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    #Checking verticals
    for i in range (len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    #Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
       
    return False

def play_without_ai(move_counter):
    print_board(board)
    if move_counter%2:
        print("\n\n")
        row, col= input("Skriv inn trekk: ").split()
        player = 'O'
        move_counter = make_a_move(row, col, player, move_counter, board)
    else:
        print("\n\n")
        row, col= input("Skriv inn trekk: ").split()
        player = 'X'
        move_counter = make_a_move(row, col, player, move_counter, board)
    if game_end(board, player) == False:
        play_without_ai(move_counter)
    else:
        if player == 'X':
            print("vant!")
        else:
            print("vant! jeg")                                                                                                         