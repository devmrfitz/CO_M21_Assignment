#!/usr/bin/env python3

reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100",
       "R5": "101", "R6": "110", }

ISA = {
    "and": ("01100", 3, 0, 0),
    "not": ("01101", 2, 0, 0),
    "cmp": ("01110", 2, 0, 0),
    "jmp": ("01111", 0, 1, 0),
    "jlt": ("10000", 0, 1, 0),
    "jgt": ("10001", 0, 1, 0),
    "je": ("10010", 0, 1, 0),
}


def assemble(command: str, line_num: int) -> str:
    """
    :param line_num:
    :param command: add R0 R1 R2
    :return: 0000000000001010
    """
    command = command.split()

    line_num = str(line_num)

    response = ""

    raw_response = ISA.get(command[0])

    if raw_response:
        if len(command) != 1+sum(raw_response[1:]):
            print("Line " + line_num + ": ERR: Incorrect number of arguments")
            exit()
        response += raw_response[0]
        suffix = ""

        for i in range(1, raw_response[1] + 1):
            reg_address = reg.get(command[i])
            if not reg_address:
                if command[i] == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                else:
                    print("Line " + line_num + ": ERR: Wrong register")
                exit()
            else:
                suffix += reg_address

        for i in range(raw_response[1] + 1, raw_response[1] + raw_response[2] + 1):
            if len(command[i]) == 8:
                suffix += command[i]
            else:
                print("Line " + line_num + ": ERR: Invalid mem_addr")
                exit()
        response += "0"*(21-len(response)-len(suffix)) + suffix

    return response


if __name__ == "__main__":
    print(assemble(input(), 0))
