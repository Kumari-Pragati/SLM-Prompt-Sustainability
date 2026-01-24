import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_positive_integer(self):
        self.assertTrue(check_integer("123456789"))

    def test_negative_integer(self):
        self.assertTrue(check_integer("-123456789"))

    def test_zero(self):
        self.assertTrue(check_integer("0"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_digit(self):
        for i in range(10):
            self.assertTrue(check_integer(str(i)))

    def test_leading_sign(self):
        self.assertTrue(check_integer("+123456789"))
        self.assertTrue(check_integer("-123456789"))

    def test_leading_non_digit(self):
        for char in ["a", "b", "c", "+", "-", "*", "/"]:
            self.assertFalse(check_integer(char + "123456789"))

    def test_trailing_sign(self):
        self.assertTrue(check_integer("123456789+"))
        self.assertTrue(check_integer("123456789-"))

    def test_trailing_non_digit(self):
        for char in ["a", "b", "c", "+", "-", "*", "/"]:
            self.assertFalse(check_integer("123456789" + char))

    def test_multiple_leading_signs(self):
        self.assertFalse(check_integer("++123456789"))
        self.assertFalse(check_integer("--123456789"))

    def test_multiple_trailing_signs(self):
        self.assertFalse(check_integer("123456789++"))
        self.assertFalse(check_integer("123456789--"))
