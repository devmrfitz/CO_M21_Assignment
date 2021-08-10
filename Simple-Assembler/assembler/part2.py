#!/usr/bin/env python3

def assemble(command: str) -> str:
    """
    :param command: add R0 R1 R2
    :return: 0000000000001010
    """

    reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100",
           "R5": "101",
           "R6": "110"}
    if command.split()[0] == "mul":
        if ((reg.get("R1") is not None) and (reg.get("R2") is not None) and
                (reg.get("R3") != None)):
            ans = "00110" + reg.get("R1") + reg.get("R2") + reg.get("R3")
        else:
            return

    return "0"
