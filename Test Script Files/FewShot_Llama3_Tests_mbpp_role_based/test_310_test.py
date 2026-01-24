import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_single_word(self):
        self.assertEqual(string_to_tuple("hello"), ("hello",))

    def test_multiple_words(self):
        self.assertEqual(string_to_tuple("hello world"), ("hello", "world"))

    def test_spaces_and_punctuation(self):
        self.assertEqual(string_to_tuple("hello, world!"), ("hello", "world"))

    def test_non_space_characters(self):
        self.assertEqual(string_to_tuple("abcdefg"), ("abcdefg",))

    def test_mixed_case(self):
        self.assertEqual(string_to_tuple("Hello World"), ("Hello", "World"))

    def test_empty_string_with_punctuation(self):
        self.assertEqual(string_to_tuple("..."), ())

    def test_punctuation_only(self):
        self.assertEqual(string_to_tuple("..."), ())
