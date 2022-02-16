from Tree import *
from board_functions import *
from moveCalc import *
from gameplay import *

board = []
someoneWon = False

for x in range(9):
    board.append(" ")

compBoard = list(board)
root = Node(-1, compBoard)

makeTree(root, "X", True)

while(not(boardFilled(board))):
    printBoard(board)
    root = playerMove(board, root)
    print("player moved")
    print("//////////")
    printBoard(root.board)
    print(root.pos)
    print("//////////")

    if (isWinner("X", board)):
        printBoard(board)
        print("You won!")
        someoneWon = True
        break

    print("computer moving")
    print(root)
    root = computerMove(board, root)
    print("computer moved")
    printBoard(board)
    print("//////////")
    printBoard(root.board)
    print(root.pos)
    print("//////////")

    if (isWinner("O", board)):
        print("You lost!")
        someoneWon = True
        break

if(boardFilled(board) and not(someoneWon)):
    print("its a tie")
