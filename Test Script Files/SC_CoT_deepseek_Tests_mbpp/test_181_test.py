import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_typical_case(self):
        arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'gee')

    def test_single_string(self):
        arr = ['geeksforgeeks']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'geeksforgeeks')

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), '')

    def test_edge_case(self):
        arr = ['abc', 'abcd', 'ab']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'ab')

    def test_invalid_input(self):
        arr = ['abc', 'abcd', 123]
        n = len(arr)
        with self.assertRaises(TypeError):
            common_prefix(arr, n)
