import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_typical_use_case(self):
        arr = ['flower', 'flow', 'flight']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'fl')

    def test_edge_case(self):
        arr = ['a']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'a')

    def test_boundary_case(self):
        arr = ['', '']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), '')

    def test_invalid_input(self):
        arr = ['flower', 'flow', None]
        n = len(arr)
        with self.assertRaises(TypeError):
            common_prefix(arr, n)

    def test_no_common_prefix(self):
        arr = ['dog', 'racecar', 'car']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), '')
