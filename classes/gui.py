from tkinter import *
import math
import time

class gui:
    
    def __init__(self,window,gameState):
        self.canvasWidth = 1000
        self.canvasHeight = 600
        self.window = window
        try:
            self.window.title('Hex')
        except:
            pass
        self.gameState = gameState
        self.width = self.canvasHeight / (self.gameState.sizeBoard)
        self.fromTheEdge=self.width
        
    def initInteract(self):
        self.drawCanvas()
        self.restartButton()        
        self.drawLattice()
        
    def drawMove(self,row,col):#draws the move at coordinates row,col
        hexagon = self.hexagon(row,col)
        if self.gameState.onMove==1:
            self.canvas.create_polygon(hexagon,fill='blue',outline='black', width=2)
        else:
            self.canvas.create_polygon(hexagon,fill='red',outline='black', width=2)
            
    def drawCanvas(self):
        self.canvas = Canvas(self.window, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas.pack()
        
    def drawLattice(self):
        for row in range(self.gameState.sizeBoard):
            for col in range(self.gameState.sizeBoard):
                hexagon=self.hexagon(row,col)
                self.canvas.create_polygon(hexagon,fill='white',outline='black', width=2)
                
    def drawPosition(self):
        self.window = Tk()
        self.drawCanvas()
        for row in range(self.gameState.sizeBoard):
            for col in range(self.gameState.sizeBoard):
                hexagon=self.hexagon(row,col)
                if self.gameState.position[row,col] == 0:
                    self.canvas.create_polygon(hexagon,fill='white',outline='black', width=2)
                elif self.gameState.position[row,col] == 1:
                    self.canvas.create_polygon(hexagon,fill='blue',outline='black', width=2)
                else:
                    self.canvas.create_polygon(hexagon,fill='red',outline='black', width=2)
        self.window.mainloop()
        
    def hexagon(self,row,col): #draw a hexagon around position x,y with R, r as on https://en.wikipedia.org/wiki/Hexagon
        x = (col+row/2)*self.width + self.fromTheEdge
        y = row*(math.sqrt(3)/2*self.width) + self.fromTheEdge
        r = self.width/2
        R = r * 2/math.sqrt(3)
        top=(x,y-R)
        bottom=(x,y+R)
        topLeft=(x-r,y-R/2)
        bottomLeft=(x-r,y+R/2)
        topRight=(x+r,y-R/2)
        bottomRight=(x+r,y+R/2)
        return [top,topRight,bottomRight,bottom,bottomLeft,topLeft]
        
    def restartButton(self):
        self.resetButton = Button(self.window, text="New game", command = self.restart )
        self.resetButton.pack(side=LEFT)
    
    def restart(self):
        self.gameState.resetGameState()
        self.canvas.destroy()
        self.resetButton.destroy()#is dit hoe je dit wil doen. De button moet zichzelf weggooien. Maar moet ie een class var zijn?
        self.initInteract()
        
    