import random
import time
from classes.gameState import *

class randomBot():

    def __init__(self):
        None

    def makeMove(self,gameState):
        try:
            return random.choice(list(gameState.possibleMoves()))
        except:
            move=0
            print(gameState.position)
            print(gameState.discovered)
            print(list(gameState.possibleMoves()))
            time.sleep(10)