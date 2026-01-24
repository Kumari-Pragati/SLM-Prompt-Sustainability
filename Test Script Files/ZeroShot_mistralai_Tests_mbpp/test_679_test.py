import unittest
from mbpp_679_code import Dict

from 679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_access_key_valid_input(self):
        data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        self.assertEqual(access_key(data, 0), 'value1')
        self.assertEqual(access_key(data, 1), 'value2')
        self.assertEqual(access_key(data, 2), 'value3')

    def test_access_key_invalid_key(self):
        data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        with self.assertRaises(KeyError):
            access_key(data, 4)

    def test_access_key_empty_dict(self):
        data = {}
        with self.assertRaises(KeyError):
            access_key(data, 0)
