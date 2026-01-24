import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(''), 0)

    def test_single_character_string(self):
        self.assertEqual(number_of_substrings('a'), 1)

    def test_multiple_characters_string(self):
        self.assertEqual(number_of_substrings('abc'), 6)

    def test_long_string(self):
        self.assertEqual(number_of_substrings('xyz1234567890'), 120)

    def test_string_with_spaces(self):
        self.assertEqual(number_of_substrings('hello world'), 22)

    def test_string_with_special_characters(self):
        self.assertEqual(number_of_substrings('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 48)

    def test_string_with_repeated_characters(self):
        self.assertEqual(number_of_substrings('aaa'), 11)

    def test_string_with_long_repeated_characters(self):
        self.assertEqual(number_of_substrings('aaaaaaa'), 66)

    def test_string_with_short_repeated_characters(self):
        self.assertEqual(number_of_substrings('aa'), 3)
