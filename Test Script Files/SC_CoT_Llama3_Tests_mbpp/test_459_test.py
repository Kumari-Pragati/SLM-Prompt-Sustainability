import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_uppercase('Hello World'), 'ello world')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_edge_case_single_character(self):
        self.assertEqual(remove_uppercase('A'), '')

    def test_edge_case_multiple_uppercase(self):
        self.assertEqual(remove_uppercase('HELLO WORLD'), 'ello world')

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_uppercase('HeLlO wOrLd'), 'ello world')

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)

    def test_edge_case_non_string_input2(self):
        with self.assertRaises(TypeError):
            remove_uppercase([1, 2, 3])

    def test_edge_case_non_string_input3(self):
        with self.assertRaises(TypeError):
            remove_uppercase({'a': 1, 'b': 2})
