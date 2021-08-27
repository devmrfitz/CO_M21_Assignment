#!/usr/bin/env python3

from matplotlib import pyplot as plt

import part1
import part2
import part3


class MemClass(dict):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.cycle = -1
        self.access_log_x = []
        self.access_log_y = []

    def set_cycle(self, cycle: int):
        self.cycle = cycle

    def __getitem__(self, item):
        if self.cycle != -1:
            self.access_log_x.append(self.cycle)
            self.access_log_y.append(int(item, 2))
        return dict.__getitem__(self, item)

    def __setitem__(self, key, value):
        if self.cycle != -1:
            self.access_log_x.append(self.cycle)
            self.access_log_y.append(int(key, 2))
        return dict.__setitem__(self, key, value)


MEM = MemClass()  # A dictionary that has mem_address as keys and the memory as values
hlt = True
for mem_address in range(256):
    if hlt:
        value = input()
        if value == "1001100000000000":
            hlt = False
    else:
        value = "0" * 16
    bin_address = bin(mem_address)[2:]
    bin_address = "0" * (8 - len(bin_address)) + bin_address
    MEM[bin_address] = value

REG = {"000": "0", "001": "0", "010": "0", "011": "0", "100": "1",
       "101": "0", "110": "0", "111": "0"}
for reg in REG:
    REG[reg] = "0" * 16

PC = "0" * 8
x = []
y = []
cycle_number = 0


def main():
    simulators = [part1.simulate, part2.simulate, part3.simulate]
    global REG, MEM, PC, x, y, cycle_number

    MEM.set_cycle(0)
    while MEM[PC] != "1001100000000000":
        for simulator in simulators:
            PCprint = PC
            x.append(cycle_number)
            y.append(int(PC))
            REG, MEM, PC, is_modified = simulator(REG, MEM, PC)
            if type(PC) == list:
                if len(PC) == 2:
                    x.append(cycle_number)
                    y.append(int(PC[1]))
                    PC = PC[0]
                    cycle_number += 1
                else:
                    PC = PC[0]
                    cycle_number += 1
            if is_modified:
                print(PCprint, end=" ")
                for reg in REG:
                    print(REG[reg], end=" ")
                print()
                break
        MEM.set_cycle(MEM.cycle+1)
    MEM.set_cycle(-1)

    print(PC, end=" ")
    for reg in REG:
        print(REG[reg], end=" ")
    print()

    for mem in MEM:
        print(MEM[mem])

    # print(MEM.access_log_x, MEM.access_log_y)
    Bonus(MEM.access_log_x, MEM.access_log_y)


def Bonus(x: list, y: list):
    plt.scatter(x, y)
    plt.xlabel("Cycle Number")
    plt.ylabel("Memory Address")
    plt.title("Bonus")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit()
