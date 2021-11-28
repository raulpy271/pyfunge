#!/bin/python3.8

from sys import argv
from src.interpreter import BefungeInterpreter

if __name__ == '__main__':
    befunge_file = argv[1]
    print_queue = '-v' in argv
    code = ''
    with open(befunge_file, 'r') as f:
        code = f.read()
    iterpreter = BefungeInterpreter()
    iterpreter.load(code)
    queue, output, err = iterpreter.run()
    print(output)
    if err:
        raise err()
    if print_queue:
        print(queue)
    

