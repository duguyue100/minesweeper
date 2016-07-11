"""Test script for the game board.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
from minesweeper.msgame import MSGame

game = MSGame(10, 10, 5)

game.print_board()

try:
    input = raw_input
except NameError:
    pass

while game.game_status == 2:
    # play move
    move = input("Move: ")
    game.play_move_msg(move)
