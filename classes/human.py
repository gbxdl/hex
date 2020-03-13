class human:
    def __init__(self):
        pass
        
    def makeMove(self,gameState,event,fromTheEdge, width):
        klik=[event.x, event.y]
        
        print(klik)
        
        y = round( (klik[1] - fromTheEdge) / width )
        x = round( ( klik[0] - fromTheEdge - y * (width/2) ) / width ) #why the +1?
        
        print(x,y)
        # print(list(gameState.possibleMoves()))
        # print(x,y)
        
        if 0 <= x < gameState.sizeBoard and 0 <= y < gameState.sizeBoard :
            if (x,y) in gameState.possibleMoves():
                # print(x,y)
                return [y,x]
            else: return 0
        else:
            return 0