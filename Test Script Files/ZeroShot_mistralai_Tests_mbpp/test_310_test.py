import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsInstance(string_to_tuple(''), tuple)
        self.assertListEqual(string_to_tuple(''), [])

    def test_single_character(self):
        self.assertIsInstance(string_to_tuple('a'), tuple)
        self.assertListEqual(string_to_tuple('a'), ['a'])

    def test_multiple_characters(self):
        self.assertIsInstance(string_to_tuple('abc'), tuple)
        self.assertListEqual(string_to_tuple('abc'), ['a', 'b', 'c'])

    def test_mixed_characters_and_spaces(self):
        self.assertIsInstance(string_to_tuple('a b c'), tuple)
        self.assertListEqual(string_to_tuple('a b c'), ['a', 'b', 'c'])

    def test_leading_trailing_spaces(self):
        self.assertIsInstance(string_to_tuple(' a b c '), tuple)
        self.assertListEqual(string_to_tuple(' a b c '), ['a', 'b', 'c'])

    def test_only_spaces(self):
        self.assertIsInstance(string_to_tuple('   '), tuple)
        self.assertListEqual(string_to_tuple('   '), [])
