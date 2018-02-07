# -*- coding: utf-8 -*-

"""This module contains all the constants used in ComPath template repo"""

import os

from bio2bel.utils import get_connection, get_data_dir

MODULE_NAME = 'compath_template'
DATA_DIR = get_data_dir(MODULE_NAME)
DEFAULT_CACHE_CONNECTION = get_connection(MODULE_NAME)

CONFIG_FILE_PATH = os.path.join(DATA_DIR, 'config.ini')