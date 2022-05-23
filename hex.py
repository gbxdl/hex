#!/usr/bin/env python3

import argparse

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

if __name__ == "__main__":
    args = parser.parse_args()
    gameState = gameState(args)

    play = play(gameState)
    play.run()
