#!/usr/bin/env python3

import sys

import part1
import part2
import part3

commands = sys.stdin.read().split("\n")
assemblers = [part1.assemble, part2.assemble, part3.assemble]

for command in commands:
    response = ""
    for assembler in assemblers:
        response = assembler(command)
        if response:
            break

    if response:
        print(response)
    else:
        # Handle error (COMMAND NOT FOUND)
        pass
