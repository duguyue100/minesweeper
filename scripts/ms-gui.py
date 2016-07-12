#!/usr/bin/env python
"""GUI for Mine Sweeper.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
from PyQt4 import QtGui

from minesweeper import MSGame, gui

board_width = 20
board_height = 20
num_mines = 40
ms_game = MSGame(board_width, board_height, num_mines,
                 port=5678, ip_add="127.0.0.1")

ms_app = QtGui.QApplication([])

# define window and set layout
ms_window = QtGui.QWidget()
ms_window.setAutoFillBackground(True)
ms_window.setWindowTitle("Mine Sweeper")
ms_layout = QtGui.QGridLayout()
ms_window.setLayout(ms_layout)

fun_wg = gui.ControlWidget()
grid_wg = gui.GameWidget(ms_game, fun_wg)


def reset_button_state():
    """Reset button state."""
    grid_wg.reset_game()

fun_wg.reset_button.clicked.connect(reset_button_state)

ms_layout.addWidget(fun_wg, 0, 0)
ms_layout.addWidget(grid_wg, 1, 0)

ms_window.show()
ms_app.exec_()
