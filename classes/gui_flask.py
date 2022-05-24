"""
Interacts between the python code and the html/javascript code
"""

from typing import Callable, Dict, Union

from flask import Response, render_template, request

from classes.gui_base import gui_base


class fake_event:
    def __init__(self):
        self.x = None
        self.y = None


class gui_flask(gui_base):
    """tries to mimic gui_tkinter and passes arguments on to javascript"""

    def __init__(self, gameState, play):
        super().__init__(gameState, play)
        self.play = play
        self.gameState = gameState
        self.view_comms()
        self.background_lattice = []  # list of hexagons to draw
        self.drawLattice()
        self.hexagons_p1 = []
        self.hexagons_p2 = []

    def view_comms(self) -> None:
        """
        connects the post method from the html to the play functions
        """
        map_name_to_callback: Dict[str, Callable[[], None]] = {
            "start_game": self.reset,
        }

        @self.play.app.route("/", methods=["POST"])
        def submit() -> Union[str, Response]:
            name = request.form.get("main-form")
            if name in map_name_to_callback:  # button push
                map_name_to_callback[name]()
            elif request.form.get("canvas-click"):
                click_data = request.form.get("canvas-click")
                fake_event.x, fake_event.y = map(int, click_data.split(","))
                self.play.gamePlay(fake_event, self)
            return self.update()

    def drawLattice(self):
        """creates the background lattice as a list to be rendered by view"""
        for row in range(self.gameState.sizeBoard):
            for col in range(self.gameState.sizeBoard):
                hexagon = self.hexagon(row, col)
                self.background_lattice.append(hexagon)

    def drawMove(self, x, y):
        """fills the lists which indicate which hexagons to draw"""
        if self.gameState.onMove == 1:
            self.hexagons_p1.append(self.hexagon(x, y))
        else:
            self.hexagons_p2.append(self.hexagon(x, y))

    def start(self):
        """starts the game"""
        pass

    def reset(self):
        self.hexagons_p1 = []
        self.hexagons_p2 = []
        self.gameState.resetGameState()

    def unbind(self):
        pass

    def update(self):
        """redraw the website"""
        return render_template(
            "hex.html.j2",
            background_lattice=self.background_lattice,
            canvas_width=self.canvasWidth,
            canvas_height=self.canvasHeight,
            playing=True,
            hexagons_p1=self.hexagons_p1,
            hexagons_p2=self.hexagons_p2,
        )
