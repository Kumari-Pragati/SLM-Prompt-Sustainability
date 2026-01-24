import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_simple_word_present(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))
        self.assertTrue(is_Word_Present("Hello World", "Hello"))
        self.assertFalse(is_Word_Present("Hello World", "Python"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))
        self.assertFalse(is_Word_Present("", "Hello"))

    def test_word_not_present(self):
        self.assertFalse(is_Word_Present("Hello World", "Python"))
        self.assertFalse(is_Word_Present("Hello World", "Java"))

    def test_multiple_words(self):
        self.assertTrue(is_Word_Present("Hello World Python", "World"))
        self.assertTrue(is_Word_Present("Hello World Python", "Python"))

    def test_single_word(self):
        self.assertTrue(is_Word_Present("Hello", "Hello"))
        self.assertFalse(is_Word_Present("Hello", "World"))
