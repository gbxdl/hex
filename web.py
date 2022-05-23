"""
Starts the flask app and calls hex.
"""
import argparse
from flask import Flask, render_template

from classes.gameState import gameState
from classes.play import play

parser = argparse.ArgumentParser()
parser.add_argument("--gui", action="store_true", help="use GUI", default=False)
parser.add_argument(
    "--player1",
    "-p1",
    choices=["human", "attack", "defend", "potential"],
    default="human",
)
parser.add_argument(
    "--player2",
    "-p2",
    choices=["human", "attack", "defend", "potential"],
    default="defend",
)
parser.add_argument(
    "--print-winner",
    action="store_true",
    default=False,
)

args = parser.parse_args()
gameState = gameState(args)

play = play(gameState)
play.run()

# define flask app
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)


@app.route("/")
def home_page_svb() -> str:
    """
    Loads page.
    """
    return render_template("hex.html")
