import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'b'))

    def test_edge_case_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_edge_case_key_not_present(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'd'))

    def test_edge_case_key_present_multiple_times(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3, 'b': 4}, 'b'))

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            is_key_present(123, 'a')

    def test_invalid_input_non_str(self):
        with self.assertRaises(TypeError):
            is_key_present({'a': 1, 'b': 2, 'c': 3}, 123)
