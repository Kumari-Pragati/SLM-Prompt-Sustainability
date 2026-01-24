import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_access_key_with_valid_index(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        expected_output = 'value1'
        self.assertEqual(access_key(data, 0), expected_output)

    def test_access_key_with_invalid_index_raises_KeyError(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        with self.assertRaises(KeyError):
            access_key(data, 3)

    def test_access_key_with_empty_dictionary(self):
        data = {}
        with self.assertRaises(KeyError):
            access_key(data, 0)

    def test_access_key_with_non_integer_index(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        with self.assertRaises(TypeError):
            access_key(data, 'invalid_key')
