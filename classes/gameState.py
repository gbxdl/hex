import numpy as np
from classes.randomBot import *
from collections import deque

class gameState:

    def __init__(self,sizeBoard):
        self.sizeBoard = sizeBoard
        self.position = self.startPosition(sizeBoard)
        self.Player = [randomBot(),randomBot()]
        self.initBfs()

    def startPosition(self,sizeBoard):#returns square numpy array of zeros depending on the board size.
        return np.zeros((sizeBoard, sizeBoard),dtype=int)
        # return [[0 for i in range(sizeBoard)] for j in range(sizeBoard)] #numpy is faster
    def possibleMoves(self):#gives a zip of the possible moves (easy to itterate over) convert to list for other purposes.
        return zip(*np.nonzero(self.position==0))#this return row,col, so y,x

    def gameover(self,lastMove,lastMoveBy):#see if game is over based on position and
        return self.updateBfs(lastMove,lastMoveBy)

    def initBfs(self):
        self.queue = [deque([]),deque([])] #is queue needed as a class variable? isn't it made empty every time or is that inefficient?
        self.discovered = [[],[]]
        self.startlist=[[(0,y) for y in range(self.sizeBoard)],[(x,0) for x in range(self.sizeBoard)]]
        self.finishlist=[[(self.sizeBoard-1,y) for y in range(self.sizeBoard)],[(x,self.sizeBoard-1) for x in range(self.sizeBoard)]]

    def updateBfs(self,lastMove,lastMoveBy):#breadth first search
        if not self.hasNeighbour(lastMove,self.discovered[lastMoveBy-1],lastMoveBy):#no need to update Bfs if last move is not connected to the starting node.
            return False
        else:
            self.queue[lastMoveBy-1].append(lastMove)
            self.discovered[lastMoveBy-1].append(lastMove)#right?
            
        colorPosition = list(zip(*np.nonzero(self.position==lastMoveBy)))#needs to be a list otherwise you can only interate over it once.

        #see if there is a begin point. Not needed
        # for pos in self.startlist[lastMoveBy-1]:
        #     if self.position[pos]==lastMoveBy and pos not in self.discovered[lastMoveBy-1]:
        #         self.queue[lastMoveBy-1].append(pos)
        #         self.discovered[lastMoveBy-1].append(pos)
        while(self.queue[lastMoveBy-1]):
            v=self.queue[lastMoveBy-1].popleft()
            if v in self.finishlist[lastMoveBy-1]:
                return True
            for w in self.neighbours(v,lastMoveBy,colorPosition):
                if w not in self.discovered[lastMoveBy-1]:
                    self.discovered[lastMoveBy-1].append(w)
                    self.queue[lastMoveBy-1].append(w)
        return False

    def hasNeighbour(self,pos,posList,lastMoveBy):
        if pos in self.startlist[lastMoveBy-1]:
            return True
        
        for pos2 in posList:
            hor = abs(pos[1]-pos2[1]) == 1 and pos[0]==pos2[0]
            ver = abs(pos[0]-pos2[0]) == 1 and pos[1]==pos2[1]
            topright = pos[0]-pos2[0] == 1 and pos2[1]-pos[1] == 1
            bottomleft = pos[1]-pos2[1] == 1 and pos2[0]-pos[0] == 1
            if hor or ver or topright or bottomleft:
                return True
        return False
        
    def neighbours(self, pos, lastMoveBy, colorPosition):#copy pasted too much code. These two functions should be the same function.
        neighbours = []
        for pos2 in colorPosition:
            hor = abs(pos[1]-pos2[1]) == 1 and pos[0]==pos2[0]
            ver = abs(pos[0]-pos2[0]) == 1 and pos[1]==pos2[1]
            topright = pos[0]-pos2[0] == 1 and pos2[1]-pos[1] == 1
            bottomleft = pos[1]-pos2[1] == 1 and pos2[0]-pos[0] == 1
            if hor or ver or topright or bottomleft:
                neighbours.append(pos2)
        return neighbours
        
    def resetGameState(self):
        self.__init__(self.sizeBoard)
        
        
        
        
        
        
        
