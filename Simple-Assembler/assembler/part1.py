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
            print("Error in line no.", end="")
            print(line_num)
            print("Syntax Error: Invalid Number of Arguments")
            exit()

        else:
            if isa[instruct][1] == "A":
                if "FLAGS" in command:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Illegal use of FLAGS register")
                    exit()

                final_bin += isa[instruct][0] +"00"

                if "$" in command[1:]:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Type B instruction format used in Type A instruction")
                else:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Typo in register name")
                exit()

                for i in range(1, types[isa[instruct][1]]):
                    reg_x = reg.get(command[i])
                    if reg_x is not None:
                        final_bin += reg_x
                    else:
                        print("Error in line no.", end="")
                        print(line_num)
                        print("Syntax Error: Typo in register name")
                        exit()

                return final_bin

            elif isa[instruct][1] == "D":
                if "FLAGS" in command:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Illegal use of FLAGS register")
                    exit()

                final_bin += isa[instruct][0]
                reg_x = reg.get(command[1])

                if reg_x is not None:
                    final_bin += reg_x
                else:
                    print("Error in line no.", end="")
                    print(line_num)
                    if "$" in command[1:]:
                        print("Syntax Error: Type B instruction format used in Type D instruction")
                    else:
                        print("Syntax Error: Typo in register name")
                        exit()

                final_bin += command[2]
                return final_bin

    elif instruct == "mov":
        if len(command) != 3:
            print("Error in line no.", end="")
            print(line_num)
            print("Syntax Error: Invalid Number of Arguments")
            exit()

        else:
            if "FLAGS" in command:
                print("Error in line no.", end="")
                print(line_num)
                print("Syntax Error: Illegal use of FLAGS register")
                exit()

            if "$" in command[2]:
                final_bin += isa[instruct][0][0]
                if command[1] in reg:
                    final_bin += reg[command[1]]
                else:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Typo in register name")
                    exit()
                if int(command[2][1:]) > 255 or int(command[2][1:]) < 0:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Illegal Immediate values")
                    exit()
                else:
                    bin_num = bin(int(command[2][1:]))[2:]
                    while len(bin_num) != 8:
                        bin_num = "0" + bin_num
                    final_bin += bin_num
                return final_bin
            else:
                final_bin += isa[instruct][1][0] + "00000"
                if command[1] in reg:
                    final_bin += reg[command[1]]
                else:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Typo in register name")
                    exit()
                if command[2] in reg:
                    final_bin += reg[command[2]]
                else:
                    print("Error in line no.", end="")
                    print(line_num)
                    print("Syntax Error: Typo in register name")
                    exit()
                return final_bin
    else:
        if isa[instruct] is None:
            print("Error in line no.", end="")
            print(line_num)
            print("Syntax Error: Typo in instruction name")
            exit()
        exit()
