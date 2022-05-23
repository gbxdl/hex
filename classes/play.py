import time
from tkinter import Tk
from classes.gui_tkinter import gui_tkinter
from classes.gui_flask import gui_flask


class play:
    def __init__(self, gameState, web_gui: bool = False):
        self.gameState = gameState
        self.web_gui = web_gui
        self.GUI = None

    def run(self):
        if self.gameState.guiOn:  # GUI on
            # print("GUI is on")
            if not self.web_gui:
                window = Tk()
                GUI = gui_tkinter(window, self.gameState, self)
                self.GUI = GUI
                GUI.initInteract()
                if self.gameState.humans == [False, False]:
                    self.gamePlay(None, GUI)
                else:
                    GUI.window.bind(
                        "<Button-1>", lambda event: self.gamePlay(event, GUI), GUI
                    )  # lambda takes event so then you can explicitly pass it together with something else.
                window.mainloop()
            else:  # web gui
                self.GUI = gui_flask(self.gameState, self)
        else:  # GUI off
            return self.gamePlay(
                None, None
            )  # call gameplay without event and without GUI.

    def gamePlay(self, event, GUI):
        keepMakingMoves = True
        while keepMakingMoves:
            [move, keepMakingMoves] = self.playMove(
                event, GUI
            )  # keep making moves unless it's a human's term (wrong move by human or bot just moved)
            if move == 0:
                return
            self.gameState.position[
                move
            ] = self.gameState.onMove  # change position according to last move.
            self.gameState.lastMove = move  # set last move to move.
            if self.gameState.guiOn:  # if the GUI is on draw the new position.
                GUI.drawMove(move[0], move[1])
                GUI.update()
            self.gameState.updateBfs()
            gameover = self.gameState.gameover()  # See if someone has won.
            if gameover:
                self.noMorePlay(
                    GUI, self.gameState.printWinner
                )  # takes bool print winner
                return self.gameState.onMove
            self.gameState.onMove = (
                3 - self.gameState.onMove
            )  # update who is on move for the next turn. Last thing since gameover still uses who is on move as 'last move by'.

    def playMove(self, event, GUI):
        if (
            self.gameState.humans[self.gameState.onMove - 1] == True
        ):  # if a human is on move
            move = self.gameState.man.makeMove(
                self.gameState, event, GUI.fromTheEdge, GUI.width
            )
            if move == 0:
                return [move, False]
        else:  # bot is on move
            if self.gameState.onMove == 1:  # first bot
                move = self.gameState.bot.makeMove(self.gameState)  # bot 1 make move
            elif self.gameState.onMove == 2:  # second bot
                move = self.gameState.bot2.makeMove(self.gameState)  # bot 2 make move
            if self.gameState.guiOn:
                time.sleep(
                    self.gameState.sleeptime
                )  # slow down a bit after a bot move so you can view
            if (
                self.gameState.humans[2 - self.gameState.onMove] == True
            ):  # if the next player is a human exit this loop.
                return [move, False]
        return [move, True]

    def noMorePlay(self, GUI, printWinner):
        if printWinner:
            if self.gameState.onMove == 1:
                print("Blue won!")
            else:
                print("Red won!")
        if self.gameState.humans != [False, False] and self.gameState.guiOn:
            GUI.unbind()
        elif self.gameState.showFinalPosition:
            GUI.drawPosition()
