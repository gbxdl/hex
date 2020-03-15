import numpy as np
import random
import math
#idea is to define a potential field depending on the position of your stones and enemy stone and take make the move with the highest potential. Or take probablity depending on potential. Boltzman or something. Normalize first.

class potentialBot:
    
    def __init__(self,gameState):
        self.potential = np.zeros(([gameState.sizeBoard,gameState.sizeBoard]))
        self.initialPotential(gameState.sizeBoard)
        
    def initialPotential(self,sizeBoard):
        basisConstant = .01
        for row in range(sizeBoard):
            for col in range(sizeBoard):
                self.potential[row][col] = 1 - ( basisConstant * ( (row - sizeBoard/2)**2 + (col - sizeBoard/2)**2  ) )
    
    def updatePotential(self,gameState,lastMove,lastMoveByMe):
        self.potential[lastMove]=0#never make an illegal move.
        if lastMoveByMe:
            myColor = gameState.position[lastMove]
        else:
            myColor = 2 - gameState.position[lastMove]
        if lastMoveByMe:
            for row in range(gameState.sizeBoard):
                for col in range(gameState.sizeBoard):
                    if gameState.distance((row,col),lastMove) > 5:
                        continue
                    print('distance', gameState.distance(row,col,lastMove))
                    print('between', (row,col), 'and', lastMove)
        
        
    def makeMove(self,gameState):
        #all else equal move in the middle:
        self.updatePotential(gameState,gameState.lastMove,False)#update potential for opponents move
        
        move = (math.floor(np.argmax(self.potential) / gameState.sizeBoard), np.argmax(self.potential) % gameState.sizeBoard)
        
        self.updatePotential(gameState,move,True)#update potential for own move
        return move
            
        return random.choice(list(gameState.possibleMoves()))