from classes.gameState import *
from classes.randomBot import *
import numpy as np
import random

gameState = gameState(11)
randomBot = randomBot()

# position=np.zeros((11,11))
# for irow in range(11):
#     for icol in range(11):
#         rand = random.random()
#         if rand > .5:
#             gameState.position[irow][icol]=1
#         elif rand <.1:
#             gameState.position[irow][icol]=2

gameState.initBfs()
while 1:
    lastMove = randomBot.makeMove(gameState)
    gameState.position[lastMove] = 2
    print(gameState.position)
    print(lastMove)
    gameover=gameState.gameover(lastMove,2)
    if(gameover):
        print('Game over!')
        break