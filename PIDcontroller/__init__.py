# -*- coding: utf-8 -*-
#
# This file is part of the PIDcontroller project
#
# (c) by Piotr Goryl, 3Controls Sp. z o.o.
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

"""PID controller

PID controller
"""

from . import release
from .PIDcontroller import PIDcontroller, main

__version__ = release.version
__version_info__ = release.version_info
__author__ = release.author
