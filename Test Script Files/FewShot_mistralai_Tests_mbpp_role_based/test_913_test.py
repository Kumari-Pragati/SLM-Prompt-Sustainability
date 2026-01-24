import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_string_with_single_digit_at_end(self):
        self.assertTrue(end_num("Hello1"))

    def test_string_with_multiple_digits_at_end(self):
        self.assertTrue(end_num("Goodbye123"))

    def test_string_with_only_digits_at_end(self):
        self.assertTrue(end_num("9876"))

    def test_string_with_no_digits_at_end(self):
        self.assertFalse(end_num("Hello"))

    def test_string_with_digits_in_middle(self):
        self.assertFalse(end_num("Hello12"))

    def test_string_with_leading_digits(self):
        self.assertFalse(end_num("1Hello"))

    def test_string_with_trailing_non_digit_characters(self):
        self.assertFalse(end_num("Hello#"))
