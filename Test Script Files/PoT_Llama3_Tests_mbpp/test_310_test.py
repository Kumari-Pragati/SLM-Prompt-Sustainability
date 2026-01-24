import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_to_tuple("Hello World"), ('Hello', 'World'))

    def test_edge_case_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_edge_case_single_space(self):
        self.assertEqual(string_to_tuple(" "), (''))

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(string_to_tuple("   "), (''))

    def test_edge_case_single_char(self):
        self.assertEqual(string_to_tuple("a"), ('a'))

    def test_edge_case_multiple_chars(self):
        self.assertEqual(string_to_tuple("abc"), ('abc'))

    def test_edge_case_punctuation(self):
        self.assertEqual(string_to_tuple("Hello, World!"), ('Hello,', 'World!'))

    def test_edge_case_punctuation_and_spaces(self):
        self.assertEqual(string_to_tuple("Hello, World!   "), ('Hello,', 'World!'))

    def test_edge_case_non_ascii_chars(self):
        self.assertEqual(string_to_tuple("Hello, World! à"), ('Hello,', 'World!', 'à'))

    def test_edge_case_non_ascii_chars_and_spaces(self):
        self.assertEqual(string_to_tuple("Hello, World!   à"), ('Hello,', 'World!', 'à'))
