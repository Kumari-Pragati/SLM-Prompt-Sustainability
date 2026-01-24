import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_simple_access(self):
        self.assertEqual(access_key({'a': 1}, 0), 'a')

    def test_empty_dictionary(self):
        with self.assertRaises(IndexError):
            access_key({}, 0)

    def test_negative_key(self):
        self.assertEqual(access_key({'a': 1}, -1), 'a')

    def test_large_key(self):
        with self.assertRaises(IndexError):
            access_key({'a': 1}, 1)

    def test_non_integer_key(self):
        with self.assertRaises(TypeError):
            access_key({'a': 1}, 'a')

    def test_dictionary_with_multiple_keys(self):
        self.assertEqual(access_key({'a': 1, 'b': 2}, 0), 'a')
        self.assertEqual(access_key({'a': 1, 'b': 2}, 1), 'b')
