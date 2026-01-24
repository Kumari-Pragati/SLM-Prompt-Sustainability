import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_to_tuple(''), tuple())

    def test_single_character_string(self):
        self.assertEqual(string_to_tuple('a'), ('a',))

    def test_multiple_characters_string(self):
        self.assertEqual(string_to_tuple('abc'), ('a', 'b', 'c'))

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple('hello world'), ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'))

    def test_string_with_only_spaces(self):
        self.assertEqual(string_to_tuple('   '), (' ',))

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(string_to_tuple(' a b c '), ('a', 'b', 'c'))
