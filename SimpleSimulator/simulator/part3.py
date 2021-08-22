#!/usr/bin/env python3

def simulate(reg: dict, mem: dict, counter: str) -> tuple:
    """

    :param reg: A dictionary containing contents of all registers
    :param mem: A dictionary containing memory contents by address
    :param counter: A string containing the value of program counter in binary
    :return: Modified values of the parameters and a boolean stating if command was found
    """
    return reg, mem, counter, False
