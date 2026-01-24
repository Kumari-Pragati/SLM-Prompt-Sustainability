import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello World, this is a test string with words of varying lengths."
        expected_output = ["World", "test", "string", "varying", "lengths"]
        self.assertEqual(find_char_long(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(find_char_long(text), expected_output)

    def test_single_word(self):
        text = "Hello"
        expected_output = ["Hello"]
        self.assertEqual(find_char_long(text), expected_output)

    def test_multiple_words(self):
        text = "Hello World, this is a test string with words of varying lengths."
        expected_output = ["World", "this", "test", "string", "varying", "lengths"]
        self.assertEqual(find_char_long(text), expected_output)

    def test_non_alphanumeric_characters(self):
        text = "Hello! World, this is a test string with words of varying lengths."
        expected_output = ["World", "this", "test", "string", "varying", "lengths"]
        self.assertEqual(find_char_long(text), expected_output)
