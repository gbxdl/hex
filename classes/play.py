import time
class play:
    def __init__(self, gameState):
        None
        # self.run(gameState)

    def run(self, gameState):
        gameover=0
        onMove=1
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
        return onMove