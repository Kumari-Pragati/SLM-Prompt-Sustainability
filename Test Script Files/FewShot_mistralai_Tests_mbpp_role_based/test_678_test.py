import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('   abc   '), 'abc')

    def test_string_with_leading_spaces(self):
        self.assertEqual(remove_spaces('  abc '), 'abc')

    def test_string_with_trailing_spaces(self):
        self.assertEqual(remove_spaces('abc  '), 'abc')

    def test_string_with_spaces_in_middle(self):
        self.assertEqual(remove_spaces('abc def ghi'), 'abcdefghi')

    def test_string_with_only_numbers(self):
        self.assertEqual(remove_spaces('123 456'), '123456')
