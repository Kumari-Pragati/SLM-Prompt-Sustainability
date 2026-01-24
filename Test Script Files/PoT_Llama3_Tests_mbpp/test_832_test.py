import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_max("123abc456"), 456)

    def test_edge_case_empty_string(self):
        self.assertIsNone(extract_max(""))

    def test_edge_case_single_digit(self):
        self.assertEqual(extract_max("1"), 1)

    def test_edge_case_multiple_digits(self):
        self.assertEqual(extract_max("123"), 123)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(extract_max(" 123 456"), 456)

    def test_edge_case_non_numeric_input(self):
        self.assertIsNone(extract_max("abc123def456"))

    def test_edge_case_mixed_digits_and_letters(self):
        self.assertEqual(extract_max("123abc456def"), 456)

    def test_edge_case_mixed_digits_and_letters_with_spaces(self):
        self.assertEqual(extract_max(" 123abc 456def"), 456)
