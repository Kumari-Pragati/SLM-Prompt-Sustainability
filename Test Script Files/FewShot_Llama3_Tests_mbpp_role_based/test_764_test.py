import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_string_with_no_numbers(self):
        self.assertEqual(number_ctr("abc"), 0)

    def test_string_with_single_number(self):
        self.assertEqual(number_ctr("a1b"), 1)

    def test_string_with_multiple_numbers(self):
        self.assertEqual(number_ctr("123abc"), 3)

    def test_string_with_numbers_and_non_numbers(self):
        self.assertEqual(number_ctr("123abc456"), 6)

    def test_string_with_leading_zeros(self):
        self.assertEqual(number_ctr("012345"), 5)

    def test_string_with_trailing_zeros(self):
        self.assertEqual(number_ctr("123000"), 3)
