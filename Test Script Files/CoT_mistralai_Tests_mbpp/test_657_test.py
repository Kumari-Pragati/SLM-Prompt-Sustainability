import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(first_Digit(12), 1)
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(1234), 1)
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(123456), 1)
        self.assertEqual(first_Digit(1234567), 1)
        self.assertEqual(first_Digit(12345678), 8)
        self.assertEqual(first_Digit(123456789), 9)
        self.assertEqual(first_Digit(1234567890), 1)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(first_Digit(-1), 0)
        self.assertEqual(first_Digit(-12), 1)
        self.assertEqual(first_Digit(-123), 3)
        self.assertEqual(first_Digit(-1234), 4)
        self.assertEqual(first_Digit(-12345), 5)
        self.assertEqual(first_Digit(-123456), 6)
        self.assertEqual(first_Digit(-1234567), 7)
        self.assertEqual(first_Digit(-12345678), 8)
        self.assertEqual(first_Digit(-123456789), 9)
        self.assertEqual(first_Digit(-1234567890), 1)

    def test_large_numbers(self):
        self.assertEqual(first_Digit(1000000000), 0)
        self.assertEqual(first_Digit(10000000000), 0)
        self.assertEqual(first_Digit(100000000000), 0)
        self.assertEqual(first_Digit(1000000000000), 0)
        self.assertEqual(first_Digit(10000000000000), 0)
        self.assertEqual(first_Digit(100000000000000), 0)
        self.assertEqual(first_Digit(1000000000000000), 0)
        self.assertEqual(first_Digit(10000000000000000), 0)
        self.assertEqual(first_Digit(100000000000000000), 0)
        self.assertEqual(first_Digit(1000000000000000000), 0)
