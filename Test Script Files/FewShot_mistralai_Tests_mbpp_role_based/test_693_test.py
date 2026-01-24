import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces('a b'), 'a b')

    def test_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces('a   b   c   '), 'a b c')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces('   a   '), 'a')

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_only_spaces(self):
        self.assertEqual(remove_multiple_spaces('   '), '')

    def test_special_characters(self):
        self.assertEqual(remove_multiple_spaces('a!b c#d'), 'a!b c#d')
