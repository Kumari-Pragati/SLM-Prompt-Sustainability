import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_max(""), None)

    def test_single_number(self):
        self.assertEqual(extract_max("123"), 123)

    def test_multiple_numbers(self):
        self.assertEqual(extract_max("123 456 789"), 789)

    def test_leading_trailing_whitespace(self):
        self.assertEqual(extract_max("  123   "), 123)

    def test_negative_numbers(self):
        self.assertEqual(extract_max("123 -456 789"), 789)

    def test_numbers_with_non_numeric_characters(self):
        self.assertEqual(extract_max("123a456b789"), None)

    def test_numbers_in_different_orders(self):
        self.assertEqual(extract_max("789 123 456"), 789)

    def test_large_numbers(self):
        self.assertEqual(extract_max("12345678901234567890"), 12345678901234567890)
