import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(remove_all_spaces('Hello World'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_string_with_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('Hello   World'), 'HelloWorld')

    def test_string_with_tabs(self):
        self.assertEqual(remove_all_spaces('Hello\tWorld'), 'HelloWorld')

    def test_string_with_newlines(self):
        self.assertEqual(remove_all_spaces('Hello\nWorld'), 'HelloWorld')

    def test_string_with_mixed_spaces_tabs_and_newlines(self):
        self.assertEqual(remove_all_spaces('Hello\t\nWorld'), 'HelloWorld')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_all_spaces('Hello@#$World'), 'Hello@#$World')

    def test_string_with_numbers(self):
        self.assertEqual(remove_all_spaces('Hello123World456'), 'Hello123World456')

    def test_string_with_mixed_characters_and_numbers(self):
        self.assertEqual(remove_all_spaces('Hello123 World456'), 'Hello123World456')
