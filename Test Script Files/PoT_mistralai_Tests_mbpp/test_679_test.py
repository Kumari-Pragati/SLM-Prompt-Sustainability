import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(access_key({'a': 1, 'b': 2, 'c': 3}, 1), 1)
        self.assertEqual(access_key({'a': 1, 'b': 2, 'c': 3}, 2), 2)
        self.assertEqual(access_key({'a': 1, 'b': 2, 'c': 3}, 3), 3)

    def test_edge_case_empty_dict(self):
        self.assertRaises(KeyError, access_key, {}, 0)

    def test_edge_case_non_existent_key(self):
        self.assertRaises(KeyError, access_key, {'a': 1, 'b': 2, 'c': 3}, 4)

    def test_edge_case_key_is_not_integer(self):
        self.assertRaises(TypeError, access_key, {'a': 1, 'b': 2, 'c': 3}, 'a')
