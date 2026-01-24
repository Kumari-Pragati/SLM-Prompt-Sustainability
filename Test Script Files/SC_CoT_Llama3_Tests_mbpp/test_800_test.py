import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_all_spaces(" "), "")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("   "), "")

    def test_edge_case_spaces_at_start_and_end(self):
        self.assertEqual(remove_all_spaces("   Hello World   "), "HelloWorld")

    def test_edge_case_spaces_between_words(self):
        self.assertEqual(remove_all_spaces("Hello   World"), "HelloWorld")

    def test_edge_case_spaces_before_and_after_punctuation(self):
        self.assertEqual(remove_all_spaces("Hello, World!"), "Hello,World!")

    def test_edge_case_spaces_in_punctuation(self):
        self.assertEqual(remove_all_spaces("Hello...World"), "Hello...World")

    def test_edge_case_spaces_in_punctuation_and_word(self):
        self.assertEqual(remove_all_spaces("Hello...World!"), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces(self):
        self.assertEqual(remove_all_spaces("   Hello...World!   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_trailing_spaces(self):
        self.assertEqual(remove_all_spaces("Hello...World!   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_all_spaces("   Hello...World!   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces_and_comma(self):
        self.assertEqual(remove_all_spaces("   Hello...World!,   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_trailing_spaces_and_comma(self):
        self.assertEqual(remove_all_spaces("Hello...World!,   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_and_trailing_spaces_and_comma(self):
        self.assertEqual(remove_all_spaces("   Hello...World!,   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("   Hello...World()   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation_and_word_with_trailing_spaces_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("Hello...World()   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_and_trailing_spaces_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("   Hello...World()   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces_and_comma_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("   Hello...World(),   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation_and_word_with_trailing_spaces_and_comma_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("Hello...World(),   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_and_trailing_spaces_and_comma_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("   Hello...World(),   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces_and_punctuation(self):
        self.assertEqual(remove_all_spaces("   Hello...World!   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_trailing_spaces_and_punctuation(self):
        self.assertEqual(remove_all_spaces("Hello...World!   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_and_trailing_spaces_and_punctuation(self):
        self.assertEqual(remove_all_spaces("   Hello...World!   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces_and_punctuation_and_comma(self):
        self.assertEqual(remove_all_spaces("   Hello...World!,   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_trailing_spaces_and_punctuation_and_comma(self):
        self.assertEqual(remove_all_spaces("Hello...World!,   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_and_trailing_spaces_and_punctuation_and_comma(self):
        self.assertEqual(remove_all_spaces("   Hello...World!,   "), "Hello...World!")

    def test_edge_case_spaces_in_punctuation_and_word_with_leading_spaces_and_punctuation_and_parenthesis(self):
        self.assertEqual(remove_all_spaces("   Hello...World()   "), "Hello...World()")

    def test_edge_case_spaces_in_punctuation