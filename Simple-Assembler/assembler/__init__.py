#!/usr/bin/env python3

import sys

import part1
import part2
import part3

commands = sys.stdin.read().split("\n")[:-1]
assemblers = [part1.assemble, part2.assemble, part3.assemble]

variables = {}

labels = {}

# Store variables
while commands[0].startswith("var"):
    command_split = commands[0].split(" ")
    if len(command_split) != 2:
        print("Line " + str(len(variables)) + ": ERR: Syntax error")
        exit()
    else:
        variables[command_split[1]] = 2 * len(variables) + len(commands)
        commands = commands[1:]
    while not commands[0] and len(commands) != 0:
        commands = commands[1:]

# Store labels
for index in range(len(commands)):
    command = commands[index]
    command_split = command.split(" ")
    if command_split[0].endswith(":"):
        if command_split[0][:-1].replace('_', "").isalnum():
            labels[command_split[0][:-1]] = index
        else:
            print("Line " + str(index + len(variables)) + ": Invalid label name")
            exit()

for index in range(len(commands) - 1):
    command = commands[index]

    if command.startswith("var"):
        print("Line " + str(index + len(variables)) + ": ERR: var called in-between program")
        exit()

    command_split = command.split(" ")
    if command_split[0].endswith(":"):
        command_split = command_split[1:]
        command = " ".join(command_split)

    if command_split[0] == "st" or command_split[0] == "ld":
        if len(command_split) != 3:
            print("Line " + str(index + len(variables)) + ": ERR: Invalid syntax")
            exit()
        if variables.get(command_split[2]):
            command_split[2] = variables.get(command_split[2])
        else:
            print("Line " + str(index + len(variables)) + ": ERR: Variable not found")
            exit()
        command = " ".join(command_split)

    elif command_split[0].startswith("j"):
        if len(command_split) != 2:
            print("Line " + str(index + len(variables)) + ": ERR: Invalid syntax")
            exit()
        if labels.get(command_split[1]):
            command_split[1] = labels.get(command_split[1])
        else:
            print("Line " + str(index + len(variables)) + ": ERR: Label not found")
            exit()
        command = " ".join(command_split)

    if command == "hlt":
        print("Line " + str(index + len(variables)) + ": ERR: HALT found in between")
        exit()
    else:
        response = ""
        for assembler in assemblers:
            response = assembler(command)
            if response:
                break

        if response:
            print(response)
        else:
            print("Line " + str(index + len(variables)) + ": ERR: COMMAND NOT FOUND")
            exit()

if commands[-1] == "hlt":
    print("1001100000000000")
else:
    print("Line " + str(len(commands) + len(variables) - 1) + ": ERR: Last command isn't HALT")
    exit()
