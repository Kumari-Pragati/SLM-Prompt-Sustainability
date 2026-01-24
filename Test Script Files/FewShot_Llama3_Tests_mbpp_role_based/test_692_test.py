import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_last_two_digits_positive(self):
        self.assertEqual(last_Two_Digits(12), 12)

    def test_last_two_digits_negative(self):
        self.assertEqual(last_Two_Digits(-12), 12)

    def test_last_two_digits_zero(self):
        self.assertEqual(last_Two_Digits(0), 0)

    def test_last_two_digits_single_digit(self):
        self.assertEqual(last_Two_Digits(1), 1)

    def test_last_two_digits_multiple_digits(self):
        self.assertEqual(last_Two_Digits(123), 21)

    def test_last_two_digits_large_number(self):
        self.assertEqual(last_Two_Digits(123456), 56)

    def test_last_two_digits_invalid_input(self):
        with self.assertRaises(TypeError):
            last_Two_Digits("abc")
