#!/bin/python3.8

from sys import argv
from src.interpreter import BefungeInterpreter

def print_playfield(playfield):
    result = ''
    for line in playfield:
        result += ''.join(line) + '\n'
    print("Playfield:")
    print(result)

if __name__ == '__main__':
    befunge_file = argv[1]
    verbose = '-v' in argv
    code = ''
    with open(befunge_file, 'r') as f:
        code = f.read()
    iterpreter = BefungeInterpreter()
    iterpreter.load(code)
    stack, err = iterpreter.run()
    if err:
        raise err()
    if verbose:
        print(f"\nStack:\n{stack}")
        print_playfield(iterpreter.playfield)
    

