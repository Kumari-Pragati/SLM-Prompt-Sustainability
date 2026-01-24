import unittest
from mbpp_459_code import remove_uppercase

class TestRemove_Uppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_uppercase('hello world'), 'ello orld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_edge_case_single_character(self):
        self.assertEqual(remove_uppercase('a'), 'a')

    def test_edge_case_all_uppercase(self):
        self.assertEqual(remove_uppercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '')

    def test_edge_case_all_lowercase(self):
        self.assertEqual(remove_uppercase('abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloWorld')

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_uppercase('   hello   world   '),'  ello   orld   ')

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)
