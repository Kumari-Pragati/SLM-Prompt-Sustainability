import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_position("123abc"), 0)

    def test_no_number(self):
        self.assertIsNone(num_position("abc"))

    def test_multiple_numbers(self):
        self.assertEqual(num_position("abc123def"), 3)

    def test_empty_string(self):
        self.assertIsNone(num_position(""))

    def test_string_with_only_numbers(self):
        self.assertEqual(num_position("12345"), 0)

    def test_string_with_leading_zero(self):
        self.assertEqual(num_position("0123"), 0)

    def test_string_with_trailing_zero(self):
        self.assertEqual(num_position("1230"), 3)

    def test_string_with_multiple_leading_zero(self):
        self.assertEqual(num_position("000123"), 3)

    def test_string_with_multiple_trailing_zero(self):
        self.assertEqual(num_position("123000"), 3)
