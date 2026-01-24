import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_typical_word_present(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_typical_word_absent(self):
        self.assertFalse(is_Word_Present("Hello World", "Python"))

    def test_edge_word_at_start(self):
        self.assertTrue(is_Word_Present("Hello World", "Hello"))

    def test_edge_word_at_end(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_word_in_middle(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_word_single_word(self):
        self.assertTrue(is_Word_Present("World", "World"))

    def test_edge_word_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))

    def test_edge_word_empty_word(self):
        self.assertFalse(is_Word_Present("Hello World", ""))

    def test_edge_word_multiple_spaces(self):
        self.assertTrue(is_Word_Present("Hello  World", "World"))

    def test_edge_word_multiple_spaces_and_punctuation(self):
        self.assertTrue(is_Word_Present("Hello, World!", "World"))

    def test_invalid_input_sentence_non_string(self):
        with self.assertRaises(TypeError):
            is_Word_Present(123, "World")

    def test_invalid_input_word_non_string(self):
        with self.assertRaises(TypeError):
            is_Word_Present("Hello World", 123)
