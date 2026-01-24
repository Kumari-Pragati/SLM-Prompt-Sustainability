import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a sample text with some words of length 4 or more."
        expected_output = ['This', 'sample', 'text', 'some', 'words', 'length', 'or', 'more']
        self.assertEqual(find_char_long(text), expected_output)

    def test_single_word(self):
        text = "Python"
        expected_output = ['Python']
        self.assertEqual(find_char_long(text), expected_output)

    def test_no_words(self):
        text = "No words here!"
        expected_output = []
        self.assertEqual(find_char_long(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(find_char_long(text), expected_output)

    def test_special_characters(self):
        text = "!@#$%^&*()"
        expected_output = []
        self.assertEqual(find_char_long(text), expected_output)

    def test_numbers(self):
        text = "1234567890"
        expected_output = ['1234567890']
        self.assertEqual(find_char_long(text), expected_output)

    def test_mixed_case(self):
        text = "ThIs iS a tEst"
        expected_output = ['ThIs', 'iS', 'a', 'tEst']
        self.assertEqual(find_char_long(text), expected_output)

    def test_multiple_spaces(self):
        text = "This   is a   test"
        expected_output = ['This', 'is', 'a', 'test']
        self.assertEqual(find_char_long(text), expected_output)

    def test_edge_case_4_chars(self):
        text = "abcd"
        expected_output = ['abcd']
        self.assertEqual(find_char_long(text), expected_output)

    def test_edge_case_5_chars(self):
        text = "abcde"
        expected_output = ['abcde']
        self.assertEqual(find_char_long(text), expected_output)
