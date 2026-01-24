import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):

    def test_typical_case(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'b'), 2)

    def test_edge_case_empty_dictionary(self):
        dictionary = {}
        with self.assertRaises(IndexError):
            access_key(dictionary, 'a')

    def test_boundary_case_single_element_dictionary(self):
        dictionary = {'a': 1}
        self.assertEqual(access_key(dictionary, 0), 'a')

    def test_corner_case_non_string_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key(dictionary, 1.5)

    def test_invalid_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(KeyError):
            access_key(dictionary, 'd')
