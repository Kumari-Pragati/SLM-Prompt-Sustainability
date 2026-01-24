import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_all_spaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('   foo   '), 'foo')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_all_spaces(' foo   '), 'foo')
        self.assertEqual(remove_all_spaces('  foo'), 'foo')

    def test_tab_spaces(self):
        self.assertEqual(remove_all_spaces('\tfoo\t'), 'foo')

    def test_newline_spaces(self):
        self.assertEqual(remove_all_spaces('\nfoo\n'), 'foo')

    def test_special_characters_and_spaces(self):
        self.assertEqual(remove_all_spaces('foo bar baz'), 'foobarbaz')
