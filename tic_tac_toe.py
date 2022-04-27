import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def display_board(board):
    
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3])

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    return board[7] == board[8] == board[9] == mark or \
           board[4] == board[5] == board[6] == mark or \
           board[1] == board[2] == board[3] == mark or \
           board[7] == board[4] == board[1] == mark or \
           board[8] == board[5] == board[2] == mark or \
           board[9] == board[6] == board[3] == mark or \
           board[7] == board[5] == board[3] == mark or \
           board[9] == board[5] == board[1] == mark

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    return not ' ' in board

def player_choice(board):
    
    while True:
        
        try:
            print("select a position (1-9)")
            choice = int(input())
            if not choice in range(1,10):
                print("position must be a digit between 1 and 9")
            elif not space_check(board, choice):
                print("space is already taken")
            else:
                return choice
        except:
            print("position must be a digit between 1 and 9")

def reset_board():
    return ('X', ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '])

def play_again():

    while True:
        play_again = input("Play again?(y or n) ")
        if play_again.lower() == 'y':
            return True
        elif play_again.lower() == 'n':
            return False
        else:
            print("Please enter y or n")

print('Welcome to Tic Tac Toe!')

mark = 'X'
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

while not full_board_check(board) and not win_check(board, mark):
    
    # changes active player
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'
        
    display_board(board)
    print( "{}'s turn".format(mark))
    choice = player_choice(board)
    place_marker(board, mark, choice)
    clearConsole()

    if win_check(board, mark):
        
        display_board(board)
        print("{} wins".format(mark))
        
        if play_again():
            mark, board = reset_board()

    elif full_board_check(board):
        
        display_board(board)
        print("draw")
        
        if play_again():
            mark, board = reset_board()

    