import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_extra_char("Hello World!"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_extra_char(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_extraChar("a"), "a")

    def test_edge_case_multiple_chars(self):
        self.assertEqual(remove_extraChar("abc"), "abc")

    def test_edge_case_non_alphanumeric_chars(self):
        self.assertEqual(remove_extraChar("Hello! World"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars(self):
        self.assertEqual(remove_extraChar("Hello!@# World"), "HelloWorld")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_extraChar("Hello   World"), "HelloWorld")

    def test_edge_case_multiple_punctuation(self):
        self.assertEqual(remove_extraChar("Hello... World"), "HelloWorld")

    def test_edge_case_multiple_punctuation_and_spaces(self):
        self.assertEqual(remove_extraChar("Hello...   World"), "HelloWorld")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_extra_char(123)
