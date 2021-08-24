isa = {"00110": "mul", "00111": "div", "01000": "rs", "01001": "ls",
       "01010": "xor", "01011": "or"}


def simulate(reg: dict, mem: dict, counter: str) -> tuple:
    """
    :param reg: A dictionary containing contents of all registers
    :param mem: A dictionary containing memory contents by address
    :param counter: A string containing the value of program counter in binary
    :return: Modified values of the parameters and a boolean stating if command was found
    """

    if isa.get(mem[counter][0:5]) == 'mul':
        counter = bin(int(counter) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg2 = int(reg.get(mem[counter][10:13]))
        reg3 = int(reg.get(mem[counter][13:16]))
        result = bin(reg2 * reg3)[2:]
        length = len(result)
        if length <= 16:
            reg[mem[counter][7:10]] = "0" * (16 - length) + result
        else:
            reg[mem[counter][7:10]] = result[length - 16:]
            reg["FLAGS"] = "0" * 12 + "1" + "0" * 3

        return reg, mem, [counter], False

    elif isa.get(mem[counter][0:5]) == 'div':
        counter = bin(int(counter) + 1)[2:]
        counter = "0" * (8 - len(counter)) + counter
        reg2 = int(reg.get(mem[counter][10:13]))
        reg3 = int(reg.get(mem[counter][13:16]))
        quo = bin(int(reg2 / reg3))[2:]
        len_q = len(quo)
        rem = bin(int(reg2 % reg3))[2:]
        len_r = len(rem)
        reg["000"] = "0" * (16 - len_q) + quo
        reg["001"] = "0" * (16 - len_r) + rem

        return reg, mem, [counter], False

    # elif isa.get(mem[counter][0:5])

    else:
        return reg, mem, counter, False
