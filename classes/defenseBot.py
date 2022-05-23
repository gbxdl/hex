import random

from classes.gameState import *


class defenseBot:
    
    def __init__(self,gameState):
        pass
        
    def makeMove(self,gameState):
        moveOptions = []
        if gameState.lastMove:
            if gameState.onMove == 1:
                moveOptions = [(gameState.lastMove[0] + y, gameState.lastMove[1] - x) for y in [0,1] for x in [1,2,3]] #move above somewhat random
            else:
                moveOptions = [(gameState.lastMove[0] + y, gameState.lastMove[1] - x) for y in [1,2,3] for x in [0,1]]#move left somewhat random
                
        moveOptions = [x for x in gameState.possibleMoves() if x in moveOptions] #take overlap
        
        if moveOptions:
            move = random.choice(moveOptions)
            return move
        
        if gameState.lastMove:
            if gameState.onMove == 1:
                moveOptions = [(gameState.lastMove[0] + y, gameState.lastMove[1] + x) for y in [0,1] for x in [1,2,3]] #move above somewhat random
            else:
                moveOptions = [(gameState.lastMove[0] + y, gameState.lastMove[1] - x) for y in [1,2,3] for x in [0,1]]#move left somewhat random
        
        moveOptions = [x for x in gameState.possibleMoves() if x in moveOptions] #take overlap
        
        if moveOptions:
            move = random.choice(moveOptions)
            return move
        
        return random.choice(list(gameState.possibleMoves()))