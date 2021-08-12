#!/usr/bin/env python3

def assemble(command: str, line_num: int) -> str:
    reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100",
           "R5": "101",
           "R6": "110"}
    isa = {"add": ("00000", "A"), "sub": ("00001", "A"), "mov": (("00010", "B"), ("00011", "C")),
           "ld": ("00100", "D"), "st": ("00101", "D")}
    types = {"A": 4, "B": 3, "C": 3, "D": 3}
    command = command.split()
    instruct = command[0]
    final_bin = ""
    if (instruct in isa) and instruct != "mov":
        if len(command) != types[isa[instruct][1]]:
            return ""
        else:
            if isa[instruct][1] == "A":
                final_bin += isa[instruct][0]
                for i in range(1, types[isa[instruct][1]]):
                    reg_x = reg.get(command[i])
                    if reg is not None:
                        final_bin += reg_x
                    else:
                        return ""
                return final_bin
            elif isa[instruct][1] == "D":
                final_bin += isa[instruct][0]
                reg_x = reg.get(command[1])
                if reg_x is not None:
                    final_bin += reg_x
                else:
                    return ""
                final_bin += command[2]
                return final_bin
            else:
                return ""
    elif instruct == "mov":
        if len(command) != 3:
            return ""
        else:
            if "$" in command[2]:
                final_bin += isa[instruct][0][0]
                if command[1] in reg:
                    final_bin += reg[command[1]]
                else:
                    return ""
                if int(command[2][1:]) > 255 or int(command[2][1:]) < 0:
                    return ""
                else:
                    bin_num = bin(int(command[2][1:]))[2:]
                    while len(bin_num) != 8:
                        bin_num = "0" + bin_num
                    final_bin += bin_num
                return final_bin
            else:
                final_bin += isa[instruct][1][0]
                if command[1] in reg:
                    final_bin += reg[command[1]]
                else:
                    return ""
                if command[2] in reg:
                    final_bin += reg[command[2]]
                else:
                    return ""
                return final_bin
    else:
        return ""
