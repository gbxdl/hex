import numpy as np
import math
from classes.randomBot import *
from classes.defenseBot import *
from classes.attackBot import *
from classes.potentialBot import *
from classes.human import *
from collections import deque


class gameState:
    def __init__(self):
        self.sizeBoard = 11
        self.position = self.startPosition(self.sizeBoard)
        self.humans = [True, False]
        self.guiOn = False
        self.printWinner = False
        self.sleeptime = 0.2
        if any(self.humans) == True:
            self.guiOn = True
            self.printWinner = True
        self.showFinalPosition = False

        self.bot = potentialBot(self)
        self.bot2 = defenseBot(self)
        # self.bot = defenseBot(self)
        # self.bot2 = potentialBot(self)
        self.man = human()
        self.lastMove = []
        self.onMove = 1
        self.initBfs()

    def startPosition(
        self, sizeBoard
    ):  # returns square numpy array of zeros depending on the board size.
        return np.zeros((sizeBoard, sizeBoard), dtype=int)  # row,col
        # return [[0 for i in range(sizeBoard)] for j in range(sizeBoard)] #numpy is faster

    def possibleMoves(
        self,
    ):  # gives a zip of the possible moves (easy to itterate over) convert to list for other purposes.
        return zip(*np.nonzero(self.position == 0))  # this return row,col, so y,x

    def gameover(self):  # see if game is over based on position and
        for dis in self.discovered[self.onMove - 1]:
            if dis in self.finishlist[self.onMove - 1]:
                return True
        if any(
            [
                x in self.finishlist[self.onMove - 1]
                for x in self.discovered[self.onMove - 1]
            ]
        ):
            return True

        return False  # should seperate this call from gameover.

    def initBfs(self):
        self.queue = [
            deque([]),
            deque([]),
        ]  # is queue needed as a class variable? isn't it made empty every time or is that inefficient?
        self.discovered = [[], []]
        self.startlist = [
            [(0, y) for y in range(self.sizeBoard)],
            [(x, 0) for x in range(self.sizeBoard)],
        ]
        self.finishlist = [
            [(self.sizeBoard - 1, y) for y in range(self.sizeBoard)],
            [(x, self.sizeBoard - 1) for x in range(self.sizeBoard)],
        ]

    def updateBfs(self):  # breadth first search
        if (
            not self.neighbours(self.lastMove, self.discovered[self.onMove - 1])
            and self.lastMove not in self.startlist[self.onMove - 1]
        ):
            return False  # no need to update not connected to the starting node.
        else:
            self.queue[self.onMove - 1].append(self.lastMove)
            self.discovered[self.onMove - 1].append(self.lastMove)  # right?

        colorPosition = list(
            zip(*np.nonzero(self.position == self.onMove))
        )  # needs to be a list otherwise you can only interate over it once.
        while self.queue[self.onMove - 1]:
            v = self.queue[self.onMove - 1].popleft()
            if v in self.finishlist[self.onMove - 1]:
                return True
            for w in self.neighbours(v, colorPosition):
                if w not in self.discovered[self.onMove - 1]:
                    self.discovered[self.onMove - 1].append(w)
                    self.queue[self.onMove - 1].append(w)
        return False

    def neighbours(
        self, pos, colorPosition
    ):  # copy pasted too much code. These two functions should be the same function.
        neighbours = []
        if not pos:  # shouldn't be needed. pos should never be none.
            return neighbours
        for pos2 in colorPosition:
            hor = abs(pos[1] - pos2[1]) == 1 and pos[0] == pos2[0]
            ver = abs(pos[0] - pos2[0]) == 1 and pos[1] == pos2[1]
            topright = pos[0] - pos2[0] == 1 and pos2[1] - pos[1] == 1
            bottomleft = pos[1] - pos2[1] == 1 and pos2[0] - pos[0] == 1
            if hor or ver or topright or bottomleft:
                neighbours.append(pos2)
        return neighbours

    def euclidDistanceYX(
        self, pos1, pos2
    ):  # calculate distance between two possitions in hex widths = radius circle
        x1 = (
            pos1[1] + pos1[0] / 2
        )  # actual x location in the hex grid is shifted half a width to the right per line
        y1 = (
            pos1[0] * math.sqrt(3) / 2
        )  # actual y location is different due to difference in
        x2 = pos2[1] + pos2[0] / 2
        y2 = pos2[0] * math.sqrt(3) / 2
        xdiff = x1 - x2
        ydiff = y1 - y2
        return [ydiff, xdiff]

    def resetGameState(self):
        self.position = self.startPosition(self.sizeBoard)
        self.onMove = 1
        self.bot.__init__(self)
        self.bot2.__init__(self)
        self.initBfs()
