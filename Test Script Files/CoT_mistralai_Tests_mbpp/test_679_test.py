import unittest
from mbpp_679_code import dict
from six.moves.builtins import range

class TestAccessKey(unittest.TestCase):

    def test_empty_dictionary(self):
        with self.assertRaises(KeyError):
            access_key(dict(), 0)

    def test_single_item_dictionary(self):
        result = access_key(dict(key1='value1'), 'key1')
        self.assertEqual(result, 'value1')

    def test_multiple_items_dictionary(self):
        result = access_key(dict(key1='value1', key2='value2'), 'key2')
        self.assertEqual(result, 'value2')

    def test_negative_key(self):
        with self.assertRaises(KeyError):
            access_key(dict(key1='value1'), -1)

    def test_non_existent_key(self):
        with self.assertRaises(KeyError):
            access_key(dict(key1='value1'), 'key3')

    def test_key_not_integer(self):
        with self.assertRaises(TypeError):
            access_key(dict(key1='value1'), 3.14)

    def test_key_out_of_range(self):
        with self.assertRaises(IndexError):
            access_key(dict(key1='value1', key2='value2'), len(dict(key1='value1', key2='value2')) + 1)
