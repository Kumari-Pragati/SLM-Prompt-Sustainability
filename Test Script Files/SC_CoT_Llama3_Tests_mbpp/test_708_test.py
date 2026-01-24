import unittest
from mbpp_708_code import Convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Convert("Hello World"), ["Hello", "World"])

    def test_empty_string(self):
        self.assertEqual(Convert(""), [])

    def test_single_word(self):
        self.assertEqual(Convert("Hello"), ["Hello"])

    def test_multiple_spaces(self):
        self.assertEqual(Convert("Hello   World"), ["Hello", "World"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(Convert("   Hello   World   "), ["Hello", "World"])

    def test_multiple_sentences(self):
        self.assertEqual(Convert("Hello World, this is a test"), ["Hello", "World,", "this", "is", "a", "test"])

    def test_punctuation(self):
        self.assertEqual(Convert("Hello, World!"), ["Hello,", "World!"])

    def test_numbers(self):
        self.assertEqual(Convert("Hello 123 World"), ["Hello", "123", "World"])

    def test_special_characters(self):
        self.assertEqual(Convert("Hello * World"), ["Hello", "World"])

    def test_empty_input_list(self):
        self.assertEqual(Convert("   "), [""])

    def test_empty_input_string(self):
        self.assertEqual(Convert(""), [])
