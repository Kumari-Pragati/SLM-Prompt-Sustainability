import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_digit(self):
        for digit in range(10):
            self.assertTrue(check_integer(str(digit)))

    def test_multiple_digits(self):
        for num in range(100):
            self.assertTrue(check_integer(str(num)))

    def test_leading_non_digit(self):
        for char in ["+", "-", ".", ","]:
            self.assertFalse(check_integer(f"{char}123"))

    def test_trailing_non_digit(self):
        for char in ["+", "-", ".", ","]:
            self.assertFalse(check_integer("123" + char))

    def test_mixed_non_digit(self):
        for char in ["+", "-", ".", ","]:
            self.assertFalse(check_integer(f"{char}123{char}"))

    def test_zero_length(self):
        self.assertIsNone(check_integer(""))

    def test_negative_numbers(self):
        for num in [-10, -9, -2, -1]:
            self.assertTrue(check_integer(str(num)))

    def test_long_string(self):
        long_string = "0" * 100
        self.assertTrue(check_integer(long_string))
