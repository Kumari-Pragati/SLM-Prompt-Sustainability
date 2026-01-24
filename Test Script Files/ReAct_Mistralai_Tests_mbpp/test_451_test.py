import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_whitespaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_whitespaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces('   hello   '), 'hello')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_whitespaces(' hello '), 'hello')
        self.assertEqual(remove_whitespaces('hello '), 'hello')
        self.assertEqual(remove_whitespaces(' hello\t'), 'hello')

    def test_tab_spaces(self):
        self.assertEqual(remove_whitespaces('hello\tworld'), 'hello world')
        self.assertEqual(remove_whitespaces('\t\t\t'), '')

    def test_newline(self):
        self.assertEqual(remove_whitespaces('\nhello\nworld'), 'hello\nworld')
        self.assertEqual(remove_whitespaces('\n'), '')

    def test_mixed_whitespaces(self):
        self.assertEqual(remove_whitespaces('hello \t world\n'), 'hello world')

    def test_unicode_spaces(self):
        self.assertEqual(remove_whitespaces('\u00A0hello\u200B world'), 'hello world')

    def test_error_non_string(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(123)
