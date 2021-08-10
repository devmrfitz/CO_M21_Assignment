#!/usr/bin/env python3

import sys

import part1
import part2
import part3

commands = sys.stdin.read().split("\n")
assemblers = [part1.assemble, part2.assemble, part3.assemble]

for command in commands[:-1]:
    if command == "hlt":
        print("ERR: HALT found in between")
        pass
    else:
        response = ""
        for assembler in assemblers:
            response = assembler(command)
            if response:
                break

        if response:
            print(response)
        else:
            print("ERR: COMMAND NOT FOUND")
            pass

if commands[-1] == "hlt":
    print("1001100000000000")
else:
    print("ERR: Last command isn't HALT")
    pass
