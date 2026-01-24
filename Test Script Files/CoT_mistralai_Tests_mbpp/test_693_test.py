import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces('hello world'), 'hello world')

    def test_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces('hello   world'), 'hello world')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces('   hello world   '), 'hello world')

    def test_multiple_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces('   hello   world   '), 'hello world')

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_single_tab(self):
        self.assertEqual(remove_multiple_spaces('\thello world'), 'hello world')

    def test_multiple_tabs(self):
        self.assertEqual(remove_multiple_spaces('\t\thello   world\t\t'), 'hello world')

    def test_mixed_spaces_and_tabs(self):
        self.assertEqual(remove_multiple_spaces('hello \tworld'), 'hello world')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(123)
