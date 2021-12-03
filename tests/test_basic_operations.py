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

class TestMovements(TestCase):
    def test_left_and_rigth(self):
        code = ">21  #@ . <"
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '12')

    def test_up_and_down(self):
        code = (
            'v  @ ' + '\n' \
            '   . ' + '\n' \
            '   1 ' + '\n' \
            '>  ^ ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(code)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1')

    def test_wraps_the_page_down_to_up(self):
        wraps_vertically = (
            'v    > 1.@ ' + '\n' \
            '>    v     ' + '\n' \
            '           ' + '\n' \
            '           ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(wraps_vertically)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1', "The PC should wraps the page vertically")
        self.assertFalse(err)

    def test_wraps_the_page_up_to_down(self):
        wraps_vertically = (
            '     ^     ' + '\n' \
            '     @     ' + '\n' \
            '     .     ' + '\n' \
            '     1     ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(wraps_vertically)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1', "The PC should wraps the page vertically")
        self.assertFalse(err)

    def test_wraps_the_page_rigth_to_left(self):
        wraps_horizontally = (
            '   v       ' + '\n' \
            '@  >     1.' + '\n' \
            '           ' + '\n' \
            '           ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(wraps_horizontally)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1', "The PC should wraps the page horizontally")
        self.assertFalse(err)

    def test_wraps_the_page_left_to_rigth(self):
        wraps_horizontally = (
            '   v       ' + '\n' \
            '.1 <      @' + '\n' \
            '           ' + '\n' \
            '           ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(wraps_horizontally)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1', "The PC should wraps the page horizontally")
        self.assertFalse(err)


class TestConditinals(TestCase):
    def test_horizontal_if(self):
        if_with_true_value = (
            ' 1   v   ' + '\n' \
            '         ' + '\n' \
            '  @.1_0.@' + '\n' \
        )
        if_with_false_value = (
            ' 0   v   ' + '\n' \
            '         ' + '\n' \
            '  @.1_0.@' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(if_with_true_value)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1')

        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(if_with_false_value)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '0')

    def test_vertical_if(self):
        if_with_true_value = (
            'v     > 1.@ ' + '\n' \
            '1           ' + '\n' \
            '>     |     ' + '\n' \
            '      > 0.@ ' + '\n' \
        )
        if_with_false_value = (
            'v     > 1.@ ' + '\n' \
            '0           ' + '\n' \
            '>     |     ' + '\n' \
            '      > 0.@ ' + '\n' \
        )
        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(if_with_true_value)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '1')

        stdout_mock = StdoutMock()
        interpreter = BefungeInterpreter(output=stdout_mock)
        interpreter.load(if_with_false_value)
        stack, err = interpreter.run()
        self.assertEqual(stdout_mock.read(), '0')

