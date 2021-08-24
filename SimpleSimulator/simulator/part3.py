#!/usr/bin/env python3

ISA = {
    "01100": (3, 0, 0),
    "01101": (2, 0, 0),
    "01110": (2, 0, 0),
    "01111": (0, 1, 0),
    "10000": (0, 1, 0),
    "10001": (0, 1, 0),
    "10010": (0, 1, 0),
}

FLAGS = "111"


def bitwise_and(a: str, b: str):
    return "".join([str(int(a[i]) * int(b[i])) for i in range(len(a))])


def bitwise_not(a: str):
    return "".join([str(abs(int(char) - 1)) for char in a])


def simulate(reg: dict, mem: dict, counter: str) -> tuple:
    """

    :param reg: A dictionary containing contents of all registers
    :param mem: A dictionary containing memory contents by address
    :param counter: A string containing the value of program counter in binary
    :return: Modified values of the parameters and a boolean stating if command was found
    """
    flags_old = reg[FLAGS]
    reg[FLAGS] = "0" * 16
    command = mem.get(counter)
    opcode = command[:5]
    new_counter = bin(int(counter, 2) + 1)[2:]
    new_counter = "0" * (8 - len(new_counter)) + new_counter
    is_modified = True
    if opcode == "01100":
        reg1 = command[7:10]
        reg2 = command[10:13]
        reg3 = command[13:16]
        reg[reg1] = bitwise_and(reg[reg2], reg[reg3])
    elif opcode == "01101":
        reg1 = command[10:13]
        reg2 = command[13:16]
        reg[reg1] = bitwise_not(reg[reg2])
    elif opcode == "01110":
        reg1 = command[10:13]
        reg2 = command[13:16]
        if int(reg[reg1]) < int(reg[reg2]):
            reg[FLAGS] = "0" * 13 + "1" + "00"
        elif reg[reg1] == reg[reg2]:
            reg[FLAGS] = "0" * 15 + "1"
        else:
            reg[FLAGS] = "0" * 14 + "1" + "0"
    elif opcode == "01111":
        new_counter = command[-8:]
    elif opcode == "10000":
        if flags_old[-3] == "1":
            new_counter = command[-8:]
    elif opcode == "10001":
        if flags_old[-2] == "1":
            new_counter = command[-8:]
    elif opcode == "10010":
        if flags_old[-1] == "1":
            new_counter = command[-8:]
    else:
        is_modified = False

    return reg, mem, [new_counter], is_modified
