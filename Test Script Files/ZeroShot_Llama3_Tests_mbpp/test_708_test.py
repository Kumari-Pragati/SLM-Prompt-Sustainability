import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_single_word(self):
        self.assertEqual(Convert("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(Convert("hello world"), ["hello", "world"])

    def test_multiple_spaces(self):
        self.assertEqual(Convert("hello   world"), ["hello", "world"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(Convert("   hello   world   "), ["hello", "world"])

    def test_punctuation(self):
        self.assertEqual(Convert("hello, world!"), ["hello,", "world!"])

    def test_numbers(self):
        self.assertEqual(Convert("hello 123 world"), ["hello", "123", "world"])

    def test_special_characters(self):
        self.assertEqual(Convert("hello @# world"), ["hello", "@#", "world"])
