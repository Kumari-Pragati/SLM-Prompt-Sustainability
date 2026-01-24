import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_input(self):
        self.assertListEqual(small_nnum([1, 2, 3, 4, 5], 2), [1, 2])
        self.assertListEqual(small_nnum([10, 20, 30, 40, 50], 3), [10, 20, 30])

    def test_edge_input(self):
        self.assertListEqual(small_nnum([], 1), [])
        self.assertListEqual(small_nnum([1], 1), [1])
        self.assertListEqual(small_nnum([1, 2], 2), [1, 2])
        self.assertListEqual(small_nnum([1, 2, 3], 4), [1, 2, 3])

    def test_invalid_input(self):
        self.assertRaises(TypeError, small_nnum, [1, 2, 3], 'n')
        self.assertRaises(TypeError, small_nnum, ['a', 'b', 'c'], 1)
