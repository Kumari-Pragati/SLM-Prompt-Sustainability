import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_access_key_typical_case(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 1
        self.assertEqual(access_key(dictionary, key), list(dictionary)[key])

    def test_access_key_edge_case_empty_dictionary(self):
        dictionary = {}
        key = 0
        self.assertRaises(IndexError, access_key, dictionary, key)

    def test_access_key_edge_case_large_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 10
        self.assertRaises(IndexError, access_key, dictionary, key)

    def test_access_key_edge_case_negative_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = -1
        self.assertRaises(IndexError, access_key, dictionary, key)
