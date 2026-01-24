import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_simple_valid_input(self):
        dictionary = {'a': 1, 'b': 2}
        key = 'a'
        self.assertEqual(access_key(dictionary, key), [1])

    def test_edge_empty_input(self):
        dictionary = {}
        key = 'a'
        with self.assertRaises(KeyError):
            access_key(dictionary, key)

    def test_edge_non_existent_key(self):
        dictionary = {'a': 1, 'b': 2}
        key = 'c'
        with self.assertRaises(KeyError):
            access_key(dictionary, key)

    def test_edge_key_type_mismatch(self):
        dictionary = {'a': 1, 'b': 2}
        key = 'a'
        self.assertIsInstance(access_key(dictionary, key), list)

    def test_edge_dictionary_type_mismatch(self):
        dictionary = {'a': 1, 'b': 2}
        key = 'a'
        self.assertIsInstance(access_key(dictionary, key), list)
