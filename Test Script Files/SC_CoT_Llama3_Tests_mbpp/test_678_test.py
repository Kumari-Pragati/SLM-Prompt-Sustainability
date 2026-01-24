import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_spaces(" "), "")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_spaces("   "), "")

    def test_edge_case_leading_spaces(self):
        self.assertEqual(remove_spaces("   Hello"), "Hello")

    def test_edge_case_trailing_spaces(self):
        self.assertEqual(remove_spaces("Hello   "), "Hello")

    def test_edge_case_multiple_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("   Hello   "), "Hello")

    def test_edge_case_spaces_in_between_words(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_edge_case_spaces_at_the_end_of_string(self):
        self.assertEqual(remove_spaces("Hello World  "), "HelloWorld")

    def test_edge_case_spaces_at_the_start_of_string(self):
        self.assertEqual(remove_spaces("  Hello World"), "HelloWorld")

    def test_edge_case_spaces_in_between_words_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("   Hello World   "), "HelloWorld")

    def test_edge_case_spaces_in_between_words_with_leading_spaces(self):
        self.assertEqual(remove_spaces("  Hello World"), "HelloWorld")

    def test_edge_case_spaces_in_between_words_with_trailing_spaces(self):
        self.assertEqual(remove_spaces("Hello World  "), "HelloWorld")
