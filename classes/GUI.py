from tkinter import *
from classes.human import *
import math
import time

class gui:
    
    def __init__(self,window,gameState):
        self.canvasWidth = 1300
        self.canvasHeight = 800
        self.window = window
        self.gameState = gameState
        self.width = self.canvasHeight / (self.gameState.sizeBoard)
        self.fromTheEdge=self.width
        self.window.title('Hex')
        
    def initInteract(self):
        self.drawCanvas()
        self.drawLattice()
        self.restartButton()
        if self.gameState.humans == [False,False]:
            self.gamePlay()
        else:
            self.window.bind("<Button-1>", self.gamePlay)

    def gamePlay(self,event=None):
        man = human()
        while 1:
            move = 0
            print(self.gameState.onMove)
            if event and self.gameState.onMove == 1:
                move = man.makeMove(self.gameState, event, self.fromTheEdge, self.width)
            elif self.gameState.onMove == 2:
                move = self.gameState.bot.makeMove(self.gameState)
                print('bot move', move)
                # time.sleep(.1)
            if move==0:
                return
            self.gameState.position[move]=self.gameState.onMove
            self.gameState.lastMove = move
            self.drawMove(move[0],move[1])
            self.window.update()
            # print(self.gameState.position)
            gameover=self.gameState.gameover()
            if gameover:
                if self.gameState.onMove==1:
                    print('Blue won!')
                else:
                    print('Red won!')
                if self.gameState.humans != [False,False]:
                    self.window.unbind("<Button-1>")
                return
            self.gameState.onMove=3-self.gameState.onMove
        
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
        
    def hexagon(self,row,col): #draw a hexagon around position x,y with R, r as on https://en.wikipedia.org/wiki/Hexagon
        x = (col+row/2)*self.width + self.fromTheEdge
        y=row*(math.sqrt(3)/2*self.width) + self.fromTheEdge
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
        reset_button = Button(self.window, text="New game",command = self.restart())
        reset_button.pack(side=LEFT)
    
    def restart(self):
        self.gameState.resetGameState()
        self.canvas.destroy()
        self.drawCanvas()
        self.drawLattice()
    
        