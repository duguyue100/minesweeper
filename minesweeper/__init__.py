"""The init file for minsweeper package.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import os
from minesweeper.msgame import MSGame
from minesweeper.msboard import MSBoard

PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))
PACKAGE_IMGS_PATH = os.path.join(PACKAGE_PATH, "imgs")
