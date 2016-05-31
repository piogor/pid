# -*- coding: utf-8 -*-
#
# This file is part of the PIDcontroller project
#
# (c) by Piotr Goryl, 3Controls Sp. z o.o.
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" PID controller

PID controller
"""

__all__ = ["PIDcontroller", "main"]

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import class_property, device_property
from PyTango import AttrQuality, AttrWriteType, DispLevel, DevState
# Additional import
# PROTECTED REGION ID(PIDcontroller.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  PIDcontroller.additionnal_import


class PIDcontroller(Device):
    """
    PID controller
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(PIDcontroller.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  PIDcontroller.class_variable
    # ----------------
    # Class Properties
    # ----------------

    # -----------------
    # Device Properties
    # -----------------

    ControlledDeviceProxy = device_property(
        dtype='str',
    )

    InputAttribute = device_property(
        dtype='str', default_value="Input"
    )

    OutputAttribute = device_property(
        dtype='str', default_value="Output"
    )

    # ----------
    # Attributes
    # ----------

    SetPoint = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
        label="Set point",
    )

    ControlValue = attribute(
        dtype='double',
    )

    PorcessValue = attribute(
        dtype='double',
    )

    ErrorValue = attribute(
        dtype='double',
    )

    KP = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
    )

    KI = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
    )

    KD = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(PIDcontroller.init_device) ENABLED START #
        self.kd = 0.0
        self.ki = 0.0
        self.kp = 1.0
        # PROTECTED REGION END #    //  PIDcontroller.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(PIDcontroller.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  PIDcontroller.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(PIDcontroller.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  PIDcontroller.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def write_SetPoint(self, value):
        # PROTECTED REGION ID(PIDcontroller.SetPoint_write) ENABLED START #
        self.sp = value
        # PROTECTED REGION END #    //  PIDcontroller.SetPoint_write

    def read_ControlValue(self):
        # PROTECTED REGION ID(PIDcontroller.ControlValue_read) ENABLED START #
        return self.cv
        # PROTECTED REGION END #    //  PIDcontroller.ControlValue_read

    def read_PorcessValue(self):
        # PROTECTED REGION ID(PIDcontroller.PorcessValue_read) ENABLED START #
        return self.pv
        # PROTECTED REGION END #    //  PIDcontroller.PorcessValue_read

    def read_ErrorValue(self):
        # PROTECTED REGION ID(PIDcontroller.ErrorValue_read) ENABLED START #
        return self.sp-self.pv
        # PROTECTED REGION END #    //  PIDcontroller.ErrorValue_read

    def read_KP(self):
        # PROTECTED REGION ID(PIDcontroller.KP_read) ENABLED START #
        return self.kp
        # PROTECTED REGION END #    //  PIDcontroller.KP_read

    def write_KP(self, value):
        # PROTECTED REGION ID(PIDcontroller.KP_write) ENABLED START #
        self.kp=value
        # PROTECTED REGION END #    //  PIDcontroller.KP_write

    def read_KI(self):
        # PROTECTED REGION ID(PIDcontroller.KI_read) ENABLED START #
        return self.ki
        # PROTECTED REGION END #    //  PIDcontroller.KI_read

    def write_KI(self, value):
        # PROTECTED REGION ID(PIDcontroller.KI_write) ENABLED START #
        self.ki=value
        # PROTECTED REGION END #    //  PIDcontroller.KI_write

    def read_KD(self):
        # PROTECTED REGION ID(PIDcontroller.KD_read) ENABLED START #
        return self.kd
        # PROTECTED REGION END #    //  PIDcontroller.KD_read

    def write_KD(self, value):
        # PROTECTED REGION ID(PIDcontroller.KD_write) ENABLED START #
        self.kd=value
        # PROTECTED REGION END #    //  PIDcontroller.KD_write

    # --------
    # Commands
    # --------

    @command
    @DebugIt()
    def computePID(self):
        # PROTECTED REGION ID(PIDcontroller.computePID) ENABLED START #
        pass
        # PROTECTED REGION END #    //  PIDcontroller.computePID

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    from PyTango.server import run
    return run((PIDcontroller,), args=args, **kwargs)

if __name__ == '__main__':
    main()
