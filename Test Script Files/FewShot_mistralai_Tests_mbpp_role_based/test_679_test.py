import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_valid_key_in_list(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(access_key(data, 'key1'), 'value1')

    def test_invalid_key_in_list(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        with self.assertRaises(KeyError):
            access_key(data, 'non_existent_key')

    def test_empty_list(self):
        data = {}
        with self.assertRaises(KeyError):
            access_key(data, 'key')

    def test_key_not_string(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        with self.assertRaises(TypeError):
            access_key(data, 1)
