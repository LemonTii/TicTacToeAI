from Tree import *

def playerMove(board, root):
    choice = int(input("Where do you want to place? (type number between 1-9):"))

    board[choice-1] = "X"

    for i in root.children:
        if (i.pos == choice-1):
            root = i
            break

    return root

def computerMove(board, root):
    bigNum = "n"
    nextNode = "n"
    for i in root.children:
        if(bigNum == "n"):
            bigNum = i.winNum
            nextNode = i
        elif(bigNum < i.winNum):
            bigNum = i.winNum
            nextNode = i

    root = nextNode
    if (root != ""):
        board[root.pos] = "O"

    return root
