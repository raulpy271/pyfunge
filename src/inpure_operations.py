from collections import deque
from typing import Union

from src import exceptions

def input_integer_command(stdInput, prompt_digit: str, stack: deque) -> Union[None, Exception] :
    value = stdInput(prompt_digit)
    if value:
        if value.isdigit():
            stack.append(int(value[0]))
        else:
            return exceptions.WrongInput
    else:
        return exceptions.EmptyInput
    