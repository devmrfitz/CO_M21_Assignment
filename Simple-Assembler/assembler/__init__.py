#!/usr/bin/env python3

import sys

import part1
import part2
import part3


def remove_items(input_list, item):
    return [i for i in input_list if i != item]


commands = sys.stdin.read().split("\n")[:-1]
print(commands)
assemblers = [part1.assemble, part2.assemble, part3.assemble]

variables = {}

labels = {}

commands = remove_items(commands, "")


first_non_var = 0
while first_non_var < len(commands) and commands[first_non_var].startswith("var"):
    first_non_var += 1

code_size = len(commands)-first_non_var
# Store variables
while commands[0].startswith("var"):
    command_split = commands[0].split(" ")
    if len(command_split) != 2:
        print("Line " + str(len(variables)) + ": ERR: Syntax error")
        exit()
    else:
        variables[command_split[1]] = bin(code_size)[2:]

        while len(variables[command_split[1]]) < 8:
            variables[command_split[1]] = "0" + variables[command_split[1]]

        commands = commands[1:]
    while not commands[0] and len(commands) != 0:
        commands = commands[1:]

# Store labels
for index in range(len(commands)):
    command = commands[index]
    command_split = command.split(" ")
    if command_split[0].endswith(":"):
        if command_split[0][:-1].replace('_', "").isalnum():
            labels[command_split[0][:-1]] = bin(index)[2:]

            while len(labels[command_split[0][:-1]]) < 8:
                labels[command_split[0][:-1]] = "0" + labels[command_split[0][:-1]]

            commands[index] = " ".join(command_split)
        else:
            print("Line " + str(index + len(variables)) + ": Invalid label name")
            exit()

for index in range(len(commands) - 1):
    command = commands[index]
    while command.startswith(" "):
        command = command[1:]

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
            response = assembler(command, index + len(variables))
            if response:
                break

        if response:
            print(response)
        else:
            print("Line " + str(index + len(variables)) + ": ERR: COMMAND NOT FOUND")
            exit()

if commands[-1] == "hlt":
    print("10011000000000")
else:
    print("Line " + str(len(commands) + len(variables) - 1) + ": ERR: Last command isn't HALT")
    exit()
