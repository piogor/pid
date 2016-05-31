#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the PIDcontroller project
#
# (c) by Piotr Goryl, 3Controls Sp. z o.o.
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

import os
import sys
from setuptools import setup

setup_dir = os.path.dirname(os.path.abspath(__file__))

# make sure we use latest info from local code
sys.path.insert(0, setup_dir)

with open('README.rst') as file:
    long_description = file.read()

exec(open('PIDcontroller/release.py').read())
pack = ['PIDcontroller']

setup(name=name,
      version=version,
      description='PID controller',
      packages=pack,
      scripts=['scripts/PIDcontroller'],
      include_package_data=True,
      test_suite="test",
      author='piotr.goryl',
      author_email='piotr.goryl at 3-controls.com',
      license='GPL',
      long_description=long_description,
      url='www.tango-controls.org',
      platforms="All Platforms"
      )
