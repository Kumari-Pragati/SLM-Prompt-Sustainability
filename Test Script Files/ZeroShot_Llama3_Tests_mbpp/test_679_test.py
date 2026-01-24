import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_access_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'a'), 1)
        self.assertEqual(access_key(dictionary, 'b'), 2)
        self.assertEqual(access_key(dictionary, 'c'), 3)
        self.assertRaises(KeyError, access_key, dictionary, 'd')

    def test_access_key_non_existent_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertRaises(KeyError, access_key, dictionary, 'd')

    def test_access_key_empty_dict(self):
        dictionary = {}
        self.assertRaises(KeyError, access_key, dictionary, 'a')

    def test_access_key_non_dict(self):
        dictionary = 'not a dictionary'
        self.assertRaises(TypeError, access_key, dictionary, 'a')
