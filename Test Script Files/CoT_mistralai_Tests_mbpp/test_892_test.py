import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces(' '), ' ')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('   foo   '), ' foo ')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces(' foo   '), 'foo')
        self.assertEqual(remove_spaces('  foo  '), 'foo')

    def test_multiple_words(self):
        self.assertEqual(remove_spaces('foo bar baz'), 'foo bar baz')

    def test_multiple_spaces_between_words(self):
        self.assertEqual(remove_spaces('foo   bar   baz'), 'foo bar baz')

    def test_leading_trailing_spaces_and_multiple_words(self):
        self.assertEqual(remove_spaces(' foo bar   baz   '), 'foobar baz')

    def test_tab_spaces(self):
        self.assertEqual(remove_spaces('\tfoo\tbar\tbaz'), 'foobarbaz')

    def test_mixed_spaces_and_tabs(self):
        self.assertEqual(remove_spaces('foo \tbar \tbaz'), 'foobarbaz')

    def test_multiple_newlines(self):
        self.assertEqual(remove_spaces('\nfoo\n\nbar\nbaz'), 'foobarbaz')

    def test_empty_lines(self):
        self.assertEqual(remove_spaces('\n\n'), '')

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_spaces, 123)
        self.assertRaises(TypeError, remove_spaces, None)
        self.assertRaises(TypeError, remove_spaces, [])
