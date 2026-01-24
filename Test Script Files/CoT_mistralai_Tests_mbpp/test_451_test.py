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
        self.assertEqual(remove_whitespaces(' hello '), 'hello')

    def test_tab_spaces(self):
        self.assertEqual(remove_whitespaces('\thello\t'), 'hello')

    def test_newline(self):
        self.assertEqual(remove_whitespaces('\nhello\n'), 'hello')

    def test_mixed_whitespace(self):
        self.assertEqual(remove_whitespaces(' \t\nhello \t\n '), 'hello')

    def test_only_whitespace(self):
        self.assertEqual(remove_whitespaces('   \t\n  '), '')

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_whitespaces, 123)
