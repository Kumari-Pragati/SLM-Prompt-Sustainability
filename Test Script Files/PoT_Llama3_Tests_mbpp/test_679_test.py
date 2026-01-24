import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_typical_case(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'a'), 1)

    def test_edge_case_key_not_in_dict(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(KeyError):
            access_key(dictionary, 'd')

    def test_edge_case_dict_empty(self):
        dictionary = {}
        with self.assertRaises(IndexError):
            access_key(dictionary, 'a')

    def test_edge_case_key_type_mismatch(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key(dictionary, 'a.0')

    def test_edge_case_dict_type_mismatch(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key(123, 'a')

    def test_typical_case_multiple_keys(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'b'), 2)

    def test_typical_case_multiple_keys_last_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'c'), 3)
