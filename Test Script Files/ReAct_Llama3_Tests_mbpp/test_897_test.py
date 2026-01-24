import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_case_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))

    def test_edge_case_empty_word(self):
        self.assertFalse(is_Word_Present("Hello World", ""))

    def test_edge_case_word_not_present(self):
        self.assertFalse(is_Word_Present("Hello Universe", "World"))

    def test_edge_case_word_present_at_start(self):
        self.assertTrue(is_Word_Present("World Hello", "World"))

    def test_edge_case_word_present_at_end(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_case_word_present_multiple_times(self):
        self.assertTrue(is_Word_Present("Hello World World", "World"))

    def test_edge_case_word_present_multiple_times_with_spaces(self):
        self.assertTrue(is_Word_Present("Hello World  World", "World"))

    def test_edge_case_word_present_multiple_times_with_spaces_and_punctuation(self):
        self.assertTrue(is_Word_Present("Hello World, World! World", "World")

    def test_edge_case_word_present_multiple_times_with_spaces_and_punctuation_and_uppercase(self):
        self.assertTrue(is_Word_Present("Hello World, World! WORLD", "World")

    def test_edge_case_word_present_multiple_times_with_spaces_and_punctuation_and_uppercase_and_numbers(self):
        self.assertTrue(is_Word_Present("Hello World, World! 123 WORLD", "World")

    def test_edge_case_word_present_multiple_times_with_spaces_and_punctuation_and_uppercase_and_numbers_and_special_chars(self):
        self.assertTrue(is_Word_Present("Hello World, World! 123 WORLD @#%$", "World")
