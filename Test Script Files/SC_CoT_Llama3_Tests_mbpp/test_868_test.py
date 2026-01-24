import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(length_Of_Last_Word("Hello World"), 5)

    def test_edge_case_empty_string(self):
        self.assertEqual(length_Of_Last_Word(""), 0)

    def test_edge_case_single_word(self):
        self.assertEqual(length_Of_Last_Word("Hello"), 5)

    def test_edge_case_single_space(self):
        self.assertEqual(length_Of_Last_Word("   "), 0)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(length_Of_Last_Word("Hello  World"), 5)

    def test_edge_case_multiple_spaces_at_end(self):
        self.assertEqual(length_Of_Last_Word("Hello   World"), 5)

    def test_edge_case_multiple_spaces_at_start(self):
        self.assertEqual(length_Of_Last_Word("   Hello World"), 5)

    def test_edge_case_multiple_spaces_at_start_and_end(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World"), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World"), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces_and_no_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World"), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces_and_no_leading_spaces(self):
        self.assertEqual(length_Of_Last_Word("Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces_and_no_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello     World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces_and_no_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces_and_no_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("Hello World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and_end_with_leading_and_trailing_spaces_and_spaces_in_between(self):
        self.assertEqual(length_Of_Last_Word("     Hello   World     "), 5)

    def test_edge_case_multiple_spaces_at_start_and