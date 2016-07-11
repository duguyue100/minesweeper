"""GUI for Mine Sweeper.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
from PyQt4 import QtGui, QtCore
import numpy as np

from minesweeper import MSGame
from minesweeper import gui

# create game

board_width = 20
board_height = 10
num_mines = 10
ms_game = MSGame(board_width, board_height, num_mines,
                 port=5678, ip_add="127.0.0.1")

print(ms_game.get_mine_map())

# init mine sweeper application
ms_app = QtGui.QApplication([])

# define window and set layout
ms_window = QtGui.QWidget()
ms_window.setWindowTitle("Mine Sweeper")
ms_layout = QtGui.QGridLayout()
ms_window.setLayout(ms_layout)

fun_wg = QtGui.QWidget()
fun_layout = QtGui.QHBoxLayout()
fun_wg.setLayout(fun_layout)
reset_button = QtGui.QPushButton("Reset")
fun_layout.addWidget(reset_button)

grid_wg = QtGui.QWidget()
grid_layout, grid_wgs = gui.create_grid(board_width, board_height)
grid_wg.setLayout(grid_layout)

ms_layout.addWidget(fun_wg, 0, 0)
ms_layout.addWidget(grid_wg, 1, 0)

prev_info_map = ms_game.get_info_map()
prev_field_loc = gui.FIELD_LOCATION


def update():
    """Update function."""
    global prev_info_map, prev_field_loc

    if prev_field_loc != gui.FIELD_LOCATION:
        gui.button_move(ms_game)
        gui.update_grid(grid_wgs, ms_game.get_info_map(),
                        board_width, board_height)

    curr_info_map = ms_game.get_info_map()
    if not np.array_equal(prev_info_map, curr_info_map):
        prev_info_map = curr_info_map

    if ms_game.game_status in [0, 1]:
        return

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

ms_window.show()
ms_app.exec_()
