
isa = {"00110": "mul", "00111": "div", "01000": "rs", "01001": "ls",
       "01010": "xor", "01011": "or"}

FLAGS = "111"


def simulate(reg: dict, mem: dict, counter: str) -> tuple:
    """
    :param reg: A dictionary containing contents of all registers
    :param mem: A dictionary containing memory contents by address
    :param counter: A string containing the value of program counter in binary
    :return: Modified values of the parameters and a boolean stating if command was found
    """

    old_flags = reg[FLAGS]
    reg[FLAGS] = "0" * 16

    if isa.get(mem[counter][0:5]) == 'mul':
        counter = bin(int(counter, 2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg2 = int(reg.get(mem[counter][10:13]))
        reg3 = int(reg.get(mem[counter][13:]))
        result = bin(reg2 * reg3)[2:]
        if len(result) <= 16:
            reg[mem[counter][7:10]] = "0" * (16 - len(result)) + result
        else:
            reg[mem[counter][7:10]] = result[len(result) - 16:]
            reg[FLAGS] = "0" * 12 + "1" + "0" * 3

        return reg, mem, [counter], True

    elif isa.get(mem[counter][0:5]) == 'div':
        counter = bin(int(counter, 2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg2 = int(reg.get(mem[counter][10:13]))
        reg3 = int(reg.get(mem[counter][13:]))
        quo = bin(int(reg2 / reg3))[2:]
        len_q = len(quo)
        rem = bin(int(reg2 % reg3))[2:]
        len_r = len(rem)
        reg["000"] = "0" * (16 - len_q) + quo
        reg["001"] = "0" * (16 - len_r) + rem
        return reg, mem, [counter], True

    elif isa.get(mem[counter][0:5]) == 'rs':
        counter = bin(int(counter, 2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg1 = int(reg.get(mem[counter][5:8]), 2)
        imm = int(mem[counter][8:], 2)
        result = bin(reg1 >> imm)[2:0]
        if len(result) <= 16:
            reg[reg1] = "0" * (8-len(result)) + result
        return reg, mem, [counter], True

    elif isa.get(mem[counter][0:5]) == 'ls':
        counter = bin(int(counter, 2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg1 = int(reg.get(mem[counter][5:8]), 2)
        imm = int(mem[counter][8:], 2)
        result = bin(imm << reg1)[2:0]
        if len(result) >= 16:
            reg[reg1] = result[-16:-1]
        return reg, mem, [counter], True

    elif isa.get(mem[counter][0:5]) == 'xor':
        counter = bin(int(counter, 2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg1 = int(reg.get(mem[counter][7:10]))
        reg2 = int(reg.get(mem[counter][10:13]))
        reg3 = int(reg.get(mem[counter][13:]))
        reg[reg1] = reg2 ^ reg3
        return reg, mem, [counter], True

    elif isa.get(mem[counter][0:5]) == 'or':
        counter = bin(int(counter, 2) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg1 = int(reg.get(mem[counter][7:10]))
        reg2 = int(reg.get(mem[counter][10:13]))
        reg3 = int(reg.get(mem[counter][13:]))
        reg[reg1] = reg2 | reg3
        return reg, mem, [counter], True

    else:
        reg[FLAGS] = old_flags
        return reg, mem, [counter], False
