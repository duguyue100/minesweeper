"""Class that defines the board for Mine Sweeper game.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import numpy as np
from collections import deque


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
            self.board_height = board_height

        if (num_mines >= (board_width*board_height)):
            raise ValueError("The number of mines cannot be larger than "
                             "number of grids!")
        else:
            self.num_mines = num_mines

        self.init_board()

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
            12 is a mine field.
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

    def click_field(self, move_x, move_y):
        """Click one grid by given position."""
        field_status = self.info_map[move_y, move_x]

        # can only click blank region
        if field_status == 11:
            if self.mine_map[move_y, move_x] == 1:
                self.info_map[move_y, move_x] = 12
            else:
                # discover the region.
                self.discover_region(move_x, move_y)

    def discover_region(self, move_x, move_y):
        """Discover region from given location."""
        field_list = deque([(move_y, move_x)])

        while len(field_list) != 0:
            field = field_list.popleft()

            (tl_idx, br_idx, region_sum) = self.get_region(field[1], field[0])
            if region_sum == 0:
                self.info_map[field[0], field[1]] = region_sum
                # get surrounding to queue
                region_mat = self.info_map[tl_idx[0]:br_idx[0]+1,
                                           tl_idx[1]:br_idx[1]+1]
                x_list, y_list = np.nonzero(region_mat == 11)

                for x_idx, y_idx in zip(x_list, y_list):
                    field_temp = (x_idx+max(field[0]-1, 0),
                                  y_idx+max(field[1]-1, 0))
                    if field_temp not in field_list:
                        field_list.append(field_temp)
            elif region_sum > 0:
                self.info_map[field[0], field[1]] = region_sum

    def get_region(self, move_x, move_y):
        """Get region around a location."""
        top_left = (max(move_y-1, 0), max(move_x-1, 0))
        bottom_right = (min(move_y+1, self.board_height-1),
                        min(move_x+1, self.board_width-1))
        region_sum = self.mine_map[top_left[0]:bottom_right[0]+1,
                                   top_left[1]:bottom_right[1]+1].sum()

        return top_left, bottom_right, region_sum

    def flag_field(self, move_x, move_y):
        """Flag a grid by given position."""
        field_status = self.info_map[move_y, move_x]

        # a questioned or undiscovered field
        if field_status != 9 and (field_status == 10 or field_status == 11):
            self.info_map[move_y, move_x] = 9

    def unflag_field(self, move_x, move_y):
        """Unflag or unquestion a grid by given position."""
        field_status = self.info_map[move_y, move_x]

        if field_status == 9 or field_status == 10:
            self.info_map[move_y, move_x] = 11

    def question_field(self, move_x, move_y):
        """Question a grid by given position."""
        field_status = self.info_map[move_y, move_x]

        # a questioned or undiscovered field
        if field_status != 10 and (field_status == 9 or field_status == 11):
            self.info_map[move_y, move_x] = 10

    def check_board(self):
        """Check the board status and give feedback."""
        num_mines = np.sum(self.info_map == 12)
        num_undiscovered = np.sum(self.info_map == 11)
        num_questioned = np.sum(self.info_map == 10)

        if num_mines > 0:
            return 0
        elif np.array_equal(self.info_map == 9, self.mine_map):
            return 1
        elif num_undiscovered > 0 or num_questioned > 0:
            return 2

    def print_board(self):
        """Print board in structural way."""
        print(self.board_msg())

    def board_msg(self):
        """Structure a board as in print_board."""
        board_str = "s\t\t"
        for i in xrange(self.board_width):
            board_str += str(i)+"\t"
        board_str = board_str.expandtabs(4)+"\n\n"

        for i in xrange(self.board_height):
            temp_line = str(i)+"\t\t"
            for j in xrange(self.board_width):
                if self.info_map[i, j] == 9:
                    temp_line += "@\t"
                elif self.info_map[i, j] == 10:
                    temp_line += "?\t"
                elif self.info_map[i, j] == 11:
                    temp_line += "*\t"
                elif self.info_map[i, j] == 12:
                    temp_line += "!\t"
                else:
                    temp_line += str(self.info_map[i, j])+"\t"
            board_str += temp_line.expandtabs(4)+"\n"

        return board_str
