import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_char("Hello World, this is a test string"), ["Hello", "World", "this", "test", "string"])

    def test_empty_string(self):
        self.assertEqual(find_char(""), [])

    def test_single_word(self):
        self.assertEqual(find_char("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(find_char("Hello World, this is a test string again"), ["Hello", "World", "this", "is", "a", "test", "string", "again"])

    def test_non_alphanumeric_characters(self):
        self.assertEqual(find_char("Hello! World, this is a test string"), ["Hello", "World", "this", "is", "a", "test", "string"])

    def test_punctuation_at_end(self):
        self.assertEqual(find_char("Hello, World!"), ["Hello", "World"])

    def test_punctuation_in_middle(self):
        self.assertEqual(find_char("Hello, World! this is a test string"), ["Hello", "World", "this", "is", "a", "test", "string"])
