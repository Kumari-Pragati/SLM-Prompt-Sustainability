import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_max("12345"), 5)

    def test_edge_case_single_digit(self):
        self.assertEqual(extract_max("9"), 9)

    def test_boundary_case_max_at_start(self):
        self.assertEqual(extract_max("98765"), 9)

    def test_boundary_case_max_at_end(self):
        self.assertEqual(extract_max("123456"), 6)

    def test_corner_case_multiple_max_values(self):
        self.assertEqual(extract_max("1234554321"), 5)

    def test_corner_case_empty_string(self):
        self.assertIsNone(extract_max(""))

    def test_corner_case_only_non_digit_chars(self):
        self.assertIsNone(extract_max("abcde"))

    def test_corner_case_only_digits(self):
        self.assertEqual(extract_max("1234567890"), 9)
