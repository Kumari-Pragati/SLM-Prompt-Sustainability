import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_typical_input(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'a'), [1])

    def test_edge_case_key_not_in_dict(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(KeyError):
            access_key(dictionary, 'd')

    def test_edge_case_dict_empty(self):
        dictionary = {}
        with self.assertRaises(IndexError):
            access_key(dictionary, 'a')

    def test_edge_case_key_empty(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key({}, 'a')

    def test_edge_case_dict_and_key_empty(self):
        dictionary = {}
        with self.assertRaises(IndexError):
            access_key(dictionary, '')

    def test_edge_case_key_non_string(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key(dictionary, 1)
