from tkinter import *
import math

class gui:
    
    def __init__(self,tk,gameState):
        self.canvasWidth = 1300
        self.canvasHeight = 800
        self.tk = tk
        self.gameState = gameState
        self.tk.title('Hex')
        self.drawCanvas()
        self.drawLattice()

    def drawCanvas(self):
        self.canvas = Canvas(self.tk, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas.pack()
        
    def drawLattice(self):
        width = self.canvasHeight / (self.gameState.sizeBoard)
        fromTheEdge=width
        for i in range(self.gameState.sizeBoard):
            for j in range(self.gameState.sizeBoard):
                x = (i+j/2)*width + fromTheEdge
                y=j*(math.sqrt(3)/2*width) + fromTheEdge
                hexagon=self.hexagon(x,y,width)
                self.canvas.create_polygon(hexagon,fill='white',outline='black', width=2)
                
    def hexagon(self,x,y,width):
        #draw a hexagon around position x,y with R, r as on https://en.wikipedia.org/wiki/Hexagon
        r = width/2
        R = r * 2/math.sqrt(3)
        top=(x,y-R)
        bottom=(x,y+R)
        topLeft=(x-r,y-R/2)
        bottomLeft=(x-r,y+R/2)
        topRight=(x+r,y-R/2)
        bottomRight=(x+r,y+R/2)
        
        return [top,topRight,bottomRight,bottom,bottomLeft,topLeft]
        
        

class HexaCanvas(Canvas):
    """ A canvas that provides a create-hexagone method """
    def __init__(self, master):
        Canvas.__init__(self, master)

        self.hexaSize = 20

    def setHexaSize(self, number):
        self.hexaSize = number

    def create_hexagone(self, x, y):
        size = self.hexaSize
        dx = (size**2 - (size/2)**2)**0.5

        point1 = (x+dx, y+size/2)
        point2 = (x+dx, y-size/2)
        point3 = (x   , y-size  )
        point4 = (x-dx, y-size/2)
        point5 = (x-dx, y+size/2)
        point6 = (x   , y+size  )

        self.create_line(point1, point2, width=2)
        self.create_line(point2, point3, width=2)
        self.create_line(point3, point4, width=2)
        self.create_line(point4, point5, width=2)
        self.create_line(point5, point6, width=2)
        self.create_line(point6, point1, width=2)

        # self.create_polygon(point1, point2, point3, point4, point5, point6)

class HexagonalGrid(HexaCanvas):
    """ A grid whose each cell is hexagonal """
    def __init__(self, master, scale, grid_width, grid_height, *args, **kwargs):

        dx     = (scale**2 - (scale/2.0)**2)**0.5
        width  = 2 * dx * grid_width + dx
        height = 1.5 * scale * grid_height + 0.5 * scale

        HexaCanvas.__init__(self, master)
        self.setHexaSize(scale)

    def setCell(self, xCell, yCell):
        size = self.hexaSize
        dx = (size**2 - (size/2)**2)**0.5

        pix_x = dx + 2*dx*xCell
        if yCell%2 ==1 :
            pix_x += dx

        pix_y = size + yCell*1.5*size

        self.create_hexagone(pix_x, pix_y)



# if __name__ == "__main__":
#     tk = Tk()
# 
#     grid = HexagonalGrid(tk, scale = 50, grid_width=4, grid_height=4)
#     grid.grid(row=0, column=0, padx=5, pady=5)
# 
#     def correct_quit(tk):
#         tk.destroy()
#         tk.quit()
# 
#     quit = Button(tk, text = "Quit", command = lambda: correct_quit(tk))
#     quit.grid(row=1, column=0)
#     for i in range(10):
#         for j in range(10):
#             grid.setCell(i,j)
# 
#     tk.mainloop()