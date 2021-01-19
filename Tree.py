class Node:
    def __init__(self, pos, board):
        self.winNum = 0
        self.pos = pos
        self.board = board
        self.children = []
        self.parent = -1

    def addChild(self, node):
        self.children.append(node)

    def setParent(self, node):
        self.parent = node

    def setWinNum(self, winNum):
        self.winNum = winNum
        return self.winNum
