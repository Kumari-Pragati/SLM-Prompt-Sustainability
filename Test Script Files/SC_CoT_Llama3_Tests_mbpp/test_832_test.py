import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(extract_max("123abc456"), 456)

    def test_edge_case_empty_string(self):
        self.assertIsNone(extract_max(""))

    def test_edge_case_single_digit(self):
        self.assertEqual(extract_max("1"), 1)

    def test_edge_case_multiple_digits(self):
        self.assertEqual(extract_max("123"), 123)

    def test_edge_case_multiple_digits_with_non_digit(self):
        self.assertEqual(extract_max("123abc456"), 456)

    def test_edge_case_multiple_digits_with_non_digit_at_start(self):
        self.assertEqual(extract_max("abc123456"), 456)

    def test_edge_case_multiple_digits_with_non_digit_at_end(self):
        self.assertEqual(extract_max("123456abc"), 456)

    def test_edge_case_multiple_digits_with_non_digit_in_between(self):
        self.assertEqual(extract_max("abc123456def"), 456)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            extract_max(123)
