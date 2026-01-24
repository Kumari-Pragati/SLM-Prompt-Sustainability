import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):
    def test_simple_input(self):
        self.assertListEqual(Convert("hello world"), ["hello", "world"])

    def test_single_word_input(self):
        self.assertListEqual(Convert("hello"), ["hello"])

    def test_empty_input(self):
        self.assertListEqual(Convert(""), [])

    def test_whitespace_only_input(self):
        self.assertListEqual(Convert("   "), [""])

    def test_multiple_spaces_input(self):
        self.assertListEqual(Convert("hello   world"), ["hello", "world"])

    def test_special_characters_input(self):
        self.assertListEqual(Convert("hello@world"), ["hello@world"])
