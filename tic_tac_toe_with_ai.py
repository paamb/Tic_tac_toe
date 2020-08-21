import numpy as np
import math
board = [['_','_','_'],['_','_','_'],['_','_','_']]
rewards = [1,0,-1]
move_counter = 0
winning_boards = 0
losing_boards = 0
draw_boards = 0

ai = "X"
player = "O"
def start(move_counter):
    starting_player = input("Do you want to start (y/n)?")
    if starting_player == "y":
        move_counter = 0
    else:
        move_counter = 1
    play(move_counter)

def print_board(board):
        for i in range (len(board)):
            if i != 0:
                print("\n","- - - - -")
            for j in range (len(board)):
                if j != 0:
                    print(" | ", end="")
                print(board[i][j], end="")

def make_a_move(row, col, player, move_counter):
    row = int(row)
    col = int(col)
    if board[row][col] == '_':
        board[row][col] = player
        move_counter += 1
    else:
        print("Feltet er tatt velg et annet")
    return move_counter

def mini_max_scoring(board, player):
    #Checking horisontals
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            if player == "X":
                return 10
            if player == "O":
                return -10
    #Checking verticals
    for i in range (len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
            if player == "X":
                return 10
            if player == "O":
                return -10
    #Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        if player == "X":
            return 10
        if player == "O":
            return -10
    if board[0][2] == board[1][1] == board[2][0] == player:
        if player == "X":
            return 10
        if player == "O":
            return -10
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return None
    return 0

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

def play(move_counter):
    print_board(board)
    if move_counter%2:
        print("\n\n\n")
        row, col= input("Skriv inn trekk: ").split()
        player = 'O'
        move_counter = make_a_move(row, col, player, move_counter)
    else:
        print("\n\n\n")
        row, col = best_ai_move(board)
        player = "X"
        board[row][col] = player 
        move_counter += 1
    if game_end(board, player) == False:
        play(move_counter)
    else:
        print_board(board)
        print("\n")
        print("GAME OVER")

def best_ai_move(board):
    best_move_score = -math.inf
    losing_boards = int(0)
    winning_boards = int(0)
    draw_boards = int(0)
    different_outcomes = [winning_boards, draw_boards, losing_boards]
    best_move_x = -1
    best_move_y = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                player = "X"
                value_of_move = mini_max(board, 0, False, player, different_outcomes)                    
                board[i][j] = "_"
                if best_move_score < value_of_move:
                    best_move_score = value_of_move
                    best_move_x = i
                    best_move_y = j
    if best_move_score == 10:
        print("AI says: 'Imagine playing this bad'")
    elif best_move_score == 0:
        print("AI says: 'Okay good move sir'")
    elif best_ai_move == -10:
        print("AI says: 'Do you cheat?'")
    return (best_move_x, best_move_y)

def mini_max(pos, depth, maximizing_player, player, different_outcomes):
    score = mini_max_scoring(board, player)
    if score is not None:
        if score == 10:
            different_outcomes[0] += 1
        if score == -10:
            different_outcomes[2] += 1
        if score == 0:
            different_outcomes[1] += 1
        return score
    if maximizing_player:
        best_val = -(math.inf)
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    player = "X"
                    board[i][j] = "X"
                    value = mini_max(board, depth +1, False, player, different_outcomes)
                    board[i][j] = "_"
                    best_val = max(best_val, value)
        return best_val
    else:
        best_val = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    player = "O"
                    board[i][j] = "O"
                    value = mini_max(board, depth +1, True, player, different_outcomes)
                    board[i][j] = "_"
                    best_val = min(best_val, value)
        return best_val                                                                                                        

start(move_counter)


#Viser for den over. Og viser for alle verdier og ikke de verdiene som er de beste