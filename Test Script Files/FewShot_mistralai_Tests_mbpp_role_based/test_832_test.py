import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(extract_max("1 2 3 4 5"), 5)

    def test_negative_numbers(self):
        self.assertEqual(extract_max("-1 -2 -3 -4 -5"), -1)

    def test_empty_string(self):
        self.assertEqual(extract_max(""), None)

    def test_single_number(self):
        self.assertEqual(extract_max("7"), 7)

    def test_multiple_words(self):
        self.assertEqual(extract_max("apple 123 banana 456"), 456)

    def test_leading_trailing_whitespace(self):
        self.assertEqual(extract_max("  1 2 3   "), 3)

    def test_non_numeric_characters(self):
        self.assertEqual(extract_max("1a2b3c"), None)
