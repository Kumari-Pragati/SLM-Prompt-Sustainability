import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(456), 4)
        self.assertEqual(first_Digit(789), 7)

    def test_single_digit_numbers(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(5), 5)
        self.assertEqual(first_Digit(9), 9)

    def test_negative_numbers(self):
        self.assertEqual(first_Digit(-123), -1)
        self.assertEqual(first_Digit(-456), -4)
        self.assertEqual(first_Digit(-789), -7)

    def test_large_numbers(self):
        self.assertEqual(first_Digit(1234567890), 1)
        self.assertEqual(first_Digit(9876543210), 9)

    def test_decimal_numbers(self):
        self.assertEqual(first_Digit(123.45), 1)
        self.assertEqual(first_Digit(456.78), 4)
        self.assertEqual(first_Digit(789.10), 7)

    def test_zero_decimal_numbers(self):
        self.assertEqual(first_Digit(0.12), 0)
        self.assertEqual(first_Digit(0.45), 0)
        self.assertEqual(first_Digit(0.78), 0)
