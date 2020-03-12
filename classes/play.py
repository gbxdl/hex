import time
from tkinter import *
from classes.gui import *

class play:
    def __init__(self):
        pass
        # self.run(gameState)

    def run(self, gameState, guiOn):
        gameover=0
        onMove=1
        if guiOn:
            window = Tk()
            GUI = gui(window, gameState)
        while not gameover:
            move = gameState.Player[onMove-1].makeMove(gameState)
            gameState.position[move]=onMove
            # print(gameState.position)
            gameover=gameState.gameover(move,onMove)#takes position and lastMoveBy
            if gameover:
                # if onMove==1:
                #     print('White won!')
                # else:
                #     print('Black won!')
                break
            onMove=3-onMove

        if window:
            window.mainloop()