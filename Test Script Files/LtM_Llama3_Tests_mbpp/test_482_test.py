import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(match("HelloWorld"), 'Yes')

    def test_simple_invalid_input(self):
        self.assertEqual(match("hello"), 'No')

    def test_edge_case_empty_input(self):
        self.assertEqual(match(""), 'No')

    def test_edge_case_single_uppercase_letter(self):
        self.assertEqual(match("A"), 'No')

    def test_edge_case_single_lowercase_letter(self):
        self.assertEqual(match("a"), 'No')

    def test_edge_case_mixed_case_letters(self):
        self.assertEqual(match("HeLlO"), 'No')

    def test_edge_case_all_uppercase_letters(self):
        self.assertEqual(match("HELLO"), 'No')

    def test_edge_case_all_lowercase_letters(self):
        self.assertEqual(match("hello"), 'No')

    def test_edge_case_multiple_uppercase_letters(self):
        self.assertEqual(match("HELLO"), 'No')

    def test_edge_case_multiple_lowercase_letters(self):
        self.assertEqual(match("hello"), 'No')

    def test_edge_case_mixed_case_and_numbers(self):
        self.assertEqual(match("Hello123"), 'No')

    def test_edge_case_mixed_case_and_special_chars(self):
        self.assertEqual(match("Hello!"), 'No')
