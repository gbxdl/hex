"""
Interacts between the python code and the html/javascript code
"""

from classes.gui_base import gui_base


class gui_flask(gui_base):
    """tries to mimic gui_tkinter and passes arguments on to javascript"""

    def __init__(self, gameState, play):
        super().__init(gameState, play)
