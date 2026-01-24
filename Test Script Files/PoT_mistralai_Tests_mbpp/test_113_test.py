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

    def test_leading_sign(self):
        for sign in "+-":
            for num in range(100):
                self.assertTrue(check_integer(f"{sign}{str(num)}"))

    def test_zero_length_string(self):
        self.assertIsNone(check_integer("0"))

    def test_leading_zero(self):
        for num in range(100):
            self.assertTrue(check_integer(f"0{str(num)}"))

    def test_trailing_zero(self):
        for num in range(100):
            self.assertTrue(check_integer(f"{str(num)}0"))

    def test_leading_and_trailing_zero(self):
        for num in range(100):
            self.assertTrue(check_integer(f"0{str(num)}0"))

    def test_negative_numbers(self):
        for num in range(-100, 0):
            self.assertTrue(check_integer(f"-{str(num)}"))

    def test_non_integer_input(self):
        for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:'\",.<>?/":
            self.assertFalse(check_integer(char))

    def test_empty_string_as_argument(self):
        self.assertIsNone(check_integer(""))
