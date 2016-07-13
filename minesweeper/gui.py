"""Some GUI helper functions.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from os.path import join
from PyQt4 import QtGui, QtCore

import minesweeper

FLAG_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "flag.png")
QUESTION_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "question.png")
BOOM_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "boom.png")
EMPTY_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "blue_circle.png")
NUMBER_PATHS = [join(minesweeper.PACKAGE_IMGS_PATH, "zero.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "one.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "two.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "three.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "four.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "five.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "six.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "seven.png"),
                join(minesweeper.PACKAGE_IMGS_PATH, "eight.png")]
WIN_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "win.png")
LOSE_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "lose.png")
CONTINUE_PATH = join(minesweeper.PACKAGE_IMGS_PATH, "continue.png")


class ControlWidget(QtGui.QWidget):
    """Control widget for showing state of the game."""

    def __init__(self):
        """Init control widget."""
        super(ControlWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        """setup control widget UI."""
        self.control_layout = QtGui.QHBoxLayout()
        self.setLayout(self.control_layout)
        self.reset_button = QtGui.QPushButton()
        self.reset_button.setFixedSize(40, 40)
        self.reset_button.setIcon(QtGui.QIcon(WIN_PATH))
        self.game_timer = QtGui.QLCDNumber()
        self.game_timer.setStyleSheet("QLCDNumber {color: red;}")
        self.game_timer.setFixedWidth(100)
        self.move_counter = QtGui.QLCDNumber()
        self.move_counter.setStyleSheet("QLCDNumber {color: red;}")
        self.move_counter.setFixedWidth(100)

        self.control_layout.addWidget(self.game_timer)
        self.control_layout.addWidget(self.reset_button)
        self.control_layout.addWidget(self.move_counter)


class GameWidget(QtGui.QWidget):
    """Setup Game Interface."""

    def __init__(self, ms_game, ctrl_wg):
        """Init the game."""
        super(GameWidget, self).__init__()

        self.ms_game = ms_game
        self.ctrl_wg = ctrl_wg
        self.init_ui()

    def init_ui(self):
        """Init game interface."""
        board_width = self.ms_game.board_width
        board_height = self.ms_game.board_height
        self.create_grid(board_width, board_height)
        self.time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timing_game)
        self.timer.start(1000)

    def create_grid(self, grid_width, grid_height):
        """Create a grid layout with stacked widgets.

        Parameters
        ----------
        grid_width : int
            the width of the grid
        grid_height : int
            the height of the grid
        """
        self.grid_layout = QtGui.QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.setSpacing(1)
        self.grid_wgs = {}
        for i in xrange(grid_height):
            for j in xrange(grid_width):
                self.grid_wgs[(i, j)] = FieldWidget()
                self.grid_layout.addWidget(self.grid_wgs[(i, j)], i, j)

    def timing_game(self):
        """Timing game."""
        self.ctrl_wg.game_timer.display(self.time)
        self.time += 1

    def reset_game(self):
        """Reset game board."""
        self.ms_game.reset_game()
        self.update_grid()
        self.time = 0
        self.timer.start(1000)

    def update_grid(self):
        """update grid according to info map."""
        info_map = self.ms_game.get_info_map()
        for i in xrange(self.ms_game.board_height):
            for j in xrange(self.ms_game.board_width):
                self.grid_wgs[(i, j)].info_label(info_map[i, j])

        self.ctrl_wg.move_counter.display(self.ms_game.num_moves)
        if self.ms_game.game_status == 2:
            self.ctrl_wg.reset_button.setIcon(QtGui.QIcon(CONTINUE_PATH))
        elif self.ms_game.game_status == 1:
            self.ctrl_wg.reset_button.setIcon(QtGui.QIcon(WIN_PATH))
        elif self.ms_game.game_status == 0:
            self.ctrl_wg.reset_button.setIcon(QtGui.QIcon(LOSE_PATH))
            self.timer.stop()


class FieldWidget(QtGui.QLabel):
    """A customized Field Widget."""

    def __init__(self, field_width=25, field_height=25):
        """Init the field."""
        super(FieldWidget, self).__init__()

        self.field_width = field_width
        self.field_height = field_height

        self.init_ui()

    def init_ui(self):
        """init the ui."""
        self.id = 11
        self.setFixedSize(self.field_width, self.field_height)
        self.setPixmap(QtGui.QPixmap(EMPTY_PATH).scaled(
                self.field_width*3, self.field_height*3))
        self.setStyleSheet("QLabel {background-color: blue;}")

    def mousePressEvent(self, event):
        """Define mouse press event."""
        if event.button() == QtCore.Qt.LeftButton:
            # get label position
            p_wg = self.parent()
            p_layout = p_wg.layout()
            idx = p_layout.indexOf(self)
            loc = p_layout.getItemPosition(idx)[:2]
            if p_wg.ms_game.game_status == 2:
                p_wg.ms_game.play_move("click", loc[1], loc[0])
                p_wg.update_grid()
        elif event.button() == QtCore.Qt.RightButton:
            p_wg = self.parent()
            p_layout = p_wg.layout()
            idx = p_layout.indexOf(self)
            loc = p_layout.getItemPosition(idx)[:2]
            if p_wg.ms_game.game_status == 2:
                if self.id == 9:
                    self.info_label(10)
                    p_wg.ms_game.play_move("question", loc[1], loc[0])
                    p_wg.update_grid()
                elif self.id == 11:
                    self.info_label(9)
                    p_wg.ms_game.play_move("flag", loc[1], loc[0])
                    p_wg.update_grid()
                elif self.id == 10:
                    self.info_label(11)
                    p_wg.ms_game.play_move("unflag", loc[1], loc[0])
                    p_wg.update_grid()

    def info_label(self, indicator):
        """Set info label by given settings.

        Parameters
        ----------
        indicator : int
            A number where
            0-8 is number of mines in srrounding.
            12 is a mine field.
        """
        if indicator in xrange(1, 9):
            self.id = indicator
            self.setPixmap(QtGui.QPixmap(NUMBER_PATHS[indicator]).scaled(
                    self.field_width, self.field_height))
        elif indicator == 0:
            self.id == 0
            self.setPixmap(QtGui.QPixmap(NUMBER_PATHS[0]).scaled(
                    self.field_width, self.field_height))
        elif indicator == 12:
            self.id = 12
            self.setPixmap(QtGui.QPixmap(BOOM_PATH).scaled(self.field_width,
                                                           self.field_height))
            self.setStyleSheet("QLabel {background-color: black;}")
        elif indicator == 9:
            self.id = 9
            self.setPixmap(QtGui.QPixmap(FLAG_PATH).scaled(self.field_width,
                                                           self.field_height))
            self.setStyleSheet("QLabel {background-color: #A3C1DA;}")
        elif indicator == 10:
            self.id = 10
            self.setPixmap(QtGui.QPixmap(QUESTION_PATH).scaled(
                    self.field_width, self.field_height))
            self.setStyleSheet("QLabel {background-color: yellow;}")
        elif indicator == 11:
            self.id = 11
            self.setPixmap(QtGui.QPixmap(EMPTY_PATH).scaled(
                    self.field_width*3, self.field_height*3))
            self.setStyleSheet('QLabel {background-color: blue;}')


class RemoteControlThread(QtCore.QThread):
    """Thread that covers remote control."""

    def __init__(self):
        """Init function of the thread."""
        super(RemoteControlThread, self).__init__()

        self.exiting = False

    def __del__(self):
        """destroy the thread."""
        self.exiting = True
        self.wait()

    def control_start(self, ms_game):
        """start thread control."""
        self.ms_game = ms_game
        self.start()

    def run(self):
        """Thread behavior."""
        self.ms_game.tcp_accept()

        while True:
            data = self.ms_game.tcp_receive()

            if data == "help\n":
                self.ms_game.tcp_help()
                self.ms_game.tcp_send("> ")
            elif data == "exit\n":
                self.ms_game.tcp_close()
            elif data == "print\n":
                self.ms_game.tcp_send(self.ms_game.get_board())
                self.ms_game.tcp_send("> ")
            elif data == "":
                self.ms_game.tcp_send("> ")
            else:
                self.emit(QtCore.SIGNAL("output(QString)"),
                          data)
                self.ms_game.tcp_send("> ")

            if self.ms_game.game_status == 1:
                self.ms_game.tcp_send("[MESSAGE] YOU WIN!\n")
                self.ms_game.tcp_close()
            elif self.ms_game.game_status == 0:
                self.ms_game.tcp_send("[MESSAGE] YOU LOSE!\n")
                self.ms_game.tcp_close()
