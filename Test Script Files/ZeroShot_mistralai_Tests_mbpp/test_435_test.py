import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    def test_last_digit_positive_numbers(self):
        self.assertEqual(last_Digit(12345), 5)
        self.assertEqual(last_Digit(9876), 6)
        self.assertEqual(last_Digit(10203040), 0)
        self.assertEqual(last_Digit(1000000), 0)

    def test_last_digit_negative_numbers(self):
        self.assertEqual(last_Digit(-12345), 5)
        self.assertEqual(last_Digit(-9876), 6)
        self.assertEqual(last_Digit(-10203040), 0)
        self.assertEqual(last_Digit(-1000000), 0)

    def test_last_digit_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_last_digit_floats(self):
        self.assertEqual(last_Digit(123.45), 5)
        self.assertEqual(last_Digit(-123.45), 5)
        self.assertEqual(last_Digit(123.0), 3)
        self.assertEqual(last_Digit(-123.0), 3)
