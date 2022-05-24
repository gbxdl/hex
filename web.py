"""
Starts the flask app and calls hex.
"""
from dataclasses import dataclass

from flask import Flask, render_template

from classes.gameState import gameState
from classes.play import play


@dataclass
class settings:
    """Place to set the things that are passed with arguemts in hex.py"""

    def __init__(self):
        self.gui = True
        self.player1 = "human"
        self.player2 = "defend"
        self.print_winner = True


args = settings()

# define flask app
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)

gameState = gameState(args)

play = play(gameState, app=app)
play.run()


@app.route("/")
def home_page_hex() -> str:
    """
    Loads starting page.
    """
    return render_template("hex.html.j2")
