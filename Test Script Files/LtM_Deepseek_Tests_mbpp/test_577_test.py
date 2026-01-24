import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(last_Digit_Factorial(0), 1)
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)

    def test_edge_cases(self):
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_complex_cases(self):
        self.assertEqual(last_Digit_Factorial(5), 0)
        self.assertEqual(last_Digit_Factorial(6), 0)
        self.assertEqual(last_Digit_Factorial(7), 0)
        self.assertEqual(last_Digit_Factorial(8), 0)
        self.assertEqual(last_Digit_Factorial(9), 0)
