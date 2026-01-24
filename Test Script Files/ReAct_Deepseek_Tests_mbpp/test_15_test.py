import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_lowerstring('abcDefGhI'), ['abc', 'Def', 'Gh', 'I'])

    def test_single_letter_words(self):
        self.assertEqual(split_lowerstring('aBcDeF'), ['a', 'BcDeF'])

    def test_empty_string(self):
        self.assertEqual(split_lowerstring(''), [])

    def test_all_lowercase_words(self):
        self.assertEqual(split_lowerstring('abcdefghi'), ['abcdefghi'])

    def test_all_uppercase_words(self):
        self.assertEqual(split_lowerstring('ABCDEFGHI'), ['ABCDEFGHI'])

    def test_mixed_case_words(self):
        self.assertEqual(split_lowerstring('AbCDeFgHi'), ['AbCDeFgHi'])

    def test_numbers_in_string(self):
        self.assertEqual(split_lowerstring('abc123def456'), ['abc', 'def456'])

    def test_special_characters_in_string(self):
        self.assertEqual(split_lowerstring('abc!def@ghi'), ['abc', 'def@ghi'])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(split_lowerstring('abc   def   ghi'), ['abc', 'def', 'ghi'])

    def test_string_with_tabs(self):
        self.assertEqual(split_lowerstring('abc\tdef\tghi'), ['abc', 'def', 'ghi'])

    def test_string_with_newlines(self):
        self.assertEqual(split_lowerstring('abc\ndef\nghi'), ['abc', 'def', 'ghi'])
