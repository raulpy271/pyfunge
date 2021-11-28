from unittest import TestCase

from src.interpreter import BefungeInterpreter
from src import exceptions

class TestAritmethicOperatrions(TestCase):
    def test_sum(self):
        code = '22+.@'
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '4')

    def test_sub(self):
        code = '22-.@'
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '0')

    def test_multiply(self):
        code = '23*.@'
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '6')

    def test_swap(self):
        code = '12\..@'
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '12')

    def test_swap_without_elements(self):
        code = '\@'
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertTrue(err and err == exceptions.EmptyStack)

    def test_swap_with_only_one_element(self):
        code = '1\..@'
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '01')

class TestMovements(TestCase):
    def test_left_and_rigth(self):
        code = ">21  #@ . <"
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '12')

    def test_up_and_down(self):
        code = (
            'v  @ ' + '\n' \
            '   . ' + '\n' \
            '   1 ' + '\n' \
            '>  ^ ' + '\n' \
        )
        interpreter = BefungeInterpreter()
        interpreter.load(code)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '1')


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
        interpreter = BefungeInterpreter()
        interpreter.load(if_with_true_value)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '1')

        interpreter = BefungeInterpreter()
        interpreter.load(if_with_false_value)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '0')

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
        interpreter = BefungeInterpreter()
        interpreter.load(if_with_true_value)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '1')

        interpreter = BefungeInterpreter()
        interpreter.load(if_with_false_value)
        stack, output, err = interpreter.run()
        self.assertEqual(output, '0')

