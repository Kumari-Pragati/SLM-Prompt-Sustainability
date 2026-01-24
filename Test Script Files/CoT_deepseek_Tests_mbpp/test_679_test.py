import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_access_key_typical_case(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 1
        self.assertEqual(access_key(dictionary, key), list(dictionary.values())[key])

    def test_access_key_edge_case_first_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 0
        self.assertEqual(access_key(dictionary, key), list(dictionary.values())[key])

    def test_access_key_edge_case_last_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = len(list(dictionary.values())) - 1
        self.assertEqual(access_key(dictionary, key), list(dictionary.values())[-1])

    def test_access_key_invalid_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = len(list(dictionary.values()))
        with self.assertRaises(IndexError):
            access_key(dictionary, key)

    def test_access_key_invalid_dictionary(self):
        dictionary = 12345
        key = 0
        with self.assertRaises(TypeError):
            access_key(dictionary, key)

    def test_access_key_invalid_key_type(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 'a'
        with self.assertRaises(TypeError):
            access_key(dictionary, key)
