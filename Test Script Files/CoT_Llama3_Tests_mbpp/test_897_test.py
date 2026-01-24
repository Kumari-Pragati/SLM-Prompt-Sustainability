import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_present_word(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_absent_word(self):
        self.assertFalse(is_Word_Present("Hello World", "Python"))

    def test_present_word_case_insensitive(self):
        self.assertTrue(is_Word_Present("Hello World", "world"))

    def test_absent_word_case_insensitive(self):
        self.assertFalse(is_Word_Present("Hello World", "python"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))

    def test_empty_word(self):
        self.assertFalse(is_Word_Present("Hello World", ""))

    def test_multiple_words(self):
        self.assertTrue(is_Word_Present("Hello World Python", "World"))

    def test_multiple_words_absent(self):
        self.assertFalse(is_Word_Present("Hello World Python", "Java"))
