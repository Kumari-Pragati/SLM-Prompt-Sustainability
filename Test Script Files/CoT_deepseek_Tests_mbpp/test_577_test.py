import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):

    def test_last_Digit_Factorial_typical_cases(self):
        self.assertEqual(last_Digit_Factorial(0), 1)
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_last_Digit_Factorial_edge_cases(self):
        self.assertEqual(last_Digit_Factorial(5), 0)
        self.assertEqual(last_Digit_Factorial(6), 0)
        self.assertEqual(last_Digit_Factorial(7), 0)
        self.assertEqual(last_Digit_Factorial(8), 0)
        self.assertEqual(last_Digit_Factorial(9), 0)

    def test_last_Digit_Factorial_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Digit_Factorial('a')
        with self.assertRaises(ValueError):
            last_Digit_Factorial(-1)
