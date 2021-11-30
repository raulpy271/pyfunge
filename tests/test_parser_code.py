from unittest import TestCase, mock

from src.interpreter import BefungeInterpreter

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
        first_len = len(interpreter.commands[0])
        for line in interpreter.commands[1:]:
            self.assertEqual(first_len, len(line), "All lines should have the same fixed size")

    def test_playfield_have_needded_spaces(self):
        code_without_needded_spaces = (
            '>    v    ' + '\n' \
            '    ' + '\n' \
            '     5    ' + '\n' \
            '     .    ' + '\n' \
            '     @    ' + '\n' \
        )
        interpreter = BefungeInterpreter()
        interpreter.load(code_without_needded_spaces)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '5')
        self.assertFalse(err)
        

