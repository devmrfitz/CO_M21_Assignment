#!/usr/bin/env python3

isa = {"00000": ("add", "A"), "00001": ("sub", "A"), "00010": ("movImm", "B"), "00011": ("movReg", "C"),
       "00100": ("ld", "D"), "00101": ("st", "D")}


def simulate(reg: dict, mem: dict, counter: str) -> tuple:
    """
        :param reg: A dictionary containing contents of all registers
        :param mem: A dictionary containing memory contents by address
        :param counter: A string containing the value of program counter in binary
        :return: Modified values of the parameters and a boolean stating if command was found
    """
    instruction = mem[counter]
    opcode = instruction[0:5]
    ins_type = isa[opcode][1]
    if ins_type == "A":
        counter = bin(int(counter,2)+1)[2:]
        counter = "0" * (8-len(counter)) + counter
        reg2 = int(reg.get(instruction[10:13], 2))
        reg3 = int(reg.get(instruction[13:16], 2))
        if isa.get(opcode)[0] == "add":
            result = bin(reg2+reg3)[2:]
            length = len(result)
            if length <= 16:
                reg[instruction[7:10]] = "0"*(16-length) + result
            else:
                reg[instruction[7:10]] = result[length-16:]
                reg["FLAGS"] = "0"*12 + "1" + "0"*3
        elif isa.get(opcode)[0] == "sub":
            if reg2 < reg3:
                reg[instruction[7:10]] = "0"*16
                reg["FLAGS"] = "0"*12 + "1" + "0"*3
            else:
                result = bin(reg2 - reg3)[2:]
                length = len(result)
                reg[instruction[7:10]] = "0" * (16 - length) + result
        return reg, mem, [counter], True
    elif ins_type == "B":
        imm = instruction[8:]
        reg[instruction[5:8]] = "0" * 8 + imm
        counter = bin(int(counter,2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        return reg, mem, [counter], True
    elif ins_type == "C":
        reg2 = reg.get(instruction[13:])
        reg[instruction[10:13]] = reg2
        counter = bin(int(counter,2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        return reg, mem, [counter], True
    elif ins_type == "D":
        if isa.get(opcode)[0] == "ld":
            value = mem[instruction[8:]]
            reg[instruction[5:8]] = value
            counter = bin(int(counter,2) + 1)[2:]
            counter = "0" * (8 - len(counter)) + counter
            return reg, mem, [counter, instruction[8:]], True
        elif isa.get(opcode)[0] == "st":
            value = reg[instruction[5:8]]
            mem[instruction[8:]] = value
            counter = bin(int(counter,2) + 1)[2:]
            counter = "0" * (8 - len(counter)) + counter
            return reg, mem, [counter, instruction[8:]], True
    else:
        return reg, mem, counter, False
