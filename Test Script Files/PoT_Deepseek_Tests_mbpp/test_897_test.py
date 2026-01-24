import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_case_word_at_start(self):
        self.assertTrue(is_Word_Present("Hello World", "Hello"))

    def test_edge_case_word_at_end(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_case_single_word(self):
        self.assertTrue(is_Word_Present("Hello", "Hello"))

    def test_edge_case_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "Hello"))

    def test_edge_case_empty_word(self):
        self.assertTrue(is_Word_Present("Hello World", ""))

    def test_corner_case_repeated_word(self):
        self.assertTrue(is_Word_Present("Hello World World", "World"))

    def test_corner_case_case_insensitive(self):
        self.assertTrue(is_Word_Present("Hello world", "World"))

    def test_corner_case_special_characters(self):
        self.assertTrue(is_Word_Present("Hello, World!", "World"))

    def test_corner_case_numbers_in_word(self):
        self.assertTrue(is_Word_Present("Hello World123", "World123"))

    def test_corner_case_punctuation_after_word(self):
        self.assertTrue(is_Word_Present("Hello World!", "World"))

    def test_corner_case_punctuation_before_word(self):
        self.assertTrue(is_Word_Present("Hello, World", "World"))
