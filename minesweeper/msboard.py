"""Class that defines the board for Mine Sweeper game.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import numpy as np


class MSBoard(object):
    """Define a Mine Sweeper Game Board."""

    def __init__(self, board_width, board_height, num_mines):
        """The init function of Mine Sweeper Game.

        Parameters
        ----------
        board_width : int
            the width of the board (> 0)
        board_height : int
            the height of the board (> 0)
        num_mines : int
            the number of mines, cannot be larger than
            (board_width x board_height)
        """
        if (board_width <= 0):
            raise ValueError("the board width cannot be non-positive!")
        else:
            self.board_width = board_width

        if (board_height <= 0):
            raise ValueError("the board height cannot be non-positive!")
        else:
            self.board_height = board_width

        if (num_mines >= (board_width*board_height)):
            raise ValueError("The number of mines cannot be larger than "
                             "number of grids!")
        else:
            self.num_mines = num_mines

    def init_board(self):
        """Init a valid board by given settings.

        Parameters
        ----------
        mine_map : numpy.ndarray
            the map that defines the mine
            0 is empty, 1 is mine
        info_map : numpy.ndarray
            the map that presents to gamer
            0-8 is number of mines in srrounding.
            9 is flagged field.
            10 is questioned field.
            11 is undiscovered field.
        """
        self.mine_map = np.zeros((self.board_height, self.board_width),
                                 dtype=np.uint8)
        idx_list = np.random.permutation(self.board_width*self.board_height)
        idx_list = idx_list[:self.num_mines]

        for idx in idx_list:
            idx_x = int(idx % self.board_width)
            idx_y = int(idx / self.board_width)

            self.mine_map[idx_y, idx_x] = 1

        self.info_map = np.ones((self.board_height, self.board_width),
                                dtype=np.uint8)*11

    def click_field(self):
        """Click one grid by given position."""

    def flag_field(self):
        """Flag a grid by given position."""

    def unflag_field(self):
        """Unflag or unquestion a grid by given position."""

    def question_field(self):
        """Question a grid by given position."""

    def check_board(self):
        """Check the board status and give feedback."""
