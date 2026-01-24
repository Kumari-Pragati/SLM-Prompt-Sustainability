import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(string_to_list(""), [])

    def test_single_word(self):
        self.assertListEqual(string_to_list("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertListEqual(string_to_list("hello world"), ["hello", "world"])

    def test_leading_trailing_whitespace(self):
        self.assertListEqual(string_to_list("   hello world   "), ["hello", "world"])

    def test_whitespace_in_middle(self):
        self.assertListEqual(string_to_list("hello world   "), ["hello", "world"])

    def test_non_alphanumeric_characters(self):
        self.assertListEqual(string_to_list("hello@world"), ["hello", "world"])

    def test_multiple_non_alphanumeric_characters(self):
        self.assertListEqual(string_to_list("hello@123world"), ["hello", "123", "world"])

    def test_empty_word(self):
        self.assertListEqual(string_to_list("   hello   "), ["", "hello", ""])

    def test_only_whitespace(self):
        self.assertListEqual(string_to_list("   "), [])

    def test_large_input(self):
        large_string = "a" * 1000
        self.assertListEqual(string_to_list(large_string), [large_string[i:i+1] for i in range(len(large_string))])

    def test_input_with_only_non_alphanumeric_characters(self):
        self.assertListEqual(string_to_list("@#$%^&*()_+-="), ["@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "="])
