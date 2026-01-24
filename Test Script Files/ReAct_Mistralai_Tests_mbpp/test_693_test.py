import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_remove_single_space(self):
        self.assertEqual(remove_multiple_spaces('hello world'), 'hello world')

    def test_remove_multiple_spaces_in_beginning(self):
        self.assertEqual(remove_multiple_spaces('   hello world   '), 'hello world')

    def test_remove_multiple_spaces_in_end(self):
        self.assertEqual(remove_multiple_spaces('hello world   '), 'hello world')

    def test_remove_multiple_spaces_in_middle(self):
        self.assertEqual(remove_multiple_spaces('hello   world'), 'hello world')

    def test_remove_multiple_spaces_with_tabs(self):
        self.assertEqual(remove_multiple_spaces('\thello\t world\t'), 'hello world')

    def test_remove_multiple_spaces_with_newlines(self):
        self.assertEqual(remove_multiple_spaces('\nhello\n world\n'), 'hello world')

    def test_remove_multiple_spaces_with_special_characters(self):
        self.assertEqual(remove_multiple_spaces('hello*world'), 'hello*world')

    def test_remove_multiple_spaces_with_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_remove_multiple_spaces_with_single_space_error(self):
        with self.assertRaises(ValueError):
            remove_multiple_spaces('hello world hello world')
