'''
Battleship Game
Version:    1.0
Author:     Mark David Jennings
Created:    2013-07-07
---------------------
Fixes required:
Need to be able to give player another turn if they guess the same location or off the board,
currently they forgo their turn.
'''

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
    print 'Turn Number ', turn + 1
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "*"
        print_board(board)
        break
    else:
        if(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            turn -= 1
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            turn -= 1
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == 3:
            print "Game Over"