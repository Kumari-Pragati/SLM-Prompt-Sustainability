import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces(' '), ' ')
        self.assertEqual(remove_spaces(' a '), 'a')
        self.assertEqual(remove_spaces(' b '), 'b')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces(' a   b   c   '), 'a b c')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('   a   '), 'a')
        self.assertEqual(remove_spaces(' a   '), 'a')
        self.assertEqual(remove_spaces('   a'), 'a')

    def test_only_spaces(self):
        self.assertEqual(remove_spaces('   '), '')

    def test_special_characters(self):
        self.assertEqual(remove_spaces('a1b2c3'), 'a1b2c3')
        self.assertEqual(remove_spaces('a1 b2 c3'), 'a1b2c3')
        self.assertEqual(remove_spaces('a1 b2 c3 '), 'a1b2c3')

    def test_newlines(self):
        self.assertEqual(remove_spaces('\na\nb\nc'), '\na\nb\nc')
        self.assertEqual(remove_spaces('\na\nb\nc\n'), '\na\nb\nc')
        self.assertEqual(remove_spaces('\na\nb\nc\n '), '\na\nb\nc')

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            remove_spaces(123)
        with self.assertRaises(TypeError):
            remove_spaces(None)
