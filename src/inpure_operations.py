from collections import deque
from typing import Union

from src import exceptions

def input_integer_command(stdInput, prompt_digit: str, stack: deque) -> Union[None, Exception] :
    value = stdInput(prompt_digit)
    if value:
        if value.isdigit():
            stack.append(int(value))
        else:
            return exceptions.WrongInput
    else:
        return exceptions.EmptyInput

def input_char_command(stdInput, prompt_char: str, stack: deque) -> Union[None, Exception] :
    value = stdInput(prompt_char)
    if value:
        stack.append(ord(value[0]))
    else:
        return exceptions.EmptyInput

COMMANDS = {
    '&': input_integer_command,
    '~': input_char_command
}
