import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_remove_spaces_typical_case(self):
        self.assertEqual(remove_all_spaces('Hello World'), 'HelloWorld')

    def test_remove_spaces_edge_case(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_remove_spaces_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('Hello   World'), 'HelloWorld')

    def test_remove_spaces_special_characters(self):
        self.assertEqual(remove_all_spaces('Hello! World!'), 'Hello!World!')

    def test_remove_spaces_numbers(self):
        self.assertEqual(remove_all_spaces('1 2 3 4'), '1234')

    def test_remove_spaces_special_spaces(self):
        self.assertEqual(remove_all_spaces('\t\n Hello \t\n World \t\n'), 'HelloWorld')
