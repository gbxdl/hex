import time
from tkinter import *
from classes.gui import *

class play:
    def __init__(self):
        pass
        # self.run(gameState)

    def run(self, gameState):
        if gameState.guiOn: #GUI on
            print('GUI is on')
            window = Tk()
            GUI = gui(window, gameState)
            GUI.initInteract()
            window.mainloop()

        else: #GUI off
            gameover=0
            while not gameover:
                move = gameState.bot.makeMove(gameState)
                gameState.position[move]=gameState.onMove
                gameState.lastMove = move
                # print(gameState.position)
                gameover=gameState.gameover()#takes position and lastMoveBy
                if gameover:
                    if gameState.onMove==1:
                        print('Blue won!')
                    else:
                        print('Red won!')
                    break
                gameState.onMove=3-gameState.onMove
            
            showFinalPosition=0
            if showFinalPosition:
                window = Tk()
                GUI = gui(window, gameState)
                GUI.drawPosition()
                window.mainloop()
            