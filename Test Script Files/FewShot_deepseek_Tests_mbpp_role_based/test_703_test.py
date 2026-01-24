import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'b'))

    def test_edge_case_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_boundary_case_single_key_dict(self):
        self.assertTrue(is_key_present({'a': 1}, 'a'))
        self.assertFalse(is_key_present({'a': 1}, 'b'))

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            is_key_present(None, 'a')

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            is_key_present('not a dict', 'a')
