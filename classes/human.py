import math

class human:
    def __init__(self):
        pass
        
    def makeMove(self,gameState,event,fromTheEdge, width):
        klik=[event.x, event.y]
        #klik[1] = fromTheEdge + y*width*sqrt(3)/2 -> 
        #klik[0] = fromTheEdge + x * width + y * width/2 -> klik[0] - fromTheEdge) /width = x + y/2
        row = round( (klik[1] - fromTheEdge) / (width*math.sqrt(3)/2) )
        col = round( (klik[0] - fromTheEdge ) / width - row/2 )
        
        if 0 <= col < gameState.sizeBoard and 0 <= row < gameState.sizeBoard :
            if (row,col) in gameState.possibleMoves():
                return (row,col)
            else: 
                return 0
        else:
            return 0