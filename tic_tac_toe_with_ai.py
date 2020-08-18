import numpy as np
import math
board = [['_','_','_'],['_','_','_'],['_','_','_']]
rewards = [1,0,-1]
move_counter = 0

ai = "X"
player = "O"
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
    # print(player)
    if board[row][col] == '_':
        board[row][col] = player
        move_counter += 1
    else:
        print("Feltet er tatt velg et annet")
    return move_counter

def mini_max_scoring(board, player):
    #Checking horisontals
    print(player)
    for i in range(len(board)):
        print(board)
        if board[i][0] == board[i][1] == board[i][2] == "hei":
            # print(print_board(board))
            print("nice")
            if player == "X":
                return 10
            if player == "O":
                return -10
    #Checking verticals
    for i in range (len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
            print(print_board(board))
            print("nice1")
            if player == "X":
                return 10
            if player == "O":
                return -10
    #Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        print("nice2")
        if player == "X":
            return 10
        if player == "O":
            return -10
    if board[0][2] == board[1][1] == board[2][0] == player:
        print("nice3")
        if player == "X":
            return 10
        if player == "O":
            return -10
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
        print("\n\n")
        row, col= input("Skriv inn trekk: ").split()
        player = 'O'
        move_counter = make_a_move(row, col, player, move_counter)
    else:
        print("\n\n")
        row, col = best_ai_move(board)
        player = 'X'
        move_counter = make_a_move(row, col, player, move_counter)
    if game_end(board, player) == False:
        play(move_counter)
    # else:
    #     print("GAME OVER")
def best_ai_move(board):
    best_move_score = -100
    best_move_x = -1
    best_move_y = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                player = "O"
                value_of_move = mini_max(board, 0, False, player)
                print(value_of_move)
                board[i][j] = "_"
                if best_move_score < value_of_move:
                    # print("halla")
                    best_move_score = value_of_move
                    best_move_x = i
                    best_move_y = j
    return (best_move_x, best_move_y)

def mini_max(pos, depth, maximizing_player, player):
    # print("yo")
    score = mini_max_scoring(board, player)
    if score == 10:
        print("score1")
        return score
    if score == -10:
        print("score2")
        return score
    if score == 0 and depth == 4:
        print("score3")
        return score
    if maximizing_player:
        print("yo2")
        best_val = -(math.inf)
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    player = "X"
                    board[i][j] == "X"
                    print("halla2")
                    value = mini_max(board, depth +1, False, player)
                    board[i][j] = "_"
                    best_val = max(best_val, value)
        return best_val
    else:
        print("yo2")
        best_val = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    player = "O"
                    board[i][j] == "O"
                    print("halla3")
                    value = mini_max(board, depth +1, True, player)
                    board[i][j] = "_"
                    best_val = min(best_val, value)
        return best_val                                                                                                           

play(move_counter)