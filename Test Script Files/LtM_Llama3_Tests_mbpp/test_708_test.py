import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(Convert("Hello World"), ["Hello", "World"])
    def test_empty_string(self):
        self.assertEqual(Convert(""), [])
    def test_single_word(self):
        self.assertEqual(Convert("Hello"), ["Hello"])
    def test_multiple_spaces(self):
        self.assertEqual(Convert("Hello   World"), ["Hello", "World"])
    def test_multiple_spaces_and_empty_string(self):
        self.assertEqual(Convert("   "), [])
    def test_multiple_spaces_and_single_word(self):
        self.assertEqual(Convert("   Hello"), ["Hello"])
    def test_multiple_spaces_and_multiple_words(self):
        self.assertEqual(Convert("   Hello World"), ["Hello", "World"])
