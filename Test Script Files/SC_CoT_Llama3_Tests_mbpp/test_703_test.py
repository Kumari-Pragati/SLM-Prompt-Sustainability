import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2}, 'a'))
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, 'c'))

    def test_edge_cases(self):
        self.assertTrue(is_key_present({}, 'a'))
        self.assertFalse(is_key_present({}, 'b'))

    def test_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            is_key_present(123, 'a')

    def test_non_string_key(self):
        with self.assertRaises(TypeError):
            is_key_present({'a': 1, 'b': 2}, 123)

    def test_dict_with_non_string_values(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 'b'}, 'a'))
        self.assertFalse(is_key_present({'a': 1, 'b': 'b'}, 'c'))
