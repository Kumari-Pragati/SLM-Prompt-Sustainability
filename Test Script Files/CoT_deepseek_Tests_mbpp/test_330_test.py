import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a sample text with some words"
        expected_output = ['This', 'is', 'a', 'sample', 'text', 'with', 'some', 'words']
        self.assertEqual(find_char(text), expected_output)

    def test_single_word(self):
        text = "Python"
        expected_output = ['Python']
        self.assertEqual(find_char(text), expected_output)

    def test_no_words(self):
        text = "!@#$%^&*()"
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_special_characters(self):
        text = "!@#$%^&*()"
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_numbers_in_text(self):
        text = "123456"
        expected_output = ['123456']
        self.assertEqual(find_char(text), expected_output)

    def test_special_characters_and_numbers(self):
        text = "!@#123$%^&*456()"
        expected_output = ['123', '456']
        self.assertEqual(find_char(text), expected_output)

    def test_multiple_words_of_different_lengths(self):
        text = "This is a sample text with some words of different lengths"
        expected_output = ['This', 'is', 'a', 'sample', 'text', 'with', 'some', 'words', 'of', 'different', 'lengths']
        self.assertEqual(find_char(text), expected_output)
