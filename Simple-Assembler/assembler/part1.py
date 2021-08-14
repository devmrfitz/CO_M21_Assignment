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
            print("Error in Line " + str(line_num) + " Syntax Error: Invalid Number of Arguments")
            print(" ".join(command))
            exit()

        else:
            if isa[instruct][1] == "A":
                if "FLAGS" in command:
                    print("Error in Line " + str(line_num) + " Syntax Error: Illegal use of FLAGS register")
                    print(" ".join(command))
                    exit()

                final_bin += isa[instruct][0] + "00"

                if "$" in command[1:]:
                    print("Error in Line" + str(line_num) + " Syntax Error: Type B instruction format used in Type A instruction")
                    print(" ".join(command))

                for i in range(1, types[isa[instruct][1]]):
                    reg_x = reg.get(command[i])
                    if reg_x is not None:
                        final_bin += reg_x
                    else:
                        print("Error in Line " + str(line_num) + " Syntax Error: Typo in register name")
                        print(" ".join(command))
                        exit()

                return final_bin

            elif isa[instruct][1] == "D":
                if "FLAGS" in command:
                    print("Error in Line " + str(line_num) + "Syntax Error: Illegal use of FLAGS register")
                    print(" ".join(command))
                    exit()

                final_bin += isa[instruct][0]
                reg_x = reg.get(command[1])

                if reg_x is not None:
                    final_bin += reg_x
                else:

                    if "$" in command[1:]:
                        print("Error in Line " + str(line_num) + " Syntax Error: Type B instruction format used in Type D instruction")
                        print(" ".join(command))
                        exit()
                    else:
                        print("Error in Line " + str(line_num) + " Syntax Error: Typo in register name")
                        print(" ".join(command))
                        exit()

                final_bin += command[2]
                return final_bin

    elif instruct == "mov":
        if len(command) != 3:
            print("Error in line no." + str(line_num) + "Syntax Error: Invalid Number of Arguments")
            print(" ".join(command))
            exit()

        else:

            if "$" in command[2]:
                final_bin += isa[instruct][0][0]
                if command[1] in reg:
                    final_bin += reg[command[1]]
                else:
                    print("Error in Line " + str(line_num) + " Syntax Error: Typo in register name")
                    print(" ".join(command))
                    exit()
                if command[2][1:].isnumeric():
                    if int(command[2][1:]) > 255 or int(command[2][1:]) < 0:
                        print("Error in Line " + str(line_num) + "Syntax Error: Illegal Immediate values")
                        print(" ".join(command))
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
                elif command[1] == "FLAGS":
                    print("Error in Line " + str(line_num) + " Syntax Error: Illegal use of FLAGS register")
                    print(" ".join(command))
                    exit()
                else:
                    print("Error in Line " + str(line_num) + " Syntax Error: Typo in register name")
                    print(" ".join(command))
                    exit()
                if command[2] in reg:
                    final_bin += reg[command[2]]
                elif command[2] == "FLAGS":
                    final_bin += "111"
                else:
                    print("Error in Line " + str(line_num) + " Syntax Error: Typo in register name")
                    print(" ".join(command))
                    exit()
                return final_bin
    else:
        return ""
