from collections import deque
from random import choice

from src import operations
from src import exceptions


class BefungeInterpreter:
    def __init__(self, output = ''):
        self.stack = deque()
        self.commands = [[]]
        self.current_location = [0, -1]
        self.current_direction = '>'
        self.output = output
        self.string_mode = False
        
    def load(self, code):
        lines = code.split('\n')
        self.commands = list(map(lambda line: list(line), lines))
    
    def get_current_command(self):
        return self.commands[self.current_location[0]][self.current_location[1]]
    
    def next_command(self):
        if self.current_direction == '>':
            self.current_location = self.current_location[0], self.current_location[1] + 1
        elif self.current_direction == '<':
            self.current_location = self.current_location[0], self.current_location[1] - 1
        elif self.current_direction == 'v':
            self.current_location = self.current_location[0] + 1, self.current_location[1]
        elif self.current_direction == '^':
            self.current_location = self.current_location[0] - 1, self.current_location[1]
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
                self.output += str(self.stack.pop())
            elif command == ',':
                value = self.stack.pop()
                self.output += str(bytes([value]), 'ascii')
            elif command == '?':
                random_direction = choice(list('^v><'))
                self.current_direction = random_direction
            elif command == '$':
                self.stack.pop()
            elif command == '#':
                self.next_command()
            elif command == '\\':
                if len(self.stack) > 0:
                    operations.swap_command(self.stack)
                else:
                    err = exceptions.EmptyStack
            elif command == 'p':
                y = self.stack.pop()
                x = self.stack.pop()
                value = self.stack.pop()
                self.commands[y][x] = str(bytes([value]), 'ascii')
            elif command == 'g':
                y = self.stack.pop()
                x = self.stack.pop()
                value =  self.commands[y][x]
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
            elif command == '_':
                if len(self.stack):
                    value = self.stack.pop()
                    if value:
                        self.current_direction = '<'
                    else:
                        self.current_direction = '>'
                else:
                    self.current_direction = '>'
            elif command == '|':
                if len(self.stack):
                    value = self.stack.pop()
                    if value:
                        self.current_direction = '^'
                    else:
                        self.current_direction = 'v'
                else:
                    self.current_direction = 'v'
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
        return self.stack, self.output, err


