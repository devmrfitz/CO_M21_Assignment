#!/usr/bin/env python3

import sys

import part1
import part2
import part3


def remove_items(input_list: list, item) -> list:
    return [i for i in input_list if i != item]


def main():
    commands = sys.stdin.read().split("\n")

    assemblers = [part1.assemble, part2.assemble, part3.assemble]

    variables = {}

    labels = {}

    # Cleanup
    commands = remove_items(commands, "")
    for index in range(len(commands)):
        commands[index] = " ".join(commands[index].split())

    first_non_var = 0
    while first_non_var < len(commands) and commands[first_non_var].startswith("var"):
        first_non_var += 1

    code_size = len(commands) - first_non_var
    # Store variables
    while commands[0].startswith("var"):
        command_split = commands[0].split(" ")

        command_split = remove_items(command_split, '')
        if len(command_split) != 2:
            print("Line " + str(len(variables)) + ": ERR: Syntax error")
            print(commands[0])
            exit()
        else:
            variables[command_split[1]] = bin(code_size + len(variables))[2:]

            while len(variables[command_split[1]]) < 8:
                variables[command_split[1]] = "0" + variables[command_split[1]]

            commands = commands[1:]
        while not commands[0] and len(commands) != 0:
            commands = commands[1:]

    # Store labels
    for index in range(len(commands)):
        command = commands[index]
        command_split = command.split(" ")
        command_split = remove_items(command_split, '')

        if command_split[0].endswith(":"):
            if command_split[0][:-1].replace('_', "").isalnum():
                labels[command_split[0][:-1]] = bin(index)[2:]

                while len(labels[command_split[0][:-1]]) < 8:
                    labels[command_split[0][:-1]] = "0" + labels[command_split[0][:-1]]

                commands[index] = " ".join(command_split[1:])
            else:
                print("Line " + str(index + len(variables)) + ": ERR: Invalid label name")
                print(command)
                exit()

    for index in range(len(commands) - 1):

        while commands[index].startswith(" "):
            commands[index] = commands[index][1:]

        while commands[index].endswith(" "):
            commands[index] = commands[index][:-1]

        command = commands[index]

        if command.startswith("var"):
            print("Line " + str(index + len(variables)) + ": ERR: var called in-between program")
            print(command)
            exit()

        command_split = command.split(" ")

        command_split = remove_items(command_split, '')

        if command_split[0] == "st" or command_split[0] == "ld":
            if len(command_split) != 3:
                print("Line " + str(index + len(variables)) + ": ERR: Invalid syntax")
                print(command)
                exit()
            if variables.get(command_split[2]):
                command_split[2] = variables.get(command_split[2])
            else:
                print("Line " + str(index + len(variables)) + ": ERR: Variable not found")
                print(command)
                exit()
            command = " ".join(command_split)

        elif command_split[0].startswith("j"):
            if len(command_split) != 2:
                print("Line " + str(index + len(variables)) + ": ERR: Invalid syntax")
                print(command)
                exit()
            if labels.get(command_split[1]):
                command_split[1] = labels.get(command_split[1])
            else:
                print("Line " + str(index + len(variables)) + ": ERR: Label not found")
                print(command)
                exit()
            command = " ".join(command_split)

        if command == "hlt":
            print("Line " + str(index + len(variables)) + ": ERR: HALT found in between")
            print(command)
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
                print(command)
                exit()

    if commands[-1] == "hlt":
        print("1001100000000000", end=" ")
    else:
        print("Line " + str(len(commands) + len(variables) - 1) + ": ERR: Last command isn't HALT")
        print(commands[-1])
        exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit()
