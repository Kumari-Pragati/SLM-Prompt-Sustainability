import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters("hello"), "Hello ")

    def test_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello WoRld ")

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("hello, world!"), "Hello, WoRld!")

    def test_multiple_words_with_numbers(self):
        self.assertEqual(capitalize_first_last_letters("hello 123 world"), "Hello 123 WoRld ")

    def test_multiple_words_with_punctuation_and_numbers(self):
        self.assertEqual(capitalize_first_last_letters("hello, 123 world!"), "Hello, 123 WoRld!")
