import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(last_Digit_Factorial(0), 1)
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)
        self.assertEqual(last_Digit_Factorial(5), 5)
        self.assertEqual(last_Digit_Factorial(6), 6)
        self.assertEqual(last_Digit_Factorial(7), 9)
        self.assertEqual(last_Digit_Factorial(8), 8)
        self.assertEqual(last_Digit_Factorial(9), 9)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(last_Digit_Factorial(-1), None)
        self.assertEqual(last_Digit_Factorial(10), None)
        self.assertEqual(last_Digit_Factorial(20), None)
        self.assertEqual(last_Digit_Factorial(100), None)
        self.assertEqual(last_Digit_Factorial(1000), None)
