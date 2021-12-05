from unittest import TestCase

from src.interpreter import BefungeInterpreter
from tests.mock.stdout_mock import StdoutMock


class TestParserOfGrid(TestCase):
    def test_playfield_have_fixed_size(self):
        code_with_10_size = (
            '012345678.@' + '\n' \
            '012345678' + '\n' \
            '01234567' + '\n' \
            '0123456' + '\n' \
            '' + '\n' \
        )
        interpreter = BefungeInterpreter()
        interpreter.load(code_with_10_size)
        first_len = 0
        first_len = len(interpreter.playfield[0])
        for line in interpreter.playfield[1:]:
            self.assertEqual(first_len, len(line), "All lines should have the same fixed size")

    def test_playfield_have_needded_spaces(self):
        code_without_needded_spaces = (
            '>    v    ' + '\n' \
            '    ' + '\n' \
            '     5    ' + '\n' \
            '     .    ' + '\n' \
            '     @    ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code_without_needded_spaces)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '5')
        self.assertFalse(err)
        

