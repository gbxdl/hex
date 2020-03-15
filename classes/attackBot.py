from classes.gameState import *
import random

class attackBot:
    
    def __init__(self):
        self.firstMove=True
        #idea: find the most bottom/right element of discovered and attach bottom/right random. If not possible take second furthest.
        
    def makeMove(self,gameState):
        moveOptions = []        
        
        if self.firstMove:
            moveOptions = gameState.startlist[gameState.onMove-1]
            self.firstMove=False
        else:
            if gameState.lastMove:
                for pos in gameState.discovered[gameState.onMove-1]:            
                    if gameState.onMove == 1: #if blue, go down
                        lowest = 0
                        if pos[0] >= lowest:
                            furthest = pos
                            lowest = pos[0]
                        moveOptions = [(furthest[0]+1,furthest[1]-x) for x in [0,1]] #move above somewhat random
                    else:
                        rightest = 0
                        if pos[1] >= rightest:
                            furthest = pos
                            rightest = pos[1]
                        moveOptions = [(furthest[0]+y,furthest[1]+1) for y in [0,1]] #move left somewhat random
                
        moveOptions = [x for x in gameState.possibleMoves() if x in moveOptions] #take overlap
        
        if moveOptions:
            move = random.choice(moveOptions)
            return move
        
        return random.choice(list(gameState.possibleMoves()))