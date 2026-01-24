import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_length(''), 0)

    def test_single_character_string(self):
        self.assertEqual(string_length('a'), 1)

    def test_multiple_character_string(self):
        self.assertEqual(string_length('hello'), 5)

    def test_string_with_spaces(self):
        self.assertEqual(string_length('hello world'), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(string_length('hello@world'), 10)
