import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_position("123abc456"), 0)

    def test_no_number(self):
        self.assertIsNone(num_position("abc"))

    def test_single_number(self):
        self.assertEqual(num_position("1"), 0)

    def test_multiple_numbers(self):
        self.assertEqual(num_position("abc123def456"), 3)

    def test_empty_string(self):
        self.assertIsNone(num_position(""))

    def test_string_with_only_numbers(self):
        self.assertEqual(num_position("123456"), 0)

    def test_string_with_leading_zero(self):
        self.assertEqual(num_position("0123"), 0)
