import numpy as np
from classes.randomBot import *
from classes.human import *
from collections import deque

class gameState:

    def __init__(self):
        self.sizeBoard = 11
        self.position = self.startPosition(self.sizeBoard)
        self.humans = [True,False]
        self.guiOn = True
        self.bot = randomBot()
        self.lastMove=[]
        self.onMove=1
        self.initBfs()

    def startPosition(self,sizeBoard):#returns square numpy array of zeros depending on the board size.
        return np.zeros((sizeBoard, sizeBoard),dtype=int)
        # return [[0 for i in range(sizeBoard)] for j in range(sizeBoard)] #numpy is faster
    def possibleMoves(self):#gives a zip of the possible moves (easy to itterate over) convert to list for other purposes.
        return zip(*np.nonzero(self.position==0))#this return row,col, so y,x

    def gameover(self):#see if game is over based on position and
        return self.updateBfs()

    def initBfs(self):
        self.queue = [deque([]),deque([])] #is queue needed as a class variable? isn't it made empty every time or is that inefficient?
        self.discovered = [[],[]]
        self.startlist=[[(0,y) for y in range(self.sizeBoard)],[(x,0) for x in range(self.sizeBoard)]]
        self.finishlist=[[(self.sizeBoard-1,y) for y in range(self.sizeBoard)],[(x,self.sizeBoard-1) for x in range(self.sizeBoard)]]

    def updateBfs(self):#breadth first search
        if not self.neighbours(self.lastMove,self.discovered[self.onMove-1]) and self.lastMove not in self.startlist[self.onMove-1]:
            return False #no need to update not connected to the starting node.
        else:
            self.queue[self.onMove-1].append(self.lastMove)
            self.discovered[self.onMove-1].append(self.lastMove)#right?
            
        colorPosition = list(zip(*np.nonzero(self.position==self.onMove)))#needs to be a list otherwise you can only interate over it once.
        while(self.queue[self.onMove-1]):
            v=self.queue[self.onMove-1].popleft()
            if v in self.finishlist[self.onMove-1]:
                # print(v)
                # print('bfs found a path')
                # print(self.position)
                return True
            for w in self.neighbours(v,colorPosition):
                if w not in self.discovered[self.onMove-1]:
                    self.discovered[self.onMove-1].append(w)
                    self.queue[self.onMove-1].append(w)
        return False
        
    def neighbours(self, pos, colorPosition):#copy pasted too much code. These two functions should be the same function.
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
        self.__init__()
        
        # def hasNeighbour(self,pos,posList,lastMoveBy):
        #     if pos in self.startlist[lastMoveBy-1]:
        #         return True
        # 
        #     for pos2 in posList:
        #         hor = abs(pos[1]-pos2[1]) == 1 and pos[0]==pos2[0]
        #         ver = abs(pos[0]-pos2[0]) == 1 and pos[1]==pos2[1]
        #         topright = pos[0]-pos2[0] == 1 and pos2[1]-pos[1] == 1
        #         bottomleft = pos[1]-pos2[1] == 1 and pos2[0]-pos[0] == 1
        #         if hor or ver or topright or bottomleft:
        #             return True
        #     return False
        
        
        
        
        
