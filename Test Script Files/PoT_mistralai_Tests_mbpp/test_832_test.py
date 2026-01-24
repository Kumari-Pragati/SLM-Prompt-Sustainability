import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_max("123 456 789"), 987)

    def test_edge_case_single_number(self):
        self.assertEqual(extract_max("1"), 1)

    def test_edge_case_multiple_numbers(self):
        self.assertEqual(extract_max("123 456 789 0"), 987)

    def test_edge_case_empty_string(self):
        self.assertEqual(extract_max(""), None)

    def test_edge_case_no_numbers(self):
        self.assertEqual(extract_max("abc"), None)

    def test_edge_case_leading_trailing_whitespace(self):
        self.assertEqual(extract_max("  123   "), 123)

    def test_edge_case_only_whitespace(self):
        self.assertEqual(extract_max("   "), None)

    def test_corner_case_leading_zero(self):
        self.assertEqual(extract_max("001"), 1)

    def test_corner_case_leading_zeros(self):
        self.assertEqual(extract_max("0001"), 1)
