import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2}, 'a'))
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, 'c'))

    def test_edge_case_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_edge_case_empty_key(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, ''))

    def test_edge_case_non_dict_input(self):
        with self.assertRaises(TypeError):
            is_key_present(123, 'a')

    def test_edge_case_non_str_key(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, 123))

    def test_edge_case_dict_with_non_str_values(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2.5}, 'a'))
