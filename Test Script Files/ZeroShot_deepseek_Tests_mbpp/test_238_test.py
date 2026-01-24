import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(''), 0)

    def test_single_character_string(self):
        self.assertEqual(number_of_substrings('a'), 1)

    def test_multiple_character_string(self):
        self.assertEqual(number_of_substrings('abc'), 6)

    def test_string_with_duplicates(self):
        self.assertEqual(number_of_substrings('aaa'), 6)

    def test_string_with_special_characters(self):
        self.assertEqual(number_of_substrings('!@#'), 6)
