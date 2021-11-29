from unittest import TestCase, mock

from src.interpreter import BefungeInterpreter
from src import exceptions

class TestGetIntegerCommand(TestCase):
    def test_get_integer(self):
        code = '& .@'
        inputMock = mock.Mock()
        inputMock.return_value = '1'
        interpreter = BefungeInterpreter(stdInput=inputMock)
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '1')

    def test_get_integer_with_two_digits(self):
        code = '& ..@'
        inputMock = mock.Mock()
        inputMock.return_value = '11'
        interpreter = BefungeInterpreter(stdInput=inputMock)
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '1')
        self.assertEqual(err, exceptions.EmptyStack)

    def test_get_integer_with_empty_input(self):
        code = '& .@'
        inputMock = mock.Mock()
        inputMock.return_value = ''
        interpreter = BefungeInterpreter(stdInput=inputMock)
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(err, exceptions.EmptyInput)

    def test_get_integer_with_non_digit_char(self):
        code = '& .@'
        inputMock = mock.Mock()
        inputMock.return_value = 'A'
        interpreter = BefungeInterpreter(stdInput=inputMock)
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(err, exceptions.WrongInput)

