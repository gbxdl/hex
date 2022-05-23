import random
import time


class randomBot():

    def __init__(self,gameState):
        None

    def makeMove(self,gameState):
        try:
            return random.choice(list(gameState.possibleMoves()))
        except:
            print(gameState.position)
            print(gameState.discovered)
            print(list(gameState.possibleMoves()))
            print('gameover:', gameState.gameover())
            blueWin=False
            redWin=False
            for dis in gameState.discovered[0]:
                if dis in gameState.finishlist[0]:
                    blueWin=True
            for dis in gameState.discovered[1]:
                if dis in gameState.finishlist[1]:
                    redWin=True
            print('Blue should have won:', blueWin)
            print('Red should have won:', redWin)
            print(gameState.finishlist)
            time.sleep(10)