from unittest import TestCase

from src.interpreter import BefungeInterpreter

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



