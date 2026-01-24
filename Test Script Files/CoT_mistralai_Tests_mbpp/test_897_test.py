import unittest
from897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_present_word(self):
        self.assertTrue(is_Word_Present("Hello world, hello again", "hello"))

    def test_absent_word(self):
        self.assertFalse(is_Word_Present("Hello world, hello again", "goodbye"))

    def test_case_sensitivity(self):
        self.assertFalse(is_Word_Present("Hello world, hello again", "Hello"))
        self.assertTrue(is_Word_Present("Hello world, hello again", "hello"))

    def test_empty_string(self):
        self.assertFalse(is_Word_Present("", "word"))

    def test_single_word_sentence(self):
        self.assertTrue(is_Word_Present("hello", "hello"))
        self.assertFalse(is_Word_Present("hello", "world"))

    def test_multiple_spaces(self):
        self.assertTrue(is_Word_Present(" Hello world, hello again ", "hello"))

    def test_leading_trailing_spaces(self):
        self.assertTrue(is_Word_Present(" Hello world, hello again ", "hello"))
        self.assertTrue(is_Word_Present(" Hello world, hello again ", "world"))

    def test_empty_word(self):
        self.assertFalse(is_Word_Present("Hello world, hello again", ""))
