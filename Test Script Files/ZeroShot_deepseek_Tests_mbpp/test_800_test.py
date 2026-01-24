import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_remove_all_spaces_with_single_space(self):
        self.assertEqual(remove_all_spaces('Hello World'), 'HelloWorld')

    def test_remove_all_spaces_with_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('Hello   World'), 'HelloWorld')

    def test_remove_all_spaces_with_tabs(self):
        self.assertEqual(remove_all_spaces('Hello\tWorld'), 'HelloWorld')

    def test_remove_all_spaces_with_newlines(self):
        self.assertEqual(remove_all_spaces('Hello\nWorld'), 'HelloWorld')

    def test_remove_all_spaces_with_mixed_spaces_tabs_and_newlines(self):
        self.assertEqual(remove_all_spaces('Hello\t \nWorld'), 'HelloWorld')

    def test_remove_all_spaces_with_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')
