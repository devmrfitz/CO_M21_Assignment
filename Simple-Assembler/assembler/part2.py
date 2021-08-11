#!/usr/bin/env python3

def assemble(command: str) -> str:
    """
    :param command: add R0 R1 R2
    :return: 0000000000001010
    """

    reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100",
           "R5": "101", "R6": "110"}
    if command.split()[0] == "mul" and len(command.split()) > 4:
        if ((reg.get(command.split()[1]) is not None) and
                (reg.get(command.split()[2]) is not None) and
                (reg.get(command.split()[3]) is not None)):
            ans = "00110" + reg.get(command.split()[1]) + reg.get(
                command.split()[2]) \
                  + reg.get(command.split()[3])
            return ans
        else:
            return ""

    elif command.split()[0] == "div" and len(command.split()) > 3:
        if ((reg.get(command.split()[1]) is not None) and
                (reg.get(command.split()[2]) is not None)):
            ans = "00111" + reg.get(command.split()[1]) + reg.get(
                command.split()[2])
            return ans
        else:
            return ""

    elif command.split()[0] == "rs" and len(command.split()) > 3:
        if reg.get(command.split()[1]) is not None:
            temp = ''.join(format(ord(i), '08b') for i in command.split()[2])
            # print (temp)
            ans = "01000" + reg.get(command.split()[1]) + temp
            return ans
        else:
            return ""

    elif command.split()[0] == "rs" and len(command.split()) > 3:
        if reg.get(command.split()[1]) is not None:
            temp = ''.join(format(ord(i), '08b') for i in command.split()[2])
            # print (temp)
            ans = "01000" + reg.get(command.split()[1]) + temp
            return ans
        else:
            return ""

    return "0"