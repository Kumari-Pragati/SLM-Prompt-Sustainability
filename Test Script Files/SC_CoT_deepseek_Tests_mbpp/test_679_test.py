import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_typical_case(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 1
        self.assertEqual(access_key(dictionary, key), list(dictionary.values())[key])

    def test_edge_case_first_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 0
        self.assertEqual(access_key(dictionary, key), list(dictionary.values())[key])

    def test_edge_case_last_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = -1
        self.assertEqual(access_key(dictionary, key), list(dictionary.values())[-1])

    def test_invalid_input_key_too_large(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 10
        with self.assertRaises(IndexError):
            access_key(dictionary, key)

    def test_invalid_input_key_too_small(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = -10
        with self.assertRaises(IndexError):
            access_key(dictionary, key)
