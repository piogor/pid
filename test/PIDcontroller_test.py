#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the PIDcontroller project
#
# (c) by Piotr Goryl, 3Controls Sp. z o.o.
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.
"""Contain the tests for the PID controller."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from time import sleep
from mock import MagicMock
from PyTango import DevFailed, DevState
from devicetest import DeviceTestCase, main
from PIDcontroller import PIDcontroller

# Note:
#
# Since the device uses an inner thread, it is necessary to
# wait during the tests in order the let the device update itself.
# Hence, the sleep calls have to be secured enough not to produce
# any inconsistent behavior. However, the unittests need to run fast.
# Here, we use a factor 3 between the read period and the sleep calls.
#
# Look at devicetest examples for more advanced testing


# Device test case
class PIDcontrollerDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(PIDcontroller.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  PIDcontroller.test_additionnal_import
    device = PIDcontroller
    properties = {'ControlledDeviceProxy': '','InputAttribute': 'Input','OutputAttribute': 'Output',
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = PIDcontroller.numpy = MagicMock()
        # PROTECTED REGION ID(PIDcontroller.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  PIDcontroller.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(PIDcontroller.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  PIDcontroller.test_properties
        pass

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(PIDcontroller.test_State) ENABLED START #
        self.device.State()
        # PROTECTED REGION END #    //  PIDcontroller.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(PIDcontroller.test_Status) ENABLED START #
        self.device.Status()
        # PROTECTED REGION END #    //  PIDcontroller.test_Status

    def test_computePID(self):
        """Test for computePID"""
        # PROTECTED REGION ID(PIDcontroller.test_computePID) ENABLED START #
        self.device.computePID()
        # PROTECTED REGION END #    //  PIDcontroller.test_computePID

    def test_SetPoint(self):
        """Test for SetPoint"""
        # PROTECTED REGION ID(PIDcontroller.test_SetPoint) ENABLED START #
        self.device.SetPoint
        # PROTECTED REGION END #    //  PIDcontroller.test_SetPoint

    def test_ControlValue(self):
        """Test for ControlValue"""
        # PROTECTED REGION ID(PIDcontroller.test_ControlValue) ENABLED START #
        self.device.ControlValue
        # PROTECTED REGION END #    //  PIDcontroller.test_ControlValue

    def test_PorcessValue(self):
        """Test for PorcessValue"""
        # PROTECTED REGION ID(PIDcontroller.test_PorcessValue) ENABLED START #
        self.device.PorcessValue
        # PROTECTED REGION END #    //  PIDcontroller.test_PorcessValue

    def test_ErrorValue(self):
        """Test for ErrorValue"""
        # PROTECTED REGION ID(PIDcontroller.test_ErrorValue) ENABLED START #
        self.device.ErrorValue
        # PROTECTED REGION END #    //  PIDcontroller.test_ErrorValue

    def test_KP(self):
        """Test for KP"""
        # PROTECTED REGION ID(PIDcontroller.test_KP) ENABLED START #
        self.device.KP
        # PROTECTED REGION END #    //  PIDcontroller.test_KP

    def test_KI(self):
        """Test for KI"""
        # PROTECTED REGION ID(PIDcontroller.test_KI) ENABLED START #
        self.device.KI
        # PROTECTED REGION END #    //  PIDcontroller.test_KI

    def test_KD(self):
        """Test for KD"""
        # PROTECTED REGION ID(PIDcontroller.test_KD) ENABLED START #
        self.device.KD
        # PROTECTED REGION END #    //  PIDcontroller.test_KD


# Main execution
if __name__ == "__main__":
    main()
