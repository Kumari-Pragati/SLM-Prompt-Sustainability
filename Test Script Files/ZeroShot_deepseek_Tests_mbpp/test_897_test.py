import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_word_present(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_word_not_present(self):
        self.assertFalse(is_Word_Present("Hello World", "Universe"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "Hello"))

    def test_word_present_at_start(self):
        self.assertTrue(is_Word_Present("Hello World", "Hello"))

    def test_word_present_at_end(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_case_sensitivity(self):
        self.assertFalse(is_Word_Present("Hello World", "world"))
