import numpy as np
import random
import math
#idea is to define a potential field depending on the position of your stones and enemy stone and take make the move with the highest potential. Or take probablity depending on potential. Boltzman or something. Normalize first.

class potentialBot:
    
    def __init__(self,gameState):
        self.potential = np.zeros(([gameState.sizeBoard,gameState.sizeBoard]))
        self.basisConstant = .01
        self.ownColorConstant=.01
        self.otherColorConstant=.1
        self.initialPotential(gameState.sizeBoard)
        
    def initialPotential(self,sizeBoard): #all else equal move in the middle:
        for row in range(sizeBoard):
            for col in range(sizeBoard):
                self.potential[row][col] = 1 - ( self.basisConstant * ( (row - sizeBoard/2)**2 + (col - sizeBoard/2)**2  ) )
    
    def updatePotential(self,gameState,lastMove,newMoveByMe): #some normalization needed.
        if newMoveByMe:
            myColor = gameState.position[lastMove]
        else:
            myColor = 2 - gameState.position[lastMove]
        for row in range(gameState.sizeBoard):
            for col in range(gameState.sizeBoard):
                if gameState.euclidDistance((row,col),lastMove) > 4: #for all positions somewhat close to the last stone, remove later
                    continue
                dx = abs(col - lastMove[1])
                dy = abs(row - lastMove[0])
                if newMoveByMe:
                    if myColor==1:#up down is good. right left is bad.
                        self.potential[row,col] += self.ownColorConstant *( abs(dy - 4/math.sqrt(3)) -  math.exp(dx) )
                        #dy>0 good, dx=0 good. dx small good. dy around 4/sqrt(3) or a bit bigger good find function.
                        #so function with dx peaked around 0: e^-dx. distance from 4/sqrt(3) for now. (can make gauss of poisson or so)
                    else: #right left is good, up down is bad.
                        self.potential[row,col] += self.ownColorConstant *( abs(dx - 4/math.sqrt(3)) -  math.exp(dy) )
                        #same dx,dy swapped.
                else: #not new move by me
                    if myColor==2:#up down is good. right left is bad.
                        self.potential[row,col] += self.otherColorConstant * ( abs(dy - 4/math.sqrt(3)) -  math.exp(.1*dx) )
                        #opposite for now but maybe should be different
                    else: #right left is good, up down is bad.
                        self.potential[row,col] += self.otherColorConstant *( abs(dx - 4/math.sqrt(3)) -  math.exp(.1*dy) )
        #never make illegal moves zip(*nonzero..
        for pos in zip(*np.nonzero(gameState.position!=0)):
            self.potential[pos]=0
        
        
        
    def makeMove(self,gameState):
        self.updatePotential(gameState,gameState.lastMove,False)#update potential for opponents move
        
        move = (math.floor(np.argmax(self.potential) / gameState.sizeBoard), np.argmax(self.potential) % gameState.sizeBoard)
        
        # print(self.potential)
        
        self.updatePotential(gameState,move,True)#update potential for own move
        return move
            
        return random.choice(list(gameState.possibleMoves()))