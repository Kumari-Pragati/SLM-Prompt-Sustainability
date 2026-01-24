import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_list("Hello World"), ['Hello', 'World'])

    def test_edge_case_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(string_to_list("Hello"), ['Hello'])

    def test_edge_case_single_space(self):
        self.assertEqual(string_to_list("   "), [])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(string_to_list("Hello   World"), ['Hello', 'World'])

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(string_to_list("   Hello   World   "), ['Hello', 'World'])

    def test_edge_case_multiple_spaces_between_words(self):
        self.assertEqual(string_to_list("Hello   World   Foo"), ['Hello', 'World', 'Foo'])

    def test_edge_case_multiple_spaces_between_words_and_leading_trailing_spaces(self):
        self.assertEqual(string_to_list("   Hello   World   Foo   "), ['Hello', 'World', 'Foo'])
