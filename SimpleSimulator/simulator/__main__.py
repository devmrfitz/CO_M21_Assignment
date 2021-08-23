#!/usr/bin/env python3

import sys

import part1
import part2
import part3


def remove_items(input_list: list, item) -> list:
    return [i for i in input_list if i != item]


assembled_code = remove_items(sys.stdin.read().split("\n"), '')

MEM = {}  # A dictionary that has mem_address as keys and the memory as values
for mem_address in range(256):
    if len(assembled_code) > mem_address:
        value = assembled_code[mem_address]
    else:
        value = "0" * 16
    bin_address = bin(mem_address)[2:]
    bin_address = "0" * (8 - len(bin_address)) + bin_address
    MEM[bin_address] = value


REG = {"R0": "0", "R1": "0", "R2": "0", "R3": "0", "R4": "1",
       "R5": "0", "R6": "0", "FLAGS": "0"}
for reg in REG:
    REG[reg] = "0" * 16

PC = "0" * 8


def main():
    simulators = [part1.simulate, part2.simulate, part3.simulate]
    simulators = [part3.simulate]
    global REG, MEM, PC

    while MEM[PC] != "1001100000000000":
        for simulator in simulators:
            PCprint = PC
            REG, MEM, PC, is_modified = simulator(REG, MEM, PC)
            if is_modified:
                print(PCprint, end=" ")
                for reg in REG:
                    print(REG[reg], end=" ")
                print()
                break
    print(PC, end=" ")
    for reg in REG:
        print(REG[reg], end=" ")
    print()

    for mem in MEM:
        print(MEM[mem])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit()
