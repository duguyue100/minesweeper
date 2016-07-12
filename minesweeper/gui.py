"""Some GUI helper functions.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from PyQt4 import QtGui, QtCore


class GameWidget(QtGui.QWidget):
    """Setup Game Interface."""

    def __init__(self, ms_game):
        """Init the field."""
        super(GameWidget, self).__init__()

        self.ms_game = ms_game
        self.init_ui()

    def init_ui(self):
        """Init game interface."""
        board_width = self.ms_game.board_width
        board_height = self.ms_game.board_height
        self.create_grid(board_width, board_height)

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

    def update_grid(self):
        """update grid according to info map."""
        info_map = self.ms_game.get_info_map()
        for i in xrange(self.ms_game.board_height):
            for j in xrange(self.ms_game.board_width):
                self.grid_wgs[(i, j)].info_label(info_map[i, j])


class FieldWidget(QtGui.QLabel):
    """A customized Field Widget."""

    def __init__(self):
        """Init the field."""
        super(FieldWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        """init the ui."""
        self.setFixedSize(25, 25)
        self.setText("  ")
        self.setStyleSheet("QLabel {background-color: blue;" +
                           "color: red;" +
                           "qproperty-alignment: AlignCenter;}")

    def mousePressEvent(self, event):
        """Define mouse press event."""
        if event.button() == QtCore.Qt.LeftButton:
            # get label position
            p_wg = self.parent()
            p_layout = p_wg.layout()
            idx = p_layout.indexOf(self)
            loc = p_layout.getItemPosition(idx)[:2]
            p_wg.ms_game.play_move("click", loc[1], loc[0])
            p_wg.update_grid()
        elif event.button() == QtCore.Qt.RightButton:
            p_wg = self.parent()
            p_layout = p_wg.layout()
            idx = p_layout.indexOf(self)
            loc = p_layout.getItemPosition(idx)[:2]
            if self.text() == "@":
                self.info_label(10)
                p_wg.ms_game.play_move("question", loc[1], loc[0])
                p_wg.update_grid()
            elif self.text() == "  ":
                self.info_label(9)
                p_wg.ms_game.play_move("flag", loc[1], loc[0])
                p_wg.update_grid()
            elif self.text() == "?":
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
            self.setText(str(indicator))
            self.setStyleSheet("QLabel {background-color: green;" +
                               "color: red;" +
                               "qproperty-alignment: AlignCenter;}")
        elif indicator == 0:
            self.setText(" ")
            self.setStyleSheet("QLabel {background-color: green;" +
                               "color: red;" +
                               "qproperty-alignment: AlignCenter;}")
        elif indicator == 12:
            self.setText("!")
            self.setStyleSheet("QLabel {background-color: black;" +
                               "color: red;" +
                               "qproperty-alignment: AlignCenter;}")
        elif indicator == 9:
            self.setText("@")
            self.setStyleSheet("QLabel {background-color: #A3C1DA;" +
                               "color: purple;}")
        elif indicator == 10:
            self.setText("?")
            self.setStyleSheet("QLabel {background-color: yellow;" +
                               "color: purple;}")
        elif indicator == 11:
            self.setText("  ")
            self.setStyleSheet('QLabel {background-color: blue;}')
