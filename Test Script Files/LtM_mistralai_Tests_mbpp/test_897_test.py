import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(is_Word_Present("hello world", "hello"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "world"))

    def test_empty_word(self):
        self.assertFalse(is_Word_Present("hello world", ""))

    def test_case_sensitivity(self):
        self.assertFalse(is_Word_Present("Hello World", "hello"))

    def test_multiple_words(self):
        self.assertTrue(is_Word_Present("hello world hello again", "hello"))

    def test_word_at_end(self):
        self.assertTrue(is_Word_Present("world", "world"))

    def test_word_at_beginning(self):
        self.assertTrue(is_Word_Present("hello world", "hello"))

    def test_word_in_middle(self):
        self.assertTrue(is_Word_Present("hello world hello", "hello"))

    def test_word_with_punctuation(self):
        self.assertTrue(is_Word_Present("hello, world!", "hello"))

    def test_word_with_numbers(self):
        self.assertTrue(is_Word_Present("hello 123 world", "hello"))
