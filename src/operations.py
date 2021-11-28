from collections import deque

def swap_command(stack: deque):
    if len(stack) > 1:
        last = stack.pop()
        before_last = stack.pop()
        stack.append(last)
        stack.append(before_last)
    else:
        last = stack.pop()
        before_last = 0
        stack.append(last)
        stack.append(before_last)

def horizontal_if_command(value):
    if value:
        current_direction = '<'
    else:
        current_direction = '>'
    return current_direction

def vertical_if_command(value):
    if value:
        current_direction = '^'
    else:
        current_direction = 'v'
    return current_direction

ARITMETIC_OPERATIONS = {
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '/': lambda x, y: int(x / y) if y != 0 else 0,
    '%': lambda x, y: int(x % y) if y != 0 else 0,
    '*': lambda x, y: x * y,
    '`': lambda x, y: x > y,
    '\\': swap_command
}

UNARY_OPERATIONS = {
    '!': lambda x: not x
}

IF_OPERATIONS= {
    '_': horizontal_if_command,
    '|': vertical_if_command
}