from Tree import *
from board_functions import checkFreeSpace

def playerMove(board, root):
    choice = int(input("Where do you want to place? (type number between 1-9):"))

    while True:
        if checkFreeSpace(choice-1, board):
            board[choice-1] = "X"
            break
        else:
            print("Invalid input please try again")
            choice = int(input("Where do you want to place? (type number between 1-9):"))

    for i in root.children:
        if (i.pos == choice-1):
            root = i
            break

    return root

def computerMove(board, root):
    print("entered")
    root = min(root.children)
    board[root.pos] = "O"

    return root
