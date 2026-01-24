import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(last_Digit_Factorial(0), 1)
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)
        self.assertEqual(last_Digit_Factorial(5), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(last_Digit_Factorial(-1), None)
        self.assertEqual(last_Digit_Factorial(6), 0)
        self.assertEqual(last_Digit_Factorial(7), 1)
        self.assertEqual(last_Digit_Factorial(8), 8)
        self.assertEqual(last_Digit_Factorial(9), 9)
        self.assertEqual(last_Digit_Factorial(10), 5)
        self.assertEqual(last_Digit_Factorial(11), 1)
        self.assertEqual(last_Digit_Factorial(12), 6)
        self.assertEqual(last_Digit_Factorial(13), 4)
        self.assertEqual(last_Digit_Factorial(14), 6)
        self.assertEqual(last_Digit_Factorial(15), 1)
        self.assertEqual(last_Digit_Factorial(16), 0)
