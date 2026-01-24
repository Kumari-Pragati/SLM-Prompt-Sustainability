import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_word_present(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_word_absent(self):
        self.assertFalse(is_Word_Present("Hello World", "Python"))

    def test_word_present_at_start(self):
        self.assertTrue(is_Word_Present("Hello World", "Hello"))

    def test_word_present_at_end(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_word_present_multiple_times(self):
        self.assertTrue(is_Word_Present("Hello World World", "World"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))

    def test_word_with_spaces(self):
        self.assertTrue(is_Word_Present("Hello  World", "World"))

    def test_word_with_punctuation(self):
        self.assertTrue(is_Word_Present("Hello, World!", "World"))

    def test_word_with_non_ascii_characters(self):
        self.assertTrue(is_Word_Present("Hello, World!", "World"))
