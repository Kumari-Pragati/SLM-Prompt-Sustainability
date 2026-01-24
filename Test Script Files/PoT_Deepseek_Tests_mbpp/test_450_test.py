import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_string(["abc", "defg", "hijk"], 3), ["abc", "hijk"])

    def test_edge_case_empty_string(self):
        self.assertEqual(extract_string([""], 0), [""])

    def test_boundary_case_single_character(self):
        self.assertEqual(extract_string(["a"], 1), ["a"])

    def test_boundary_case_empty_list(self):
        self.assertEqual(extract_string([], 3), [])

    def test_corner_case_long_strings(self):
        self.assertEqual(extract_string(["abcdefgh"], 8), ["abcdefgh"])

    def test_corner_case_long_strings_with_short_ones(self):
        self.assertEqual(extract_string(["abc", "defghijk"], 3), ["abc"])

    def test_corner_case_long_strings_with_short_ones_and_empty(self):
        self.assertEqual(extract_string(["abc", "defghijk", ""], 3), ["abc", ""])
