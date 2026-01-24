import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_max("123 456 789"), 789)

    def test_empty_input(self):
        self.assertRaises(ValueError, extract_max, "")

    def test_single_number(self):
        self.assertEqual(extract_max("123"), 123)

    def test_multiple_numbers(self):
        self.assertEqual(extract_max("123 456 789 101112"), 1212)

    def test_non_numeric_input(self):
        self.assertRaises(ValueError, extract_max, "abc def")

    def test_max_value(self):
        self.assertEqual(extract_max("2147483647"), 2147483647)

    def test_min_value(self):
        self.assertEqual(extract_max("-2147483648"), -2147483648)
