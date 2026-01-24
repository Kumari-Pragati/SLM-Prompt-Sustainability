import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sort_String('cba'), 'abc')

    def test_empty_string(self):
        self.assertEqual(sort_String(''), '')

    def test_single_character_string(self):
        self.assertEqual(sort_String('a'), 'a')

    def test_string_with_repeated_characters(self):
        self.assertEqual(sort_String('aaaabbbb'), 'abababab')

    def test_string_with_special_characters(self):
        self.assertEqual(sort_String('abc!@#'), '!@#abc')

    def test_string_with_numbers(self):
        self.assertEqual(sort_String('1234567890'), '0123456789')

    def test_string_with_mixed_characters_and_numbers(self):
        self.assertEqual(sort_String('a1b2c3'), '123abc')
