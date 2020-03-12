#!/usr/bin/env python3

#start without a human player. Just have random moves.
from classes.gameState import *
from classes.play import *
import time

sizeBoard = 11
guiOn = True

gameState = gameState(sizeBoard)
play = play()

play.run(gameState,guiOn)

# 
# tic=time.time()
# numGames=100
# winner=[0,0]
# for i in range(numGames):
#     result=play.run(gameState)
#     winner[result-1]+=1
#     gameState.resetGameState()
# 
# print('Out of', numGames, 'White won', winner[0], 'times and Black won', winner[1], 'times')
# toc=time.time()
# print(toc-tic,'seconds')