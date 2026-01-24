import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_split("Hello; world, this is a test*"), ['Hello','world, this is a test'])

    def test_edge_case_empty_string(self):
        self.assertEqual(multiple_split(""), [])

    def test_edge_case_single_separator(self):
        self.assertEqual(multiple_split("Hello;"), ['Hello'])

    def test_edge_case_multiple_separators(self):
        self.assertEqual(multiple_split("Hello; world, this is a test*"), ['Hello','world, this is a test'])

    def test_edge_case_separator_at_end(self):
        self.assertEqual(multiple_split("Hello; world, this is a test*"), ['Hello','world, this is a test'])

    def test_edge_case_separator_at_start(self):
        self.assertEqual(multiple_split("; world, this is a test*Hello"), [' world, this is a test*Hello'])

    def test_edge_case_separator_in_middle(self):
        self.assertEqual(multiple_split("Hello; world, this is a test*"), ['Hello','world, this is a test'])

    def test_edge_case_separator_at_end_with_trailing_separator(self):
        self.assertEqual(multiple_split("Hello; world, this is a test*;"), ['Hello','world, this is a test', ''])

    def test_edge_case_separator_at_start_with_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*Hello;"), [' world, this is a test*Hello', ''])

    def test_edge_case_separator_in_middle_with_trailing_separator(self):
        self.assertEqual(multiple_split("Hello; world, this is a test*;"), ['Hello','world, this is a test', ''])

    def test_edge_case_separator_at_end_with_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello"), [' world, this is a test*;Hello'])

    def test_edge_case_separator_at_start_with_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_in_middle_with_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;"), [' world, this is a test*;'])

    def test_edge_case_separator_at_end_with_leading_separator_and_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_at_start_with_leading_separator_and_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_in_middle_with_leading_separator_and_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;"), [' world, this is a test*;'])

    def test_edge_case_separator_at_end_with_leading_separator_and_trailing_separator_and_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_at_start_with_leading_separator_and_trailing_separator_and_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_in_middle_with_leading_separator_and_trailing_separator_and_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;"), [' world, this is a test*;'])

    def test_edge_case_separator_at_end_with_leading_separator_and_trailing_separator_and_leading_separator_and_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_at_start_with_leading_separator_and_trailing_separator_and_leading_separator_and_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello', ''])

    def test_edge_case_separator_in_middle_with_leading_separator_and_trailing_separator_and_leading_separator_and_trailing_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;"), [' world, this is a test*;'])

    def test_edge_case_separator_at_end_with_leading_separator_and_trailing_separator_and_leading_separator_and_trailing_separator_and_leading_separator(self):
        self.assertEqual(multiple_split("; world, this is a test*;Hello;"), [' world, this is a test*;Hello