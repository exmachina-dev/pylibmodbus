# -*- coding: utf-8 -*-
# Copyright (c) 2013, Stéphane Raimbault <stephane.raimbault@gmail.com>
# Copyright (c) 2015, Benoit Rapidel <benoit.rapidel@exmachina.fr>

from .modbus_core import C, ModbusCore

class ModbusRtu(ModbusCore):

    RTU_RS232 = 0x00
    RTU_RS232 = 0x01

    RTU_RTS_NONE = 0x00
    RTU_RTS_UP = 0x01
    RTU_RTS_DOWN = 0x02

    def __init__(self, device="/dev/ttyS0", baud=9600,
            parity='N', data_bit=1, stop_bit=0):
        self.ctx = C.modbus_new_rtu(device.encode(), baud,
                parity.encode(), data_bit, stop_bit)
