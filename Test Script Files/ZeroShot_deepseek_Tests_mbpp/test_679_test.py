import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_access_key_with_valid_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 1
        self.assertEqual(access_key(dictionary, key), list(dictionary)[key])

    def test_access_key_with_invalid_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        key = 5
        with self.assertRaises(IndexError):
            access_key(dictionary, key)

    def test_access_key_with_empty_dictionary(self):
        dictionary = {}
        key = 0
        with self.assertRaises(IndexError):
            access_key(dictionary, key)
