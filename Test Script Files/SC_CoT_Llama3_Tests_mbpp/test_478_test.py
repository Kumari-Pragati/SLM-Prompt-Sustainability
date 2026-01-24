import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_lowercase('Hello WORLD'), 'WORLD')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_edge_case_all_lowercase(self):
        self.assertEqual(remove_lowercase('abcdefghijklmnopqrstuvwxyz'), '')

    def test_edge_case_all_uppercase(self):
        self.assertEqual(remove_lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_lowercase('Hello World'), 'World')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_lowercase(None)
