# -*- coding: utf-8 -*-

from __future__ import print_function

import logging

from bio2bel import build_cli

from .manager import Manager

log = logging.getLogger(__name__)

main = build_cli(Manager)
