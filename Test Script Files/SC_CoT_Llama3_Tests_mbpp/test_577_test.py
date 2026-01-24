import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(last_Digit_Factorial(0), 1)

    def test_small_numbers(self):
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_large_numbers(self):
        self.assertEqual(last_Digit_Factorial(5), 0)
        self.assertEqual(last_Digit_Factorial(10), 0)
        self.assertEqual(last_Digit_Factorial(20), 0)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            last_Digit_Factorial(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            last_Digit_Factorial(3.5)
