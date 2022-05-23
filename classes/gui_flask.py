"""
Interacts between the python code and the html/javascript code
"""

from typing import Callable, Dict, Union

from flask import Response, render_template, request

from classes.gui_base import gui_base


class gui_flask(gui_base):
    """tries to mimic gui_tkinter and passes arguments on to javascript"""

    def __init__(self, gameState, play):
        super().__init__(gameState, play)
        self.play = play
        self.init_buttons()

    def init_buttons(self) -> None:
        """
        connects the post method from the html to the play functions
        """

        map_name_to_callback: Dict[str, Callable[[], None]] = {
            "start_game": self.start,
        }

        @self.play.app.route("/", methods=["POST"])
        def submit() -> Union[str, Response]:
            name = request.form.get("top-row-button")
            if name in map_name_to_callback:
                map_name_to_callback[name]()
            return render_template(
                "hex.html",
            )

    def start(self):
        """starts the game"""
        self.play.gameplay(None, self)
