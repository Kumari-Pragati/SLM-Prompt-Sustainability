import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_word_present_in_sentence(self):
        self.assertTrue(is_Word_Present("Hello world, Hello", "Hello"))

    def test_word_not_present_in_sentence(self):
        self.assertFalse(is_Word_Present("Hello world, Hello", "World"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "Hello"))

    def test_word_with_spaces(self):
        self.assertTrue(is_Word_Present("Hello there Hello", "Hello there"))

    def test_word_with_special_characters(self):
        self.assertTrue(is_Word_Present("Hello#$%^&*()_", "Hello"))

    def test_word_with_numbers(self):
        self.assertTrue(is_Word_Present("Hello123World", "Hello"))
