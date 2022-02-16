from Tree import *
from board_functions import *

def makeTree(node, curPlayer, isMax):
    if(isWinner("O", node.board)):
        if isMax:
            node.setWinNum(-1)
        else:
            node.setWinNum(1)

        return node.winNum

    elif(isWinner("X", node.board)):
        if isMax:
            node.setWinNum(1)
        else:
            node.setWinNum(-1)

        return node.winNum

    elif(boardFilled(node.board)):
        node.setWinNum(0)

        return node.winNum

    else:
        minimax = 0
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
                newNode.setWinNum(makeTree(newNode, nextPlayer, not isMax))
                node.addChild(newNode)

        if isMax:
            minimax = max(node.children)
        else:
            minimax = min(node.children)

        return node.setWinNum(minimax.winNum)
