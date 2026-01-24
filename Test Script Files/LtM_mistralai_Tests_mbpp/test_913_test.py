import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(end_num("hello123"))

    def test_simple_false(self):
        self.assertFalse(end_num("helloworld"))

    def test_empty_string(self):
        self.assertFalse(end_num(""))

    def test_single_digit(self):
        self.assertTrue(end_num("5"))

    def test_multiple_digits(self):
        self.assertTrue(end_num("12345"))

    def test_leading_digits(self):
        self.assertTrue(end_num("1230"))

    def test_trailing_spaces(self):
        self.assertTrue(end_num("hello123 "))

    def test_leading_spaces(self):
        self.assertTrue(end_num(" 123"))

    def test_leading_non_digit(self):
        self.assertFalse(end_num("a123"))

    def test_mixed_case(self):
        self.assertTrue(end_num("HeLLO123"))
