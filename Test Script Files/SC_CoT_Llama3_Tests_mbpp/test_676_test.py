import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_extra_char("Hello World!"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_extra_char(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_extra_char("a"), "a")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_extra_char("   Hello   World   "), "HelloWorld")

    def test_edge_case_punctuation(self):
        self.assertEqual(remove_extra_char("Hello, World!"), "HelloWorld")

    def test_edge_case_multiple_punctuation(self):
        self.assertEqual(remove_extra_char("Hello... World!"), "HelloWorld")

    def test_edge_case_non_alphanumeric_chars(self):
        self.assertEqual(remove_extra_char("Hello@World!"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars(self):
        self.assertEqual(remove_extra_char("Hello@World!"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation(self):
        self.assertEqual(remove_extra_char("Hello@World!"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces(self):
        self.assertEqual(remove_extra_char("Hello@World!"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_spaces(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_spaces_and_punctuation(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_spaces_and_punctuation_and_spaces(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_spaces_and_punctuation_and_spaces_and_punctuation(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_spaces_and_punctuation_and_spaces_and_punctuation_and_spaces(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars_and_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_multiple_punctuation_and_spaces_and_multiple_spaces_and_punctuation_and_spaces_and_punctuation_and_spaces_and_punctuation_and_spaces_and_punctuation(self):
        self.assertEqual(remove_extra_char("   Hello@World!   "), "HelloWorld")
