from Tree import *
from board_functions import *

def makeTree(node, curPlayer):
    if(isWinner("O", node.board)):
        node.setWinNum(1)

        return node.winNum

    elif(isWinner("X", node.board)):
        node.setWinNum(-1)

        return node.winNum

    elif(boardFilled(node.board)):
        node.setWinNum(0)

        return node.winNum

    else:
        totalNum = 0
        nextPlayer = " "

        if(curPlayer == "X"):
            nextPlayer = "O"

        else:
            nextPlayer = "X"

        for x in range(len(node.board)):
            if(node.board[x] == " "):
                tempboard = list(node.board)
                tempboard[x] = curPlayer
                newNode = Node(x, tempboard)
                newNode.setParent(node)
                node.addChild(newNode)
                totalNum += newNode.setWinNum(makeTree(newNode, nextPlayer))

        return node.setWinNum(totalNum)
