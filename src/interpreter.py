from collections import deque
from random import choice
from sys import stdout

from src import operations
from src import exceptions
from src import inpure_operations
from src import messages


class BefungeInterpreter:
    def __init__(self, output=stdout, stdInput=input):
        self.stack = deque()
        self.playfield = [[]]
        self.PC = [0, -1]
        self.current_direction = '>'
        self.output = output
        self.string_mode = False
        self.stdInput = stdInput
        
    def load(self, code):
        lines = code.split('\n')
        grid_without_fixed_len = list(map(lambda line: list(line), lines))
        size_of_each_line = map(len, grid_without_fixed_len)
        max_size = max(size_of_each_line)
        grid_with_fixed_len = []
        for line in grid_without_fixed_len:
            remaining_cells = (max_size - len(line))
            spaces = [' '] * remaining_cells
            grid_with_fixed_len.append(line + spaces)
        self.playfield = grid_with_fixed_len
    
    def get_current_command(self):
        if (self.PC[0] < 0 or self.PC[1] < 0 or self.PC[0] >= len(self.playfield) or self.PC[1] >= len(self.playfield[0])):
            raise Exception("Invalid")
        return self.playfield[self.PC[0]][self.PC[1]]
    
    def next_command(self):
        if self.current_direction == '>':
            if (self.PC[1] + 1 >= len(self.playfield[0])):
                self.PC = self.PC[0], 0
            else:
                self.PC = self.PC[0], self.PC[1] + 1
        elif self.current_direction == '<':
            if (self.PC[1] - 1 < 0):
                self.PC = self.PC[0], len(self.playfield[0]) - 1
            else:
                self.PC = self.PC[0], self.PC[1] - 1
        elif self.current_direction == 'v':
            if (self.PC[0] + 1 >= len(self.playfield)):
                self.PC = 0, self.PC[1]
            else:
                self.PC = self.PC[0] + 1, self.PC[1]
        elif self.current_direction == '^':
            if (self.PC[0] - 1 < 0):
                self.PC = len(self.playfield) - 1, self.PC[1]
            else:
                self.PC = self.PC[0] - 1, self.PC[1]
        return self.get_current_command()
    
    def run(self):
        err = None
        while True:
            command = self.next_command()
            if command == "\"":
                self.string_mode = not self.string_mode
            elif self.string_mode:
                self.stack.append(ord(command))
            elif command.isdigit():
                self.stack.append(int(command))
            elif command == '.':
                if len(self.stack):
                    self.output.write(str(self.stack.pop()))
                else:
                    err = exceptions.EmptyStack
                    break
            elif command == ',':
                value = self.stack.pop()
                self.output.write(str(bytes([value]), 'ascii'))
            elif command == '?':
                random_direction = choice(list('^v><'))
                self.current_direction = random_direction
            elif command == '$':
                self.stack.pop()
            elif command in inpure_operations.COMMANDS:
                prompt = messages.PROMPT_MSG[command]
                command = inpure_operations.COMMANDS[command]
                err_input = command(self.stdInput, prompt, self.stack)
                if err_input:
                    err = err_input
                    break
            elif command == '#':
                self.next_command()
            elif command == '\\':
                if len(self.stack) > 0:
                    operations.swap_command(self.stack)
                else:
                    err = exceptions.EmptyStack
                    break
            elif command == 'p':
                y = self.stack.pop()
                x = self.stack.pop()
                value = self.stack.pop()
                self.playfield[y][x] = str(bytes([value]), 'ascii')
            elif command == 'g':
                y = self.stack.pop()
                x = self.stack.pop()
                value =  self.playfield[y][x]
                self.stack.append(ord(value))
            elif command in '><v^':
                self.current_direction = command
            elif command in operations.ARITMETIC_OPERATIONS:
                operation = operations.ARITMETIC_OPERATIONS[command]
                first = self.stack.pop()
                second = self.stack.pop()
                self.stack.append(int(operation(second, first)))
            elif command in operations.UNARY_OPERATIONS:
                operation = operations.UNARY_OPERATIONS[command]
                first = self.stack.pop()
                self.stack.append(int(operation(first)))
            elif command in operations.IF_OPERATIONS: 
                if len(self.stack):
                    value = self.stack.pop()
                    self.current_direction = operations.IF_OPERATIONS[command](value)
                else:
                    err = exceptions.EmptyStack
                    break
            elif command == ':':
                if len(self.stack):
                    value = self.stack.pop()
                    self.stack.append(value)
                    self.stack.append(value)
                else:
                    self.stack.append(0)
            elif command == '@':
                break
            elif command in ' ':
                pass
            else:
                raise Exception(f"No support to {command}")
        return self.stack, err


