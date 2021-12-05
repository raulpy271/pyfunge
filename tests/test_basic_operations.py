from unittest import TestCase

from src.interpreter import BefungeInterpreter
from src import exceptions
from tests.mock.stdout_mock import StdoutMock


class TestAritmethicOperatrions(TestCase):
    def test_sum(self):
        code = '22+.@'
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '4')

    def test_sub(self):
        code = '22-.@'
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '0')

    def test_multiply(self):
        code = '23*.@'
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '6')

    def test_swap(self):
        code = '12\..@'
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '12')

    def test_swap_without_elements(self):
        code = '\@'
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertTrue(err and err == exceptions.EmptyStack)
        self.assertFalse(stdout_mock.read())

    def test_swap_with_only_one_element(self):
        code = '1\..@'
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '01')


