import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(last_Digit_Factorial(0), 1)

    def test_small_positive(self):
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)

    def test_large_positive(self):
        self.assertEqual(last_Digit_Factorial(4), 4)
        self.assertEqual(last_Digit_Factorial(5), 0)

    def test_negative(self):
        with self.assertRaises(TypeError):
            last_Digit_Factorial(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            last_Digit_Factorial(3.5)
