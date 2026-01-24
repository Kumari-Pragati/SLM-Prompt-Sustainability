import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(4567), 4)
        self.assertEqual(first_Digit(8910), 8)

    def test_single_digit_numbers(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(5), 5)
        self.assertEqual(first_Digit(9), 9)

    def test_negative_numbers(self):
        self.assertEqual(first_Digit(-123), -1)
        self.assertEqual(first_Digit(-4567), -4)
        self.assertEqual(first_Digit(-8910), -8)

    def test_large_numbers(self):
        self.assertEqual(first_Digit(1234567890), 1)
        self.assertEqual(first_Digit(9876543210), 9)

    def test_decimal_numbers(self):
        self.assertEqual(first_Digit(123.45), 1)
        self.assertEqual(first_Digit(456.78), 4)
        self.assertEqual(first_Digit(789.01), 7)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            first_Digit('abc')
        with self.assertRaises(TypeError):
            first_Digit(None)
        with self.assertRaises(TypeError):
            first_Digit([1, 2, 3])
