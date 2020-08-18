import numpy as np
board = [['_','_','_'],['_','_','_'],['_','_','_']]
move_counter = 0
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
    print(player)
    if board[row][col] == '_':
        board[row][col] = player
        move_counter += 1
    else:
        print("Feltet er tatt velg et annet")
    return move_counter

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
        row, col = input("Skriv inn trekk: ").split()
        player = 'X'
        move_counter = make_a_move(row, col, player, move_counter)
    if game_end(board, player) == False:
        play(move_counter)
    else:
        print("Spiller", player, "vant!")

play(move_counter)