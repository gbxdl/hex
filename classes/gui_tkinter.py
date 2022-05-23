from tkinter import Button, Canvas, Tk, LEFT

from classes.gui_base import gui_base


class gui_tkinter(gui_base):
    def __init__(self, window, gameState, play):
        super().__init__(gameState, play)
        self.window = window
        self.window.title("Hex")

    def initInteract(self):
        self.drawCanvas()
        self.restartButton()
        self.drawLattice()

    def drawMove(self, row, col):  # draws the move at coordinates row,col
        hexagon = self.hexagon(row, col)
        if self.gameState.onMove == 1:
            self.canvas.create_polygon(hexagon, fill="blue", outline="black", width=2)
        else:
            self.canvas.create_polygon(hexagon, fill="red", outline="black", width=2)

    def drawCanvas(self):
        self.canvas = Canvas(
            self.window, width=self.canvasWidth, height=self.canvasHeight
        )
        self.canvas.pack()

    def drawLattice(self):
        for row in range(self.gameState.sizeBoard):
            for col in range(self.gameState.sizeBoard):
                hexagon = self.hexagon(row, col)
                self.canvas.create_polygon(
                    hexagon, fill="white", outline="black", width=2
                )

    def drawPosition(self):
        self.window = Tk()
        self.drawCanvas()
        for row in range(self.gameState.sizeBoard):
            for col in range(self.gameState.sizeBoard):
                hexagon = self.hexagon(row, col)
                if self.gameState.position[row, col] == 0:
                    self.canvas.create_polygon(
                        hexagon, fill="white", outline="black", width=2
                    )
                elif self.gameState.position[row, col] == 1:
                    self.canvas.create_polygon(
                        hexagon, fill="blue", outline="black", width=2
                    )
                else:
                    self.canvas.create_polygon(
                        hexagon, fill="red", outline="black", width=2
                    )
        self.window.mainloop()

    def restartButton(self):
        self.resetButton = Button(self.window, text="New game", command=self.restart)
        self.resetButton.pack(side=LEFT)

    def restart(self):
        self.gameState.resetGameState()
        self.canvas.destroy()
        self.resetButton.destroy()  # is dit hoe je dit wil doen. De button moet zichzelf weggooien. Maar moet ie een class var zijn?
        self.initInteract()
        self.window.bind(
            "<Button-1>", lambda event: self.play.gamePlay(event, self), self
        )  # rebind button.
