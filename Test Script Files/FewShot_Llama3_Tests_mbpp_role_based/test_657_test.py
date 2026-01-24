import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(first_Digit(123), 1)

    def test_large_integer(self):
        self.assertEqual(first_Digit(123456789), 9)

    def test_single_digit_integer(self):
        self.assertEqual(first_Digit(1), 1)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            first_Digit(-123)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            first_Digit('abc')
