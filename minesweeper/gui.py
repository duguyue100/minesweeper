"""Some GUI helper functions.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from functools import partial
from PyQt4 import QtGui  # QtCore

FIELD_LOCATION = None
CLICKED_FIELD = None


def create_grid(grid_width, grid_height):
    """Create a grid layout with stacked widgets.

    Parameters
    ----------
    grid_width : int
        the width of the grid
    grid_height : int
        the height of the grid

    Returns
    -------
    layout : QtGui.QGridLayout
        a QtGui grid layout.
    grid_wgs : Dictionary
        collection of QStackedWidget
    """
    layout = QtGui.QGridLayout()
    layout.setSpacing(1)
    grid_wgs = {}
    for i in xrange(grid_height):
        for j in xrange(grid_width):
            grid_wgs[(i, j)] = QtGui.QStackedWidget()
            grid_wgs[(i, j)].setFixedSize(25, 25)

            # set grids
            temp_button = QtGui.QPushButton(" ")
            temp_button.setFixedSize(25, 25)
            temp_button.setStyleSheet('QPushButton {background-color: blue;}')
            temp_button.clicked.connect(partial(button_pos, temp_button,
                                                layout))
            temp_label = QtGui.QLabel(" ")
            temp_label.setFixedSize(25, 25)

            grid_wgs[(i, j)].addWidget(temp_button)
            grid_wgs[(i, j)].addWidget(temp_label)

            layout.addWidget(grid_wgs[(i, j)], i, j)

    return layout, grid_wgs


def button_pos(button, layout):
    """Button behavior."""
    global FIELD_LOCATION, CLICKED_FIELD
    parent_widget = button.parent()
    parent_idx = layout.indexOf(parent_widget)
    FIELD_LOCATION = layout.getItemPosition(parent_idx)[:2]
    CLICKED_FIELD = button


def button_move(ms_game):
    """Transmit instruction through game."""
    if CLICKED_FIELD is not None and FIELD_LOCATION is not None:
        if CLICKED_FIELD.text() == " ":
            ms_game.play_move("click", FIELD_LOCATION[1], FIELD_LOCATION[0])


def update_grid(grid_wgs, info_map, grid_width, grid_height):
    """Update the grid according to the info map.

    Parameters
    ----------
    grid_wgs : Dictionary
        collection of QStackedWidget
    info_map : numpy.ndarray
        the info map of the game
    """
    # grid_height = info_map.shape[0]
    # grid_width = info_map.shape[1]

    for i in xrange(grid_height):
        for j in xrange(grid_width):
            if info_map[i, j] in xrange(9) or info_map[i, j] == 12:
                info_label(grid_wgs[(i, j)].widget(1), info_map[i, j])
                grid_wgs[(i, j)].setCurrentIndex(1)
            elif info_map[i, j] == 9:
                flag_button(grid_wgs[(i, j)].widget(0))
                grid_wgs[(i, j)].setCurrentIndex(0)
            elif info_map[i, j] == 10:
                question_button(grid_wgs[(i, j)].widget(0))
                grid_wgs[(i, j)].setCurrentIndex(0)
            elif info_map[i, j] == 11:
                empty_button(grid_wgs[(i, j)].widget(0))
                grid_wgs[(i, j)].setCurrentIndex(0)


def empty_button(button):
    """Default button style."""
    button.setText(" ")
    button.setStyleSheet('QPushButton {background-color: blue;}')


def question_button(button):
    """Question button by given settings."""
    button.setText("?")
    button.setStyleSheet("QPushButton {background-color: yellow;" +
                         "color: purple;}")


def flag_button(button):
    """Flag button by given settings."""
    button.setText("@")
    button.setStyleSheet("QPushButton {background-color: #A3C1DA;" +
                         "color: purple;}")


def info_label(label, indicator):
    """Set info label by given settings.

    Parameters
    ----------
    label : QtGui.QLabel
        a QLabel
    indicator : int
        A number where
        0-8 is number of mines in srrounding.
        12 is a mine field.
    """
    if indicator in xrange(1, 9):
        label.setText(str(indicator))
        label.setStyleSheet("QLabel {background-color: green;" +
                            "color: red;" +
                            "qproperty-alignment: AlignCenter;}")
    elif indicator == 0:
        label.setText(" ")
        label.setStyleSheet("QLabel {background-color: green;" +
                            "color: red;" +
                            "qproperty-alignment: AlignCenter;}")
    elif indicator == 12:
        label.setText("!")
        label.setStyleSheet("QLabel {background-color: black;" +
                            "color: red;" +
                            "qproperty-alignment: AlignCenter;}")
