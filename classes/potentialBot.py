import numpy as np
from numpy import unravel_index
import random
import math
#idea is to define a potential field depending on the position of your stones and enemy stone and take make the move with the highest potential. Or take probablity depending on potential. Boltzman or something. Normalize first.

class potentialBot: #normalize by making each field a probability of moving there.
    
    def __init__(self,gameState):
        self.potential = np.zeros(([gameState.sizeBoard,gameState.sizeBoard]))
        self.basisConstant = .01
        self.ownColorConstant=1
        self.otherColorConstant=1.1
        # self.meanGaussGood = 4/math.sqrt(3)
        self.meanGaussGood = 10
        self.meanGaussBad = 0
        self.stdGaussGood = 1.5
        self.stdGaussBad = .5
        self.normGaussGood=1/(self.stdGaussGood*math.sqrt(2*math.pi))
        self.normGaussBad=1/(self.stdGaussBad*math.sqrt(2*math.pi))
        self.varPois = 1.5
        self.initialPotential(gameState.sizeBoard)
        
    def initialPotential(self,sizeBoard): #all else equal move in the middle:
        for row in range(sizeBoard):
            for col in range(sizeBoard):
                self.potential[row][col] += sizeBoard**2 * self.basisConstant - ( self.basisConstant * ( (row - sizeBoard/2)**2 + (col - sizeBoard/2)**2  ) )
    
    def makeMove(self,gameState):
        if gameState.lastMove:
            self.updatePotential(gameState,gameState.lastMove,False)#update potential for opponents move

        move = unravel_index(np.argmax(self.potential), self.potential.shape)
        
        self.updatePotential(gameState,move,True)#update potential for own move
        
        return move
    
    def updatePotential(self,gameState,lastMove,lastMoveByMe): #some normalization needed.
        myColor = gameState.onMove
        
        for row in range(gameState.sizeBoard):
            for col in range(gameState.sizeBoard):
                [dy,dx] = gameState.euclidDistanceYX(lastMove,(row,col))
                # dy = abs(dy)
                # dx = abs(dx)
                #these are orthogonal directions but the directions of players isnt' orthogonal. Makes an angle of 30. Cos(30)=sqrt(3)/2
                if dx==dy==0:
                    dxSkewed=0
                    dySkewed=0
                else:
                    dxSkewed = dx * math.cos(-math.pi/6) + dy*math.sin(-math.pi/6)
                    dySkewed = - dx * math.sin(-math.pi/6) + dy*math.cos(-math.pi/6)
                
                if lastMoveByMe:
                    constant = self.ownColorConstant
                    if myColor==1: #i'm blue
                        goodDirection = dy #if I'm blue I should go up compared to my last stone
                        badDirection = dx # not sideways
                    else: #I'm red
                        goodDirection = dxSkewed #if I'm red I should go sideways skewed!
                        badDirection = dySkewed #rotate axis!
                else: #last move was my opponents move.
                    constant = self.otherColorConstant
                    if myColor==1:
                        goodDirection = dx #If my opponennt is red he want to go skewed so I should go sideways compared to his stone
                        badDirection = dy
                    else:
                        goodDirection = dySkewed#defend the straight up
                        badDirection = dxSkewed

                # print(dy,dx)

                self.potential[row,col] *= 1 + constant * self.normGaussGood * ( math.exp(-abs(abs(goodDirection)-self.meanGaussGood)/self.stdGaussGood) ) 
                self.potential[row,col] *= 1 + constant * self.normGaussBad * ( math.exp(-abs(abs(badDirection)-self.meanGaussBad)/self.stdGaussBad) )
                
                # print(1 + constant * self.normGauss * ( math.exp(-abs(abs(goodDirection)-self.meanGaussGood)/self.stdGauss) ) )
                # print(1 + constant * self.normGauss * ( math.exp(-abs(abs(badDirection)-self.meanGaussBad)/self.stdGauss) ))
                
                    
        for pos in zip(*np.nonzero(gameState.position!=0)):
            self.potential[pos]=0
        
                