import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_typical_input(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 'b'
        self.assertEqual(access_key(dictionary, key), 2)

    def test_edge_case_key_not_in_dict(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 'd'
        with self.assertRaises(KeyError):
            access_key(dictionary, key)

    def test_edge_case_dict_empty(self):
        dictionary = {}
        key = 'a'
        with self.assertRaises(KeyError):
            access_key(dictionary, key)

    def test_edge_case_key_empty(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = ''
        with self.assertRaises(TypeError):
            access_key(dictionary, key)

    def test_edge_case_dict_and_key_empty(self):
        dictionary = {}
        key = ''
        with self.assertRaises(TypeError):
            access_key(dictionary, key)

    def test_edge_case_dict_and_key_not_in_dict(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = ''
        with self.assertRaises(TypeError):
            access_key(dictionary, key)
