import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(last_Digit_Factorial(0), 1)
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_edge_cases(self):
        self.assertEqual(last_Digit_Factorial(-1), 1)
        self.assertEqual(last_Digit_Factorial(-2), 2)
        self.assertEqual(last_Digit_Factorial(5), 0)
        self.assertEqual(last_Digit_Factorial(10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Digit_Factorial('a')
        with self.assertRaises(TypeError):
            last_Digit_Factorial(None)
