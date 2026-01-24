import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_typical_use_case(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'b'), 2)

    def test_edge_condition(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 0), 'a')

    def test_boundary_condition(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 2), 'c')

    def test_invalid_input(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(IndexError):
            access_key(dictionary, 3)
