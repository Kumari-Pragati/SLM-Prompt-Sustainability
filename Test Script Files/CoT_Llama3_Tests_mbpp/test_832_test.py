import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(extract_max("123abc456"), 456)

    def test_multiple_numbers(self):
        self.assertEqual(extract_max("123abc456789"), 789)

    def test_single_number(self):
        self.assertEqual(extract_max("123"), 123)

    def test_empty_input(self):
        self.assertRaises(ValueError, extract_max, "")

    def test_non_numeric_input(self):
        self.assertRaises(ValueError, extract_max, "abc123def")

    def test_no_numbers_input(self):
        self.assertRaises(ValueError, extract_max, "abcdef")
