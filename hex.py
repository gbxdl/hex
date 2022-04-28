#!/usr/bin/env python3
from classes.gameState import *
from classes.play import *
import time

gameState = gameState()
play = play(gameState)
play.run()

# tic=time.time()
# numGames=100
# winner=[0,0]
# for i in range(numGames):
#     result=play.run()
#     winner[result-1]+=1
#     gameState.resetGameState()

# print('Out of', numGames, 'Blue won', winner[0], 'times and Red won', winner[1], 'times')
# toc=time.time()
# print(toc-tic,'seconds')
